def fibRec(x):
    if(x == 0):
        return 0
    elif (x == 1):
        return 1
    else:
        return fibRec(x-1) + fibRec(x-2)

def fibIter(x):
    if(x == 0):
        return 0
    elif (x == 1):
        return 1
    else:
        n1 = 0; n2 = 1
        for n in range(2, x+1):
            n2 = n1 + n2
            n1 = n2 - n1
        return n2