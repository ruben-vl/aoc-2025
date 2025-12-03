def parse_input(file: str) -> list[list[int]]:
    return [[int(c) for c in bank.rstrip()] for bank in open(file)]

def p1(input: list[list[int]]) -> int:
    total_joltage = 0
    for bank in input:
        max_tenths = max(bank[:-1])
        max_remainder = max(bank[bank.index(max_tenths)+1:])
        total_joltage += 10*max_tenths + max_remainder
    return total_joltage

def p2(input: list[list[int]]) -> int:
    total_joltage = 0
    for bank in input:
        batteries = [max(bank[:-11])]
        idx = bank.index(batteries[0])
        for rest in range(10,0,-1):
            batteries.append(max(bank[idx+1:-rest]))
            idx += 1 + bank[idx+1:-rest].index(batteries[-1])
        batteries.append(max(bank[idx+1:]))
        total_joltage += int("".join(map(str,batteries)))
    return total_joltage

if __name__ == "__main__":
    input = parse_input("solutions/day03/input.txt")
    print(f"[P1] The total joltage output is: {p1(input)}")
    print(f"[P2] The total joltage output is: {p2(input)}")