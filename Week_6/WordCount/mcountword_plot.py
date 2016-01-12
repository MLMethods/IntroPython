import matplotlib.pyplot as plt

def plotBarCWord(lCounts, lWords, width = 0.6,
                 barColor = 'g', grid = True,
                 wordRotation = 'vertical'):
    width = 0.6
    plt.bar(range(len(lCounts)), lCounts, width, color=barColor)
    plt.xticks([el + width/2.0 for el in range(len(lCounts))], lWords, rotation=wordRotation, fontsize = 14)
    plt.grid(grid)
    plt.title("Word Count", fontsize = 18)
    plt.ylabel("Count", fontsize = 16)
    plt.xlabel("Word", fontsize = 16)
    plt.show()