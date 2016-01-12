import timeit as tmr
import math

def getFibTime(x):
    lTimeRec = []
    lTimeIter = []
    for i in range(x+1):
        tmrRec = tmr.Timer('fib.fibRec('+str(i)+')', setup='import mfibonacci as fib')
        tmrIter = tmr.Timer('fib.fibIter('+str(i)+')', setup='import mfibonacci as fib')
        lTimeRec.append(tmrRec.timeit(10))
        lTimeIter.append(tmrIter.timeit(10))
    return (lTimeRec, lTimeIter)

def getLogList(lEl):
    return list(map(math.log10, lEl))

