sum = 0


def trav(x, y):
    i = int(x)
    j = int(y)
    while i <= j:
        stringified_i = str(i)
        length = len(stringified_i)  # length of number string
        max_p_l = int(
            length / 2 + 1
        )  # because pattern needs to repeat at least twice (t.ex. 20002000: pattern=2000, max_p_l=4, length=8)

        for p_length in range(1, max_p_l):  # try all possible pattern lengths

            p = stringified_i[0:p_length]  # extract pattern

            # p:2000 length:8 p_length:4 compare:2000
            # 8 / 4 = 2. 2000 * 2 = 20002000 == stringified_i
            if int(length / p_length) * p == stringified_i:
                global sum
                sum += i
                break
        i += 1
    print("done")


txt = "9191906840-9191941337,7671-13230,2669677096-2669816099,2-12,229599-392092,48403409-48523311,96763-229430,1919163519-1919240770,74928-96389,638049-668065,34781-73835,736781-819688,831765539-831907263,5615884-5749554,14101091-14196519,7134383-7169141,413340-625418,849755289-849920418,7745350-7815119,16717-26267,4396832-4549887,87161544-87241541,4747436629-4747494891,335-549,867623-929630,53-77,1414-3089,940604-1043283,3444659-3500714,3629-7368,79-129,5488908-5597446,97922755-98097602,182-281,8336644992-8336729448,24-47,613-1077"
x = txt.split(",")
print(x)
for obj in x:
    o = obj.split("-")
    # print(o[0])
    # print(o[1])
    trav(o[0], o[1])


print(sum)
