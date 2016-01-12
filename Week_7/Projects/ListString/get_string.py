lNumInt = [1,2,3,4]

#Conversion List of numbers -> string
#Approach 1
strNumInt1 = " ".join(map(str, lNumInt))
print("strNumInt1 = '" + strNumInt1+"'")

#Approach 2
strNumInt2 = str(lNumInt[0])
for i in range(1, len(lNumInt)):
    strNumInt2 = strNumInt2 + " " + str(lNumInt[i])
print("strNumInt2 = '" + strNumInt2+"'")

#Approach 3
strNumInt3 = ""
for indx, el in enumerate(lNumInt):
    if (indx == 0):
        strNumInt3 = str(el)
    else:
        strNumInt3 = strNumInt3 + " " + str(el)
print("strNumInt3 = '" + strNumInt3+"'")

#With additional whitespace
print("With additional whitespace:")
strNumInt4 = ""
for el in lNumInt:
    #strNumInt3 += str(lNumInt[i]) + " "
    strNumInt4 = strNumInt4 + str(el) + " "
print("strNumInt4 = '" + strNumInt4+"'")

strNumInt5 = ""
for i in range(0, len(lNumInt)):
    #strNumInt5 += str(lNumInt[i]) + " "
    strNumInt5 = strNumInt5 + str(lNumInt[i]) + " "
print("strNumInt5 = '" + strNumInt5+"'")