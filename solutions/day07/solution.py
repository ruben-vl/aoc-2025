from queue import PriorityQueue

def parse_input(file: str) -> list[str]:
    return [row.rstrip() for row in open(file)]

def p1(input: list[str]) -> int:
    splits = 0
    beam_cols = set([input[0].index("S")])
    for row in input[1:]:
        for beam in beam_cols.copy():
            if row[beam] == "^":
                splits += 1
                beam_cols.remove(beam)
                beam_cols.update({beam-1,beam+1})
    return splits

def p2(input: list[str]) -> int:
    paths: PriorityQueue[tuple[int,tuple[int,...]]] = PriorityQueue()
    paths.put((len(input), (input[0].index("S"),)))
    path_count = 0
    while not paths.empty():
        _, path = paths.get()
        if input[len(path)][path[-1]] == "^":
            new_paths = {(len(input)-(len(path)), path + (path[-1]-1,)), 
                         (len(input)-(len(path)), path + (path[-1]+1,))}
        else:
            new_paths = {(len(input)-(len(path)), path + (path[-1],))}
        if len(path) == len(input) - 1:
            path_count += len(new_paths)
        else:
            for new_path in new_paths:
                paths.put(new_path)
    return path_count

if __name__ == "__main__":
    input = parse_input("solutions/day07/input.txt")
    print(f"[P1] The number of splits is: {p1(input)}")
    print(f"[P2] The number of timelines is: {p2(input)}")