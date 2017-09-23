import feedparser
url_input = "car"
d = feedparser.parse("http://www.reddit.com/r/"+url_input+"/.rss")
lis = []
#print len(d['entries'])
for i in range(5):
    res = d['entries'][i]["title"]
    lis.append(res)
print lis
print d['entries'][0]['link']
