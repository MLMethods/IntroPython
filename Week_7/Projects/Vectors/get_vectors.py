#Functions-----------------------
def vsum(x, y, n):
    s=[]
    for i in range(0, n):
        s.append(x[i]+y[i])
    return s
def vabssubstr(x, y, n):
    s=[]
    for i in range(0, n):
        s.append(abs(x[i]-y[i]))
    return s
def distance2(x):
    s = 0
    for i in range(0, len(x)):
        #s += x[i]**2
        s = s + x[i]**2
    return s**0.5
def distance2_v2(x, y, n):
    s = 0
    for i in range(n):
        s = s + (x[i]-y[i])**2
    return s**0.5
def vscalarprod(x, y, n):
    s = 0
    for i in range(0, n):
        s += x[i]*y[i]
    return s
#----------------------------------

#Main part-------------------------
with open("input_vector_1.txt") as fO:
    m = int(fO.readline().rstrip())
    v1 = [int(el) for el in fO.readline().split()]
    v2 = [int(el) for el in fO.readline().split()]

if (m!=len(v1) or m!=len(v2)):
    print("The dimension (the number of elements) of one of the vectors differs from m.")
    exit()
    
print("1) Vectors:")
print("   v1 = " + str(v1))
print("   v2 = " + str(v2))

vS = vsum(v1,v2,m) #Sum
print("2) Sum:\n   vS = "+str(vS))

vAS = vabssubstr(v1, v2, m) #Subtraction
print("3) Subtraction (abs):\n   vAS = "+str(vAS))

d1 = distance2(vAS) #Euclidean distance
print("4) Euclidean distance:")
print("   Version 1: d1 = "+str(d1))

d2 = distance2_v2(v1, v2, m) #Euclidean distance
print("   Version 2: d2 = "+str(d2))

p = vscalarprod(v1,v2,m) #Scalar product
print("5) Scalar product:\n   p = "+str(p))
#---------------------------------