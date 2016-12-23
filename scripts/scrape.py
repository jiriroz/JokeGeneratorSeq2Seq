from lxml import html
import requests
import time
import dateutil.parser as dp
import datetime

TITLE_CACHE = []
TEXT_CACHE = []
TITLE_FILE = "titles.txt"
TEXT_FILE = "texts.txt"

def main():
    #create empty files
    #with open(TITLE_FILE, "w") as f:
    #    f.write("")
    #with open(TEXT_FILE, "w") as f:
    #    f.write("")
    startTime = 1429132009
    stopTime = 0
    getAll(startTime, stopTime)

def getAll(startTime, stopTime):
    timeUntil = startTime
    i = 0
    totalQ = 0
    while stopCondition(timeUntil, stopTime, i):
        lastPost, q, total, tree = getData(timeUntil)
        if total == 0:
            wait = tree.xpath("//p[3]/text()")[0]
            secs = int(wait.split(" ")[2])
            time.sleep(secs + 0.5)
            continue
        timeUntil = lastPost - 1
        totalQ += q
        i += 1
        print timeUntil
    print totalQ

def stopCondition(currentPostT, stopTime, iteration):
    return currentPostT > stopTime

def unitToDate(unix):
    return datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')


def getData(timeUntil):
    low = 0
    high = timeUntil
    url = "https://www.reddit.com/r/Jokes/search?q=timestamp%3A{}..{}&sort=new&restrict_sr=on&syntax=cloudsearch".format(low, high)

    page = requests.get(url)
    tree = html.fromstring(page.content)

    results = tree.xpath("//header[@class='search-result-header']/..")

    unix = 1
    qCount = 0
    totalCount = 0
    for entry in results:
        totalCount += 1
        try:
            title = entry.xpath("header/a/text()")[0]
            title = title.strip()
            title = title.encode("utf-8")
            text = entry.xpath("div[2]/div[1]/div[1]/p/text()")
            text = " ".join(text)
            text = text.encode("utf-8")
            t = entry.xpath("div[1]/span[3]/time[1]/@datetime")[0]
            unix = dp.parse(t).strftime('%s')
            unix = int(unix)
        except Exception as e:
            continue
        if isQuestion(title):
            qCount += 1
            saveOne(title, text)
    return unix, qCount, totalCount, tree
    
def isQuestion(title):
    if type(title) is not str:
            return False
    if len(title) == 0:
        return False
    return title[-1] == "?"

def saveOne(title, text):
    TITLE_CACHE.append(title)
    TEXT_CACHE.append(text)
    if len(TITLE_CACHE) == 10:
        save()

def save():
    global TITLE_CACHE, TEXT_CACHE
    if len(TITLE_CACHE) != len(TEXT_CACHE):
        print "Number of titles and texts to save differs!"
        TITLE_CACHE, TEXT_CACHE = [], []
        return
    #get rid of newlines
    TITLE_CACHE = [" ".join(x.split("\n")) for x in TITLE_CACHE]
    TEXT_CACHE = [" ".join(x.split("\n")) for x in TEXT_CACHE]
    titles = "\n".join(TITLE_CACHE) + "\n"
    texts = "\n".join(TEXT_CACHE) + "\n"
    with open(TITLE_FILE, "a") as f:
        f.write(titles)
    with open(TEXT_FILE, "a") as f:
        f.write(texts)
    TITLE_CACHE, TEXT_CACHE = [], []


if __name__ == "__main__":
    main()
