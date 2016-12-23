
with open("titles.txt", "r") as f:
    titles = f.read().split("\n")[:-1]
with open("texts.txt", "r") as f:
    texts = f.read().split("\n")[:-1]


dupl = dict()

for title in titles:
    if title not in dupl:
        dupl[title] = 0
    dupl[title] += 1
    
newtitles = []
newtexts = []

for i in range(len(titles)):
    a = titles[i]
    b = texts[i]
    if dupl[a] == -1:
        continue
    if b == "":
        continue
    if len(a) > 100 or len(b) > 500:
        continue
    if dupl[a] > 1:
        #mark duplicate
        dupl[a] = -1
    newtitles.append(a)
    newtexts.append(b)

print len(newtitles), len(newtexts)
savetitles = "\n".join(newtitles)
savetexts = "\n".join(newtexts)

with open("titlesReady.txt", "w") as f:
    f.write(savetitles)

with open("textsReady.txt", "w") as f:
    f.write(savetexts)



