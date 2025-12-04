def parse_input(file: str) -> list[str]:
    return [row.rstrip() for row in open(file)]

def p1(input: list[str]) -> int:
    accessible = 0
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "@":
                if neighboring_rolls(r, c, input) < 4:
                    accessible += 1
    return accessible

def neighboring_rolls(row: int, col: int, input: list[str]) -> int:
    rolls_count = 0
    for r in range(row-1, row+2):
        if r >= 0 and r < len(input):
            for c in range(col-1, col+2):
                if c >= 0 and c < len(input[0]):
                    if not (r == row and c == col):
                        if input[r][c] == "@":
                            rolls_count += 1
    return rolls_count

def p2(input: list[str]) -> int:
    removed_count = 0
    for r in range(len(input)):
        for c in range(len(input[0])):
            if input[r][c] == "@":
                if neighboring_rolls(r, c, input) < 4:
                    input[r] = input[r][:c] + "." + input[r][c+1:]
                    removed_count += 1
    if removed_count == 0:
        return 0
    return removed_count + p2(input)

if __name__ == "__main__":
    input = parse_input("solutions/day04/input.txt")
    print(f"[P1] The amount of accessible rolls of paper is: {p1(input)}")
    print(f"[P2] The amount of paper that can be removed is: {p2(input)}")