from functools import lru_cache

diagram = [row.rstrip() for row in open("solutions/day07/input.txt")]

def splits() -> int:
    splits = 0
    beam_cols = set([diagram[0].index("S")])
    for row in diagram[1:]:
        for beam in beam_cols.copy():
            if row[beam] == "^":
                splits += 1
                beam_cols.remove(beam)
                beam_cols.update({beam-1,beam+1})
    return splits

@lru_cache(maxsize=1024, typed=False)
def paths(row: int, col: int) -> int:
    if row == len(diagram)-1: return 1
    if diagram[row+1][col] == "^":
        return paths(row+1, col-1) + paths(row+1, col+1)
    return paths(row+1, col)

if __name__ == "__main__":
    print(f"[P1] The number of splits is: {splits()}")
    print(f"[P2] The number of timelines is: {paths(0,diagram[0].index("S"))}")