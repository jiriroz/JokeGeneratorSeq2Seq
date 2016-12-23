import matplotlib.pyplot as plt
import numpy as np

countsTitles = []
with open("titlesAnalyze.txt", "r") as f:
    spl = f.read().split("\n")
    countsTitles = np.array([len(x) for x in spl])

countsTexts = []
with open("textsAnalyze.txt", "r") as f:
    spl = f.read().split("\n")
    countsTexts = np.array([len(x) for x in spl])

print "mean, std of titles"
print np.mean(countsTitles), np.std(countsTitles)
print "mean, std of texts"
print np.mean(countsTexts), np.std(countsTexts)

upperBound = 20
while True:
    ct = len([x for x in countsTitles if x <= upperBound])
    p = float(ct) / len(countsTitles)
    print "Proportion of titles shorter than {}: {}".format(upperBound, p)
    upperBound = int(upperBound * 1.2)
    if p == 1.0:
        break

print ""

upperBound = 5
while True:
    ct = len([x for x in countsTexts if x <= upperBound])
    p = float(ct) / len(countsTexts)
    print "Proportion of texts shorter than {}: {}".format(upperBound, p)
    upperBound = upperBound + 5
    if p == 1.0:
        break


'''
n, bins1, patches = plt.hist(countsTexts, 50, normed=0, facecolor='green', alpha=0.75)
plt.title("Texts")
plt.figure()
n, bins2, patches = plt.hist(countsTitles, 50, normed=0, facecolor='blue', alpha=0.75)
plt.title("Titles")

plt.show()
'''
