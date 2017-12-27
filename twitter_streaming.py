# Import package
import tweepy
import json

# Store OAuth authentication credentials in relevant variables
access_token = "942826764967010304-2Vy2mPykwdJXr4ZReCceiKzh0s3m3Me"
access_token_secret = "fU5USywwdEPFPX9nvJrbm31EBjsjunFrQvgiyzr4KxQMs"
consumer_key = "H9c7wnPsjvrFRSjIoHVcrToJb"
consumer_secret = "uLm2ye9FIHl0VFfvrj58xLUA88s3zdFcaMuVgYha0uNzSDjDVU"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # Initialize Stream listener
    l = MyStreamListener()

    # Create you Stream object with authentication
    stream = tweepy.Stream(auth, l)

    # Filter Twitter Streams to capture data by the keywords:
    stream.filter(track = ['clinton', 'trump', 'sanders', 'cruz'])


# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()