high_1 = 0
high_2 = 0

with open("test.txt") as file:
    all_lines = []
    for line in file.readlines():
        new_line = []
        # this is how you would loop through each alphabet
        for chars in line:
            if(chars != "\n"):
                new_line.append(int(chars))
        all_lines.append(new_line)
    
    

    for line in all_lines:
        print(line)
        sorted_line = line.sort()
        print(sorted_line)


        # for letter in line:
            
    #         if(letter > high_1):
    #             high_1 = letter
                

            

#print(all_lines)
    