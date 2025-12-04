sum = 0

def trav(x, y):
    i = int(x)
    j = int(y)
    while i < j:
        stringified_i = str(i)
        if len(stringified_i) % 2 == 0: #even amount of numbers! possible invalid ID
            middle = int((len(stringified_i)/2))
            p1 = stringified_i[0:middle]
            p2 = stringified_i[middle:]
            
            if p1 == p2:
                global sum
                sum += i
                #print("Sum: " + str(sum))  
        i += 1
    print("done")

txt = "959516-995437,389276443-389465477,683-1336,15687-26722,91613-136893,4-18,6736-12582,92850684-93066214,65-101,6868676926-6868700146,535033-570760,826141-957696,365650-534331,1502-2812,309789-352254,79110404-79172400,18286593-18485520,34376-65398,26-63,3333208697-3333457635,202007-307147,1859689-1936942,9959142-10053234,2318919-2420944,5142771457-5142940464,1036065-1206184,46314118-46413048,3367-6093,237-481,591751-793578"
x = txt.split(",")
print(x)
for obj in x:
    o = obj.split("-")
    #print(o[0])
    #print(o[1])
    trav(o[0],o[1])


print(sum)