freshRanges = []
ingredientIDs = []

def fetchRanges():
    with open("day_05/input_ranges.txt") as file:
        line = [line.strip() for line in file.readlines()]
        global freshRanges
        for ln in line:
            startRange, endRange = int(ln.split("-")[0]), int(ln.split("-")[1])
            freshRanges.append((startRange, endRange))

def fetchValues():
    with open("day_05/input_all.txt") as file:
        line = [line.strip() for line in file.readlines()]
        global ingredientIDs
        ingredientIDs = [int(ln) for ln in line]

def isValueInRanges(value: int) -> bool:
    for startRange, endRange in freshRanges:
        if startRange <= value <= endRange:
            return True
    return False

fetchRanges()
print("Ranges fetched!")
fetchValues()
print("Values fetched!")

freshIngredientCounter = 0
for ingredientID in ingredientIDs:
    if isValueInRanges(ingredientID):
        freshIngredientCounter += 1

print("Fresh ingredient counter: ", freshIngredientCounter)