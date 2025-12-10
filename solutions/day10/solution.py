from typing import TypedDict
from queue import PriorityQueue

class Machine(TypedDict):
    buttons: set[tuple[int, ...]]
    lights: set[int]
    joltages: list[int]

def parse_input(manual: str) -> list[Machine]:
    machines: list[Machine] = []
    for specs in {spec for spec in open(manual)}:
        machine: Machine = {"lights": set(), "buttons": set(), "joltages": []}
        for part in specs.rstrip().split(' '):
            match part[0]:
                case '[':
                    machine["lights"] = light_idcs(part[1:-1])
                case '(':
                    machine["buttons"].add(button(part[1:-1]))
                case '{':
                    machine["joltages"] = joltage_reqs(part[1:-1])
                case _:
                    pass
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

def p2(input: list[Machine]):
    presses = 0
    for i, machine in enumerate(input):
        print(f"Handling machine {i}")
        goal = machine["joltages"]
        seen_states: set[tuple[int,...]] = set()
        pq: PriorityQueue[tuple[int, list[int]]] = PriorityQueue()
        pq.put((0, [0]*len(goal)))
        while not pq.empty():
            prio, state = pq.get()
            print(state)
            if state == goal:
                presses += prio
                break
            for button in machine["buttons"]:
                new_state = [v+1 if i in button else v for i,v in enumerate(state)]
                if not tuple(new_state) in seen_states and not any([nv > v for nv, v in zip(new_state, goal)]):
                    seen_states.add(tuple(new_state))
                    pq.put((prio+1, new_state))
    return presses

if __name__ == "__main__":
    input = parse_input("solutions/day10/input.txt")
    print(f"[P1] The fewest button presses required: {p1(input)}")
    print(f"[P2] The fewest button presses required: {p2(input)}")