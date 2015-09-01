#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, time, sys
import random
import io
import os
from datetime import datetime  
from sys import argv

i = datetime.now()  
argfile = str(sys.argv[1])
 
CONSUMER_KEY = 'insertkeyhere'
CONSUMER_SECRET = 'insertsecrethere'
ACCESS_KEY = 'insertkeyhere'
ACCESS_SECRET = 'insertsecrethere'
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api=tweepy.API(auth)

##output to same file
output = ""
##open tweets and add seconds to it
tweet_file = "tweets.txt"
##remove last 2 characters
with open(tweet_file, 'r') as f:
	remove2 = [''.join([x.strip()[:-2], '\n']) for x in f.readlines()]
with open(tweet_file, 'w') as f:
    f.writelines(remove2) 

## find the system's seconds
seconds = i.strftime('%S') 
##add last 2 characters to avoid twitter duplicate message
with open(tweet_file, 'r') as f:
    add2 = [''.join([x.strip(), seconds, '\n']) for x in f.readlines()]
with open(tweet_file, 'w') as f:
	f.writelines(add2) 


##open tweets, shuffle then close
filename=open(argfile,'r')
f=filename.readlines()

random.shuffle(f)
filename.close()

for line in f:
	##post
	api.update_status(status=line)
	time.sleep(2100)#Tweet every 35 minutes


