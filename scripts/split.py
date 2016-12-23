import random

with open("titles", "r") as f:
    titles = f.read().split("\n")[:-1]

with open("texts", "r") as f:
    texts = f.read().split("\n")[:-1]

pairs = []
for i in range(len(titles)):
    pairs.append((titles[i], texts[i]))

random.shuffle(pairs)

train = pairs[:32000]
val = pairs[32000:32000 + 3134]
test = pairs[32000 + 3134:]

print len(train), len(val), len(test)

def createSet(name, data):
    titles = [x[0] for x in data]
    texts = [x[1] for x in data]
    titles = "\n".join(titles)
    texts  = "\n".join(texts)
    with open(name + ".in", "w") as f:
        f.write(titles)
    with open(name + ".out", "w") as f:
        f.write(texts)

#createSet("train", train)
#createSet("val", val)
#createSet("test", test)

