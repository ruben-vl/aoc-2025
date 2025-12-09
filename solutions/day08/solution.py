import math
from itertools import combinations

def parse_input(file: str) -> list[tuple[int, int, int]]:
    return [
        (int(row.split(",")[0]), int(row.split(",")[1]), int(row.split(",")[2]))
        for row in open(file)
    ]

def p1(input: list[tuple[int, int, int]]) -> int:
    circuits: set[tuple[tuple[int, int, int]]] = {(e,) for e in input}
    sorted_combinations = sorted(combinations(input,2), key=lambda comb: dist(comb[0],comb[1]))
    for i in range(1000):
        p1, p2 = sorted_combinations[i]
        sp1, sp2 = None, None
        for c in circuits:
            sp1 = c if p1 in c else sp1
            sp2 = c if p2 in c else sp2
        if sp1 is not None and sp2 is not None and sp1 != sp2:
            circuits.remove(sp1)
            circuits.remove(sp2)
            circuits.add(sp1 + sp2)
    circuit_sizes = sorted([len(c) for c in circuits], reverse=True)
    return circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]

def dist(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2) + math.pow((z1-z2),2))  

def p2(input: list[tuple[int, int, int]]) -> int:
    circuits: set[tuple[tuple[int, int, int]]] = {(e,) for e in input}
    sorted_combinations = sorted(combinations(input,2), key=lambda comb: dist(comb[0],comb[1]))
    for i in range(len(sorted_combinations)):
        p1, p2 = sorted_combinations[i]
        sp1, sp2 = None, None
        for c in circuits:
            sp1 = c if p1 in c else sp1
            sp2 = c if p2 in c else sp2
        if sp1 is not None and sp2 is not None and sp1 != sp2:
            circuits.remove(sp1)
            circuits.remove(sp2)
            circuits.add(sp1 + sp2)
        if len(circuits) == 1:
            return p1[0]*p2[0]
    return 0

if __name__ == "__main__":
    input = parse_input("solutions/day08/input.txt")
    print(f"[P1] The product of the sizes of the three largest circuits is: {p1(input)}")
    print(f"[P2] The product of the two last X coordinates is: {p2(input)}")