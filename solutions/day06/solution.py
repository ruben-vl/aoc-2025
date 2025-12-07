import math

def parse_input(file: str) -> list[list[int|str]]:
    rows = [row.rstrip().split() for row in open(file)]
    groups: list[list[int|str]] = []
    for i in range(len(rows[0])):
        group = [int(row[i]) if ri != len(rows)-1 else row[i] for ri, row in enumerate(rows)]
        groups.append(group)
    return groups

def p1(input: list[list[int|str]]) -> int:
    result = 0
    for group in input:
        if group[-1] == "+":
            result += sum([int(e) for e in group[:-1]])
        if group[-1] == "*":
            result += math.prod([int(e) for e in group[:-1]])
    return result

def p2(input: list[list[int|str]]) -> int:
    corrected_groups: list[list[int|str]] = []
    for group in input:
        actual_group: list[int|str] = []
        str_nums = [str(e) for e in group[:-1]]
        max_len = max([len(e) for e in str_nums])
        for col in range(max_len-1, -1, -1):
            num = "".join([num[col] for num in str_nums if len(num) > col])
            actual_group.append(int(num))
        corrected_groups.append(actual_group + [group[-1]])
    print(corrected_groups)
    return p1(corrected_groups)

if __name__ == "__main__":
    input = parse_input("solutions/day06/test.txt")
    print(f"[P1] The grand total is: {p1(input)}")
    print(f"[P2] The grand total is: {p2(input)}")