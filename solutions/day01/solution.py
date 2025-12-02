def parse_input(file: str) -> list[tuple[str,int]]:
    return [(line[0], int(line.rstrip()[1:])) for line in open(file)]

def p1(input: list[tuple[str,int]]) -> int:
    pos = [50]
    for dir, val in input:
        pos.append((pos[-1]-val)%100 if dir == "L" else (pos[-1]+val)%100)
    return pos.count(0)

if __name__ == "__main__":
    input = parse_input("solutions/day01/input.txt")
    print(f"The password to open the door is: {p1(input)}")