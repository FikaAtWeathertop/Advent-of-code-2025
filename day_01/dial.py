currDialLoc = 50
zeroes = 0

def add(x):
    for _ in range(x):
        global currDialLoc
        currDialLoc += 1
        if currDialLoc > 99:
            currDialLoc = 0
    
def subtract(x):
    for _ in range(x):
        global currDialLoc
        currDialLoc -= 1
        if currDialLoc < 0:
            currDialLoc = 99

with open("input.txt") as file:
    for line in file:
        letter = line[0:1]
        amt = int(line[1:])
        #print(letter)
        #print(amt)
        
        if letter == "L":
            subtract(amt)
            print(f"Turned dial {amt} left")
        elif letter == "R":
            add(amt)
            print(f"Turned dial {amt} right")
        if currDialLoc == 0:
            zeroes += 1
print(zeroes)
    

