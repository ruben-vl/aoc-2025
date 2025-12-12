import math
from more_itertools import split_at

def parse_horizontally(path: str) -> tuple[list[list[int]], list[str]]:
    rows = [row.rstrip().split() for row in open(path)]
    return [list(map(int, s)) for s in zip(*rows[:-1])], rows[-1]

def parse_vertically(path: str) -> tuple[list[list[int]], list[str]]:
    rows = [row.replace('\n','') for row in open(path)]
    numstr = list(map(lambda x: "".join(x).replace(' ', ''), zip(*rows[:-1])))
    return [list(map(int, e)) for e in split_at(numstr, lambda x: x == '')], rows[-1].split()

def add_worksheet(numbers: list[list[int]], operations: list[str]) -> int:
    return sum([sum(numbers[i]) if operations[i] == '+' else math.prod(numbers[i]) 
                for i in range(len(numbers))])

if __name__ == "__main__":
    print(f"[P1] The total is: {add_worksheet(*parse_horizontally("solutions/day06/input.txt"))}")
    print(f"[P2] The total is: {add_worksheet(*parse_vertically("solutions/day06/input.txt"))}")