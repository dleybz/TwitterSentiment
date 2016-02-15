from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

#Creates file named "output.json" to store tweets+metadata 
sys.stdout = open('output.json', 'w')

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status
  

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API 
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
	
#Twitter API requires you to filter ( https://dev.twitter.com/streaming/reference/post/statuses/filter ), I used solution proposed here http://stackoverflow.com/questions/27530269/how-can-i-use-tweepy-without-a-filter , another solution is proposed here http://stackoverflow.com/questions/26890605/filter-twitter-feeds-only-by-language
stream = Stream(auth, l).filter(locations=[-180,-90,180,90])