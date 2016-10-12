#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
argfile = str(sys.argv[1])
with open('../../twitter_secrets.txt') as f:
    secrets = f.read().splitlines() 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = secrets[0] #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = secrets[1] #keep the quotes, replace this with your consumer secret key
ACCESS_KEY = secrets[2] #keep the quotes, replace this with your access token
ACCESS_SECRET = secrets[3] #keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes