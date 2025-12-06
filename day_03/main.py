with open("day_03/test.txt") as file:
    banks = [line.strip() for line in file.readlines()]

    def findHighIndex(bank: str, start: int, end: int):
        global digit1_index, digit2_index
        index = start
        highestNr = 0
        highestNrIndex = start
        while index < end:
            if (int(bank[index]) > highestNr) and (index != digit1_index):
                highestNr = int(bank[index])
                highestNrIndex = index
            index += 1
        return highestNrIndex
    
    def extractAndConcat(bank: str, firstIndex: int, secondIndex: int):
        test = int(bank[firstIndex] + bank[secondIndex])
        return test
    
    def remove3tocreatelargestnumber(bank: str):
        newbank = []
        toRemove = len(bank) - 12
        removedCount = 0
        
        for digit in bank:
            while newbank and newbank[len(newbank)-1] < digit and removedCount < toRemove:
                newbank.pop()
                removedCount += 1
            newbank.append(digit)
        
        while removedCount < toRemove:
            newbank.pop()
            removedCount += 1

        return ''.join(newbank)
                

    task1sum = 0
    task2sum = 0
    for bank in banks:
        digit1_index = digit2_index = -1
        digit1_index = findHighIndex(bank, 0, len(bank)-1)
        digit2_index = findHighIndex(bank, digit1_index, len(bank))
        
        if digit1_index > digit2_index:
            digit1_index, digit2_index = digit2_index, digit1_index
    
        task1result = extractAndConcat(bank, digit1_index, digit2_index)
        #print("digit1index ",digit1_index)
        #print("digit2index ",digit2_index)
        print("result task1: ", task1result)
        task1sum += task1result

        task2result = remove3tocreatelargestnumber(bank)
        print("result task2: ", task2result)
        task2sum += int(task2result)

    print("task1sum: ", task1sum)
    print("task2sum: ", task2sum)
