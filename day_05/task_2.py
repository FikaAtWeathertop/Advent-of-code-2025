freshRanges = []
freshIngredientIDs = []

def fetchRanges():
    with open("day_05/input_ranges.txt") as file:
        line = [line.strip() for line in file.readlines()]
        global freshRanges
        for ln in line:
            startRange, endRange = int(ln.split("-")[0]), int(ln.split("-")[1])
            freshRanges.append((startRange, endRange))

def count_fresh_ids(ranges):
    if not ranges:
        return 0
    
    sorted_ranges = sorted(ranges)
    
    merged = [sorted_ranges[0]]
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1: 
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    
    return sum(end - start + 1 for start, end in merged)


fetchRanges()
print("Ranges fetched!")
print("Fresh ingredient IDs populated!", count_fresh_ids(freshRanges))


