from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
access_token = "1548210780-933yQdEdgqShZ9qPStW5zLmAflvX5paIjRUZ6FO"
access_token_secret = "oguhW1YQoezEBYNtS4I9cjuRJaAtm1gCZy67fCv0lI7DZ"
consumer_key= "8qFRWYebcsoYQVehW4LJnk31S"
consumer_secret	=  "JB5Zw5k2zfZiv2a2sn2U1x7H44LxnqtOAJCpl4TS4l4fdypOv3"
class listener(StreamListener):		
   def on_data(self, data):
       try:
           saveFile = open('tweets.json','a')
           saveFile.write(data)
           saveFile.write(',  \n')
           saveFile.close()
           return True
       except Except:
           print ("failed ondata")
           time.sleep(1)
           
	
   def on_error(self, status):
        print(status)	
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["kansascitydeals,christmasdeals,dealskc2015,kansascity,kansascity2015,deals,newyeardeals,blackfriday2015,blackfridaydeals2015,targetdeals,kholsdeals,blackfridaydeals,targetdeals2015,kholsdeals2015,macysdeals2015,expressdeals2015,nikedeals2015,addidasdeals2015,gapdeals2015,laptopdeals2015,iphonedeals2015,clothesdeals2015,offers,shoesdeals2015,off,kansascity"])
