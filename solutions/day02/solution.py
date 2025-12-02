def parse_input(file: str) -> list[tuple[int, int]]:
    return [(int(range.split('-')[0]), int(range.split('-')[1])) for range in open(file).readline().split(',')]

def p1(input: list[tuple[int, int]]) -> int:
    sum = 0
    for start, end in input:
        for n in range(start, end+1):
            strn, lstrn = str(n), len(str(n))
            if lstrn > 1 and strn[:lstrn//2] == strn[lstrn//2:]:
                sum += n
    return sum

if __name__ == "__main__":
    input = parse_input("solutions/day02/input.txt")
    print(f"[P1] The sum of all invalid IDs is: {p1(input)}")