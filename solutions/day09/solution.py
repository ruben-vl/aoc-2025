from itertools import combinations

rtiles: list[tuple[int, int]] 
rtiles = [(int(line.split(",")[0]),int(line.split(",")[1])) for line in open("solutions/day09/input.txt")]

def tiles_between(t1: tuple[int, int], t2: tuple[int, int]) -> set[tuple[int, int]]:
    if t1[0] == t2[0]:
        return {(t1[0], i) for i in range(t1[1], t2[1]+1)} if t1[1] < t2[1] else {(t1[0], i) for i in range(t2[1], t1[1]+1)}
    if t1[1] == t2[1]:
        return {(i, t1[1]) for i in range(t1[0], t2[0]+1)} if t1[0] < t2[0] else {(i, t1[1]) for i in range(t2[0], t1[0]+1)}
    return set()

hull = set[tuple[int, int]]().union(*(tiles_between(rtiles[i], rtiles[(i+1) % len(rtiles)]) for i in range(len(rtiles))))

def floodfill(col: int, row: int) -> set[tuple[int, int]]:
    tiles: set[tuple[int, int]] = set()
    to_check: set[tuple[int, int]] = set([(col, row)])
    while len(to_check) > 0:
        c, r = to_check.pop()
        if (c,r) not in tiles:
            tiles.add((c,r))
            for neighbor in {(c,r+1),(c,r-1),(c+1,r),(c-1,r)}:
                if neighbor not in hull and neighbor not in tiles and neighbor not in to_check:
                    to_check.add(neighbor)
    return tiles

rgtiles: set[tuple[int, int]]
rgtiles = floodfill(98163,51305).union(hull)

def largest_area() -> int:
    return max([(abs(c1-c2)+1)*(abs(r1-r2)+1) for ((c1, r1),(c2, r2)) in combinations(rtiles, 2)])

def largest_rg_area() -> int:
    return max([valid_area(t1, t2) for (t1, t2) in combinations(rtiles, 2)])

def valid_area(t1: tuple[int, int], t2: tuple[int, int]) -> int:
    tiles: set[tuple[int, int]] = set()
    lcol, scol = max(t1[0],t2[0]), min(t1[0],t2[0])
    lrow, srow = max(t1[1],t2[1]), min(t1[1],t2[1])
    for col in range(scol, lcol+1):
        for row in range(srow, lrow+1):
            tiles.add((col,row))
    if all([t in rgtiles for t in tiles]):
        return (lcol-scol+1)*(lrow-srow+1)
    return 0

if __name__ == "__main__":
    print(f"[P1] The largest area is: {largest_area()}")
    print(f"[P2] The largest area is: {largest_rg_area()}")