import FeedParser

class Feed:
    __init__(self, url):
        feed = FeedParser.parse(url)

        title = feed.feed.title
        subtitle = feed.feed.subtitle
        
