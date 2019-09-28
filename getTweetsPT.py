import requests
import bs4
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1
import csv
import re
import nltk
import collections
import nltk
nltk.download('punkt')
from nltk.tokenize import TweetTokenizer
import os

auth_params = {
    'app_key':'XXXXXXXXXXXXXXXXXXXXXXXX',
    'app_secret':'XXXXXXXXXXXXXXXXXXXXXXXX',
    'oauth_token':'XXXXXXXXXXXXXXXXXXXXXXXX',
    'oauth_token_secret':'XXXXXXXXXXXXXXXXXXXXXXXX'
}

# Creating an OAuth Client connection
auth = OAuth1 (
    auth_params['app_key'],
    auth_params['app_secret'],
    auth_params['oauth_token'],
    auth_params['oauth_token_secret']
)

# Words about negative/positive for query. You can change
words = [
    {'word': 'bad', 'value': 0},
    {'word': 'triste', 'value': 0},
    {'word': 'tristeza', 'value': 0},
    {'word': 'repudio', 'value': 0},
    {'word': ':(', 'value': 0},
    {'word': 'sad', 'value': 0},
    {'word': 'caralho', 'value': 0},
    {'word': 'caralho', 'value': 1},
    {'word': 'decepcionado', 'value': 0},
    {'word': 'decepcionada', 'value': 0},
    {'word': 'insatisfeito', 'value': 0},
    {'word': 'cansada', 'value': 0},
    {'word': 'exausta', 'value': 0},
    {'word': 'cansado', 'value': 0},
    {'word': 'exausto', 'value': 0},
    {'word': 'feliz', 'value': 1},
    {'word': 'alegre', 'value': 1},
    {'word': 'sorrindo', 'value': 1},
    {'word': 'apaixonado', 'value': 1},
    {'word': 'apaixonada', 'value': 1},
    {'word': ':)', 'value': 1},
    {'word': 'felicidade', 'value': 1},
    {'word': 'top', 'value': 1},
    {'word': 'topzera', 'value': 1}
]

# You can change language
lang = 'pt'

# Create folder for save data
try:
    os.mkdir(lang)
except OSError:
    print ("Creation of the directory %s failed" % lang)
else:
    print ("Successfully created the directory %s " % lang)

# url according to twitter API
url_rest = "https://api.twitter.com/1.1/search/tweets.json"

# open csv for save tweets
csv_file = open(lang + '/tweets.csv', 'w')
csv_writer = csv.writer(csv_file)

# Word counts for use on weka
def word_counts(text, words):
    textTok = nltk.word_tokenize(text)
    counts = nltk.FreqDist(textTok) # This counts all word occurences
    return [counts[x] or 0 for x in words] # This returns what was counted for *words

for word in words:
    # count : no of tweets to be retrieved per one call and parameters according to twitter API
    print('Query for: %s' % word['word'])

    params_mixed = {'q': word['word'], 'exclude': 'retweets', 'count': 100, 'lang': lang,  'result_type': 'mixed'}
    params_recent = {'q': word['word'], 'exclude': 'retweets', 'count': 100, 'lang': lang,  'result_type': 'recent'}
    params_popular = {'q': word['word'], 'exclude': 'retweets', 'count': 100, 'lang': lang,  'result_type': 'popular'}

    results_mixed = requests.get(url_rest, params=params_mixed, auth=auth)
    results_recent = requests.get(url_rest, params=params_recent, auth=auth)
    results_popular = requests.get(url_rest, params=params_popular, auth=auth)
    
    tweets_mixed = results_mixed.json()
    tweets_recent = results_recent.json()
    tweets_popular = results_popular.json()

    for tweet in tweets_mixed['statuses']:
        if tweet['in_reply_to_status_id'] == None:
            tweet['text'] = re.sub("\n","",tweet['text'])
            tweet['text'] = re.sub("'",'"',tweet['text'])
            
            # Pattern words.  You can change
            words_counted = word_counts(
                tweet['text'],
                [
                    'bad',
                    'triste',
                    'solitário',
                    'depressivo',
                    'tristeza',
                    'repudio',
                    ':(',
                    'sad',
                    'caralho',
                    'caralho',
                    'decepcionado',
                    'decepcionada',
                    'insatisfeito',
                    'cansada',
                    'exausta',
                    'cansado',
                    'exausto',
                    'feliz',
                    'alegre',
                    'sorrindo',
                    'apaixonado',
                    'apaixonada',
                    ':)',
                    'felicidade',
                    'top',
                    'topzera'
                ]
            )
            list_to_string = ' ,'.join(str(e) for e in words_counted)
            tweet_normalized = list_to_string + ", " + str(word['value'])
            # Write on csv
            csv_writer.writerow([tweet_normalized])
    
    for tweet in tweets_recent['statuses']:
        if tweet['in_reply_to_status_id'] == None:
            tweet['text'] = re.sub("\n","",tweet['text'])
            tweet['text'] = re.sub("'",'"',tweet['text'])
            
            # Pattern words.  You can change
            words_counted = word_counts(
                tweet['text'],
                [
                    'bad',
                    'triste',
                    'solitário',
                    'depressivo',
                    'tristeza',
                    'repudio',
                    ':(',
                    'sad',
                    'caralho',
                    'caralho',
                    'decepcionado',
                    'decepcionada',
                    'insatisfeito',
                    'cansada',
                    'exausta',
                    'cansado',
                    'exausto',
                    'feliz',
                    'alegre',
                    'sorrindo',
                    'apaixonado',
                    'apaixonada',
                    ':)',
                    'felicidade',
                    'top',
                    'topzera'
                ]
            )
            list_to_string = ' ,'.join(str(e) for e in words_counted)
            tweet_normalized = list_to_string + ", " + str(word['value'])
            # Write on csv
            csv_writer.writerow([tweet_normalized])

    for tweet in tweets_popular['statuses']:
        if tweet['in_reply_to_status_id'] == None:
            tweet['text'] = re.sub("\n","",tweet['text'])
            tweet['text'] = re.sub("'",'"',tweet['text'])
            
            # Pattern words.  You can change
            words_counted = word_counts(
                tweet['text'],
                [
                    'bad',
                    'triste',
                    'solitário',
                    'depressivo',
                    'tristeza',
                    'repudio',
                    ':(',
                    'sad',
                    'caralho',
                    'caralho',
                    'decepcionado',
                    'decepcionada',
                    'insatisfeito',
                    'cansada',
                    'exausta',
                    'cansado',
                    'exausto',
                    'feliz',
                    'alegre',
                    'sorrindo',
                    'apaixonado',
                    'apaixonada',
                    ':)',
                    'felicidade',
                    'top',
                    'topzera'
                ]
            )
            list_to_string = ' ,'.join(str(e) for e in words_counted)
            tweet_normalized = list_to_string + ", " + str(word['value'])
            # Write on csv
            csv_writer.writerow([tweet_normalized])

print('Download tweets fineshed.')