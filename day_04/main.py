with open("day_04/input.txt") as file:
    line = [line.strip() for line in file.readlines()]

    coords = {}
    for y, ln in enumerate(line):
        for x, character in enumerate(ln):
            coords[(x, y)] = character
    
    def getCoord(x: int, y:int):
        return coords.get((x, y))

    def setCoord(x: int, y:int, value: str):
        coords[(x, y)] = value

    def countEightAdjacents(x: int, y:int):
        occupiedCount = 0
        for adjY in range(y-1, y+2):
            for adjX in range(x-1, x+2):
                if (adjX, adjY) != (x, y):
                    if getCoord(adjX, adjY) == '@':
                        occupiedCount += 1
        return occupiedCount

    def readOrMarkMap(mark: bool):
        for coord in coords:
            x, y = coord
            if getCoord(x, y) == 'X':
                setCoord(x, y, '.')
        
        count = 0
        to_mark = [] 
        for coord in coords:
            x, y = coord
            if (getCoord(x, y) == '@' and countEightAdjacents(x, y) <= 3):
                to_mark.append((x, y))
                count += 1

        if mark:
            for x, y in to_mark:
                setCoord(x, y, 'X')
        return count

    def printMap():
        maxX = max(x for x, y in coords.keys())
        maxY = max(y for x, y in coords.keys())
        for y in range(maxY + 1):
            line = ''
            for x in range(maxX + 1):
                line += getCoord(x, y)
            print(line)


    TotalCount = 0
    count = -1

    while count != 0:
        count = readOrMarkMap(False)
        if count == 0:
            break
        readOrMarkMap(True)
        TotalCount += count
        print("Total count: ", TotalCount, ", iteration count: ", count)
    printMap()