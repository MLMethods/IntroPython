import mcountword as mcw
import mcountword_plot as plt

#Получить словарь вида <слово-количество> из файла "input.txt"
dWords = mcw.getWords("input_mat.txt")
topNum = int(input("Введите число n: "))
#Получить списки:
#1) topWord: n наиболее часто встречающихся слов в тексте
#2) topCount: их количество в тексте
topCount, topWord = mcw.getNTop(topNum, dWords)
#Вывести график
plt.plotBarCWord(topCount, topWord, barColor='b')
