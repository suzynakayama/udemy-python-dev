import tweepy
import os
import time
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

# print(user.name)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# helper function
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)        # it will stay and wait in this line for 1000 ms
    except StopIteration:
        return


# Generous Bot - follows ppl back
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     print(follower.name)
#     if follower.name == "Vinicius Campos":
#         follower.follow()
#         break


# Narcissist Bot
search_str = 'Suzy Nakayama'
number_of_tweets = 2

for tweet in limit_handler(tweepy.Cursor(api.search, search_str).items(number_of_tweets)):
    try:
        tweet.favorite()
        # tweet.retweet()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

