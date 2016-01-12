import mfib
import mfib_plot as plt

n = int(input("Введите число n: "))

#Получить список времени вычисления чисел Фибоначчи [от 0 до n]
#lTimeRec - рекурсия
#lTimeIter - цикл
lTimeRec, lTimeIter = mfib.getFibTime(n)

#Преобразовать значения в логарифмы
lTimeRecLog = mfib.getLogList(lTimeRec)
lTimeIterLog = mfib.getLogList(lTimeIter)

#Отобразить график 2 в 1
plt.showPlotFibTwoInOne(lTimeRec, lTimeIter,
                        lTimeRecLog, lTimeIterLog, vert=True)
