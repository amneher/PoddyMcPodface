#!/usr/bin/env Python3

import requests
import feedparser

url = 'http://www.hackerpublicradio.org/hpr_ogg_rss.php'

feed = feedparser.parse(url)

print(feed.feed.title)
print(feed.entries[1].title)

f = feed.entries[1].id
r = requests.get(f)

with open('hprepisode.ogg', 'wb') as ogg:
	ogg.write(r.content)
