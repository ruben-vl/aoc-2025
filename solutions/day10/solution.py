from typing import TypedDict
from queue import PriorityQueue
from ortools.sat.python import cp_model

class Machine(TypedDict):
    buttons: set[tuple[int, ...]]
    lights: set[int]
    joltages: list[int]

def parse_input(manual: str) -> list[Machine]:
    machines: list[Machine] = []
    for specs in {spec.rstrip() for spec in open(manual)}:
        machine: Machine = {"lights": set(), "buttons": set(), "joltages": []}
        for part in specs.split(' '):
            match part[0]:
                case '[':
                    machine["lights"] = light_idcs(part[1:-1])
                case '(':
                    machine["buttons"].add(button(part[1:-1]))
                case '{':
                    machine["joltages"] = joltage_reqs(part[1:-1])
                case _:
                    raise RuntimeError(f"Unexpected part in input: {part}")
        machines.append(machine)
    return machines

def light_idcs(diagram: str) -> set[int]:
    return {i for i,v in enumerate(diagram) if v == "#"}

def button(diagram: str) -> tuple[int,...]:
    return tuple([int(v) for v in diagram.split(',')])

def joltage_reqs(diagram: str) -> list[int]:
    return [int(v) for v in diagram.split(',')]

type IndicatorLights = set[int]

def p1(input: list[Machine]) -> int:
    presses = 0
    for machine in input:
        goal = machine["lights"]
        seen_states: set[tuple[int,...]] = set([tuple()])
        pq: PriorityQueue[tuple[int, IndicatorLights]] = PriorityQueue()
        pq.put((0, set()))
        while not pq.empty():
            prio, state = pq.get()
            if state == goal:
                presses += prio
                break
            for button in machine["buttons"]:
                new_state = state.symmetric_difference(set(button))
                comp_state = tuple(sorted(new_state))
                if comp_state not in seen_states:
                    seen_states.add(comp_state)
                    pq.put((prio+1, new_state))
    return presses

def p2(input: list[Machine]) -> int:
    presses = 0
    for machine in input:
        goal = machine["joltages"]

        model = cp_model.CpModel()
        variables = [model.NewIntVar(0, sum(goal), f"button_{j}") for j in range(len(machine["buttons"]))]
        for idx in range(len(goal)):
            relevant_buttons = [variables[bi] for bi, b in enumerate(list(machine["buttons"])) if idx in b]
            model.Add(sum(relevant_buttons) == goal[idx])
        model.Minimize(sum(variables))

        solver = cp_model.CpSolver()
        solver.Solve(model)
        presses += int(solver.ObjectiveValue())
    return presses

if __name__ == "__main__":
    input = parse_input("solutions/day10/input.txt")
    print(f"[P1] The fewest button presses required: {p1(input)}")
    print(f"[P2] The fewest button presses required: {p2(input)}")