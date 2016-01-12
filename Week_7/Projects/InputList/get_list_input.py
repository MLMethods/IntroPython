lStr = input("Enter your line of numbers: ").split()

#Conversion String -> List of float numbers
#Approach 1
lNumFloat1 = list(map(float, lStr))
print("lNumFloat1 = " + str(lNumFloat1))

#Approach 2
lNumFloat2 = [float(el) for el in lStr]
print("lNumFloat2 = " + str(lNumFloat2))

#Approach 3
lNumFloat3 = []
for el in lStr:
    lNumFloat3.append(float(el))
print("lNumFloat3 = " + str(lNumFloat3))

#Approach 4
lNumFloat4 = []
for i in range(len(lStr)):
    lNumFloat4.append(float(lStr[i]))
print("lNumFloat4 = " + str(lNumFloat4))

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