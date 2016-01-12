#Functions-----------------------
def getSum(mX, mY, n):
    mZ = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(mX[i][j]+mY[i][j])
        mZ.append(row)
    return mZ
def getSum_v2(mX, mY, n):
    mZ = [[mX[i][j]+mY[i][j] for j in range(n)] for i in range(n)]
    return  mZ

def getMult(mX, mY, n):
    mZ = []
    for i in range(n):
        row = []
        for j in range(n):
            s = 0
            for k in range(n):
                s += mX[i][k]*mY[k][j]
            row.append(s)
        mZ.append(row)
    return mZ
def getMult_v2(mX, mY, n):
    mZ = []
    for i in range(n):
        row = []
        rowX = mX[i]
        for j in range(n):
            colY = []
            for k in range(n):
                colY.append(mY[k][j])
            row.append(__vscalarprod(rowX, colY, n))
        mZ.append(row)
    return mZ
def getMult_v3(mX, mY, n):
    colY = list(zip(*mY))
    rowX = mX
    mZ = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(__vscalarprod(rowX[i], colY[j], n))
        mZ.append(row)
    return mZ
def getMult_v4(mX, mY):
    mZ = [[sum(x*y for x,y in zip(rowX,colY)) for colY in zip(*mY)] for rowX in mX]
    return mZ

def __vscalarprod(x, y, n):
    s = 0
    for i in range(0, n):
        s += x[i]*y[i]
    return s
#--------------------------------

#Main part-----------------------
#Some notes---------
#Matrices are square (m x m)
#     1 2 3
# A = 4 5 6   ->   mA = [[1,2,3], [4,5,6],[7,8,9]
#     7 8 9
# A(1,1) = 1, A(2,2) = 5, A(3,2) = 8
# mA[0][0] = 1, mA[1][1] = 5, mA[2][1] = 8
#-------------------
with open("input_matrix.txt", "rt") as fO:
    m = int(fO.readline().rstrip()) #the number of rows and columns
    mA = [] #First matrix A
    mB = [] #Second matrix B
    #Composing matrix A
    for i in range(m):
        lNum = [int(el) for el in fO.readline().split()]
        mA.append(lNum)
    #Composing matrix B
    for i in range(m):
        lNum = [int(el) for el in fO.readline().split()]
        mB.append(lNum)

print("1) Initial data:")
print("   Size of matrix: %ix%i" % (m, m))
print("   Matrices:")
print("   A = " + str(mA))
print("   B = " + str(mB))

s1 = getSum(mA, mB, m)
s2 = getSum_v2(mA, mB, m)

print("2) Sum of matrices A and B:")
print("   Version 1: s1 = " + str(s1))
print("   Version 2: s2 = " + str(s2))

p1 = getMult(mA, mB, m)
p2 = getMult_v2(mA, mB, m)
p3 = getMult_v3(mA, mB, m)
p4 = getMult_v4(mA, mB)
print("3) Product of matrices A and B:")
print("   Version 1: p1 = " + str(p1))
print("   Version 2: p2 = " + str(p2))
print("   Version 3: p3 = " + str(p3))
print("   Version 4: p4 = " + str(p4))
#--------------------------------