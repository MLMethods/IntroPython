def getWords(fileName):
    dWords = {}
    with open(fileName) as fO:
        for line in fO:
            for word in line.split():
                word = word.strip(".,/;:\"'`!@#$%^&*-+= (){}|\\<>?").lower()
                if word.isalpha()==False:
                    continue
                if (word in dWords):
                    dWords[word] += 1
                else:
                    dWords[word] = 1
    return dWords

def getNTop(n, dWords):
    topCount = []
    topWord = []
    i = 0
    for key in sorted(dWords, key = dWords.get, reverse=True):
        topCount.append(dWords[key])
        topWord.append(key)
        i+=1
        if (i >= n):
            break
    return (topCount, topWord)