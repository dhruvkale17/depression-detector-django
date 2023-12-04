import os
from dotenv import load_dotenv
import tweepy as tw
import pandas as pd
import nltk, re
from nltk.corpus import stopwords
from textblob import TextBlob

nltk.download('stopwords')
stop = stopwords.words('english')

load_dotenv()
consumer_key = os.getenv('c_key')
consumer_secret= os.getenv('c_secret')
access_token= os.getenv('a_token')
access_token_secret= os.getenv('a_token_secret')

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Post a tweet from Python

def mine(twitter_user):
    # Define the search term and the date_since date as variables
    if twitter_user[0] == "@":
        twitter_user = twitter_user[1:len(twitter_user)]
    search_words = "from:"+twitter_user
    #date_since = "2021-06-01"

    # Collect tweets
    tweets = tw.Cursor(api.search, q=search_words, lang="en").items(10)
    tweetList = [tweet.text for tweet in tweets]
    #print(tweetList)


    #def clean_tweets(tweetList):
    #result = pd.DataFrame(tweetList, columns=['tweet'])

    def remove_url(line):
        return " ".join(re.sub(r"(?:\@|https?\://)\S+", "", line).split())

    clean_list = []

    for t in tweetList:
        clean_list.append(remove_url(t))

    #for t in clean_list:
        #print(testing.test(t))

    return clean_list



