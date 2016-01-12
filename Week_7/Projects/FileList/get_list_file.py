with open("input_list.txt", "rt") as fO:
    strLine = fO.readline().rstrip()

print("Initial line:")
print("strLine = '" + strLine + "'")
print("-----------------------")

lStr = strLine.split()
print("lStr = " + str(lStr))

#Conversion String -> List of int numbers
#Approach 1
lNumInt1 = list(map(int, lStr))
print("lNumInt1 = " + str(lNumInt1))

#Approach 2
lNumInt2 = [int(el) for el in lStr]
print("lNumInt2 = " + str(lNumInt2))

#Approach 3
lNumInt3 = []
for el in lStr:
    lNumInt3.append(int(el))
print("lNumInt3 = " + str(lNumInt3))

#Approach 4
lNumInt4 = []
for i in range(len(lStr)):
    lNumInt4.append(int(lStr[i]))
print("lNumInt4 = " + str(lNumInt4))