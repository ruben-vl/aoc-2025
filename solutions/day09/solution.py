from itertools import combinations

def parse_input(file: str) -> list[tuple[int,int]]:
    return [(int(line.split(",")[0]),int(line.split(",")[1])) for line in open(file)]

def p1(input: list[tuple[int,int]]) -> int:
    largest_area = 0
    for ((c1, r1),(c2, r2)) in combinations(input, 2):
        area = (abs(c1-c2)+1)*(abs(r1-r2)+1)
        largest_area = area if area > largest_area else largest_area
    return largest_area

if __name__ == "__main__":
    input = parse_input("solutions/day09/input.txt")
    print(f"[P1] The largest area is: {p1(input)}")