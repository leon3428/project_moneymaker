import GetOldTweets3 as got

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('trump').setSince("2019-05-01").setUntil("2019-06-01").setMaxTweets(10)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

print(tweet.text)
