import tweepy
from textblob import TextBlob
import time
import pandas
# Step 1 - Authenticate
consumer_key= 's1DFkc4aNhJkKHmq78Y5uJfoy'
consumer_secret= 'GUCpIriPOQjAoQNEOZBSgBDcvRzGtncUnJ8v2HGES43nbPPFiK'

access_token='3149460439-bny9L7ixHkDh1ma6AyVVw7UCj2RX6u569o3k8wY'
access_token_secret='ujavZkQjKFkwbb1qgC5unQIYU4MUQqoRwBc70Jte2Ljt7'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('homepod')


open("twetr1.txt","w").close() # this will delete everything in previous tweet1file and start fresh




for tweet in public_tweets:
    print (tweet.text.encode('utf-8'))
    texty = tweet.text.encode('utf-8')
    texty = str(texty)


    saveFile = open ("twetr1.txt","a")
    saveFile.write(texty)
    saveFile.write('\n')
    saveFile.write('\n')
    saveFile.close
    
   
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")


