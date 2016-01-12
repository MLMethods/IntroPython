import matplotlib.pyplot as plt

#Show-------------------------------
def showPlotFib(lTimeRec, lTimeIter, secLog):
    plt.figure("Fibonacci")
    plotFib(lTimeRec, lTimeIter, secLog)
    plt.show()
def showTwoPlotFib(lTimeRec1, lTimeIter1, lTimeRec2, lTimeIter2):
    plotTwoFib(lTimeRec1, lTimeIter1, lTimeRec2, lTimeIter2)
    plt.show()
def showPlotFibTwoInOne(lTimeRec1, lTimeIter1, lTimeRec2, lTimeIter2, vert = True):
    plt.figure("Fibonacci")
    plotFibTwoInOne(lTimeRec1, lTimeIter1, lTimeRec2, lTimeIter2, vert)
    plt.show()
#-----------------------------------

#Plot-------------------------------
def plotFib(lTimeRec, lTimeIter, secLog):
    x = range(len(lTimeRec))
    plt.plot(x, lTimeRec, color='r', marker='o', label='Recursion')
    plt.plot(x, lTimeIter, color='b', marker='o', label='Loop')

    __prePlotSec(x, secLog)

def plotTwoFib(lTimeRec1, lTimeIter1, lTimeRec2, lTimeIter2):
    plt.figure("Fibonacci (sec)")
    plotFib(lTimeRec1, lTimeIter1, False)
    plt.figure("Fibonacci (log(sec))")
    plotFib(lTimeRec2, lTimeIter2, True)

def plotFibTwoInOne(lTimeRec1, lTimeIter1, lTimeRec2, lTimeIter2, vert):
    if vert == True:
        plt.subplot(211)
    else:
        plt.subplot(121)

    plotFib(lTimeRec1, lTimeIter1, False)

    if vert == True:
        plt.subplot(212)
    else:
        plt.subplot(122)

    plotFib(lTimeRec2, lTimeIter2, True)
#----------------------------------
def __prePlotSec(x, secLog):
    #plt.title("The Fibonacci numbers")
    plt.xlabel("Fibonacci number", fontsize = 12)
    if secLog == False:
        plt.ylabel("Time (sec)", fontsize = 12)
    else:
        plt.ylabel("Time (log(sec))", fontsize = 12)
    plt.xticks(x)
    plt.grid(True)
    plt.legend(("Recursion", "Loop"), loc = "upper left")


"""
def plotFibSecLogVert():
    x = range(0,n+1)
    plt.figure("Fibonacci (sec)")
    plt.subplot(211)
    plt.title("The Fibonacci numbers")
    plt.xlabel("Fibonacci number", fontsize = 12)
    plt.ylabel("Time (sec)", fontsize = 12)

    plt.plot(x, lTimeRec, color='r', marker='o', label='Recursion')
    plt.plot(x, lTimeIter, color='b', marker='o', label='Loop')

    #p = plt.plot(x, lTimeRec, 'r', x, lTimeRec, 'ro', x, lTimeIter, 'b', x, lTimeIter, 'bo')
    plt.xticks(x)
    plt.grid(True)
    plt.legend(("Recursion", "Loop"), loc = "upper left")

    plt.subplot(212)
    plt.xlabel("Fibonacci number", fontsize = 12)
    plt.ylabel("Time (log(sec))", fontsize = 12)
    plt.plot(x, lTimeRecLog, color='r', marker='o', label='Recursion')
    plt.plot(x, lTimeIterLog, color='b', marker='o', label='Loop')
    plt.xticks(x)
    plt.grid(True)
    plt.legend(("Recursion", "Loop"), loc = "upper left")

    plt.show()

def plotFibSecLogHoriz():
    x = range(0,n+1)
    plt.figure("Fibonacci (sec)")
    plt.subplot(121)
    plt.title("The Fibonacci numbers")
    plt.xlabel("Fibonacci number", fontsize = 12)
    plt.ylabel("Time (sec)", fontsize = 12)

    plt.plot(x, lTimeRec, color='r', marker='o', label='Recursion')
    plt.plot(x, lTimeIter, color='b', marker='o', label='Loop')

    #p = plt.plot(x, lTimeRec, 'r', x, lTimeRec, 'ro', x, lTimeIter, 'b', x, lTimeIter, 'bo')
    plt.xticks(x)
    plt.grid(True)
    plt.legend(("Recursion", "Loop"), loc = "upper left")

    plt.subplot(122)
    plt.xlabel("Fibonacci number", fontsize = 12)
    plt.ylabel("Time (log(sec))", fontsize = 12)
    plt.plot(x, lTimeRecLog, color='r', marker='o', label='Recursion')
    plt.plot(x, lTimeIterLog, color='b', marker='o', label='Loop')
    plt.xticks(x)
    plt.grid(True)
    plt.legend(("Recursion", "Loop"), loc = "upper left")

    plt.show()
    """