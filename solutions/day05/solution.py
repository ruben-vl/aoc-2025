def parse_input(file: str) -> tuple[list[tuple[int,int]], list[int]]:
    db = [row.rstrip() for row in open(file)]
    ranges: list[tuple[int,int]] = []
    ingredients: list[int] = []
    processing_ranges = True
    for row in db:
        if row == "":
            processing_ranges = False
            continue
        if processing_ranges:
            ranges.append((int(row.split('-')[0]), int(row.split('-')[1])))
        else:
            ingredients.append(int(row))
    return ranges, ingredients

def p1(ranges: list[tuple[int, int]], ingredients: list[int]) -> int:
    fresh_count = 0
    for ingredient in ingredients:
        for start, end in ranges:
            if ingredient >= start and ingredient <= end:
                fresh_count += 1
                break
    return fresh_count

def p2(ranges: list[tuple[int, int]]) -> int:
    sranges = sorted(ranges)
    for idx in range(len(ranges)-1):
        if sranges[idx] == (0,0): continue
        _, curr_e = sranges[idx]
        for other_i, (other_s, other_e) in enumerate(sranges[idx+1:]):
            if other_s <= curr_e:
                if other_e <= curr_e:
                    sranges[idx+1+other_i] = (0,0)
                else:
                    sranges[idx+1+other_i] = (curr_e+1, other_e)
    fresh_count = 0
    for start, end in sranges:
        if not (start == 0 and end == 0):
            fresh_count += end - start + 1
    return fresh_count

if __name__ == "__main__":
    ranges, ingredients = parse_input("solutions/day05/input.txt")
    print(f"[P1] The amount of fresh ingredients is: {p1(ranges, ingredients)}")
    print(f"[P2] The total number of IDs considered fresh is: {p2(ranges)}")