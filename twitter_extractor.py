import pandas as pd
from tqdm import tqdm
from textblob import TextBlob
from datetime import date, timedelta
import GetOldTweets3 as got
from time import time

MAX_TWEETS = 1000
MPERSES = 50

session_start = int(input('Session start: '))
save_name = 'saves/sentiment' + str(session_start)+'.txt'

df = pd.read_csv('dataset.csv')
f = open('clubs.txt', 'r')
out_f = open(save_name, 'w')
out_f.write('')
out_f.close()

names = f.read()
f.close()
names = names.split('\n')
names.pop()

delta1 = timedelta(days = 1)
delta2 = timedelta(days = 7)

for index, row in tqdm(df.iterrows()):
    if index < session_start:
        continue
    if index == session_start+MPERSES:
        break

    od = row.DATE
    od = od.split()[0]
    d = date.fromisoformat(od)

    home = ""
    away = ""
    for club in names:
        club = club.split()
        try:
            a = int(club[1])
        except:
            club = [club[0] + ' ' + club[1], club[2], club[3]]
        #print(club)
        if row.HOME == club[0]:
            home = club[2]
        if row.AWAY == club[0]:
            away = club[2]
    start_date = d - delta2
    end_date = d - delta1
    start_date = start_date.isoformat()
    end_date = end_date.isoformat()

    #print(home, away, start_date, end_date)
    home_sub = []
    away_sub = []
    home_pol = []
    away_pol = []

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(home).setSince(start_date).setUntil(end_date).setMaxTweets(MAX_TWEETS)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    for tweet in tweets:
        analysis = TextBlob(tweet.text)
        home_sub.append(int(analysis.sentiment.subjectivity*1000))
        home_pol.append(int(analysis.sentiment.polarity*1000))


    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(away).setSince(start_date).setUntil(end_date).setMaxTweets(MAX_TWEETS)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    for tweet in tweets:
        analysis = TextBlob(tweet.text)
        away_sub.append(int(analysis.sentiment.subjectivity*1000))
        away_pol.append(int(analysis.sentiment.polarity*1000))

    home_sub = ' '.join(map(str, home_sub))
    home_pol = ' '.join(map(str, home_pol))
    away_sub = ' '.join(map(str, away_sub))
    away_pol = ' '.join(map(str, away_pol))

    out_f = open(save_name, 'a')
    out_f.write(home + ' ' + od + '\n' + home_pol + '\n' + home_sub + '\n')
    out_f.write(away + ' ' + od + '\n' + away_pol + '\n' + away_sub + '\n')
    out_f.close()
