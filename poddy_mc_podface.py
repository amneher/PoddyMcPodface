import feedparser
import sys, os
import pickle


feeds = []

# main
def poddy():
    while True:
        show_menu()

# get feed info
def show_feeds():
    if feeds:
        for f in feeds:
            feed = feedparser.parse(f)
            print(feed.feed.title)
# refresh feeds

# add feed
def add():
    feed = str(input('Enter feed URL: '))
    feeds.append(feed)
    print(feeds)

# download episodes

# show new episodes
def show_new_episodes():
    for feed in feeds:
        f = feedparser.parse(feed)
        for i in range(0,10):
            print(f.entries[i].title)
# delete old episodes

# show downloaded episodes

# save place in feed

# show menu
def show_menu():
    print('Welcome to Poddy McPodface!')
    print('---------------------------')
    print('1. Add feed')
    print('2. Show feeds')
    print('3. Show new episodes')
    print('Press Q to quit')

    choice = input('Enter number of your choice: ')

    if choice == '1':
        add()
    elif choice == '2':
        show_feeds()
    elif choice == '3':
        show_new_episodes()
    elif choice.lower() == 'q':
        print("See Ya!")
        quit()


if __name__=="__main__":
    poddy()
