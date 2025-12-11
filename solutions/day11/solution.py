from functools import lru_cache

outputs: dict[str, set[str]] = {}

def parse_input(file: str):
    for row in [row.rstrip() for row in open(file)]:
        outputs[row[:3]] = set(row[5:].split(' '))

@lru_cache(maxsize=1024, typed=False)
def paths(start: str, goal: str, dac: bool, fft: bool) -> int:
    if start == "dac": dac = True
    if start == "fft": fft = True
    if start == goal: return 1 if dac and fft else 0
    return sum([paths(output, goal, dac, fft) for output in outputs[start]])

if __name__ == "__main__":
    input = parse_input("solutions/day11/input.txt")
    print(f"[P1] The solution is: {paths("you", "out", True, True)}")
    print(f"[P2] The solution is: {paths("svr", "out", False, False)}")