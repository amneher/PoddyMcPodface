import feedparser
import sys, os
import pickle

feed_file = open('feeds.txt', 'a+')
feeds = []

# main
def poddy():
    load_feeds()
    while True:
        show_menu()

# get feed info
def show_feeds():
    print('-' * 20)
    if feeds:
        for f in feeds:
            feed = feedparser.parse(f)
            print(feed.feed.title)
    print('-' * 20)
# refresh feeds

# load feeds
def load_feeds():
    for line in feed_file:
        feeds.append(line)

# add feed
def add():
    feed = str(input('Enter feed URL: '))
    if feed not in feeds:
        feeds.append(feed)
    if feed + ' \n' not in feed_file:
        feed_file.write(feed + ' \n')
    # print(feeds)

# download episodes

# show new episodes
def show_new_episodes():
    for feed in feeds:
        f = feedparser.parse(feed)
        print(' ')
        print(f.feed.title)
        print(' ')
        for i in range(0,10):
            print(f.entries[i].title)
# delete old episodes

# show downloaded episodes

# save place in feed

# show menu
def show_menu():
    # os.system('clear')
    print('=' * 20)
    print('Welcome to Poddy McPodface!')
    print('=' * 20)
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
        feed_file.close()
        quit()


if __name__=="__main__":
    poddy()
