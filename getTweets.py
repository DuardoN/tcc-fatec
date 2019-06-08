import requests
import bs4
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1
import csv
import re

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

# Words about negative/positive for query
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

# url according to twitter API
url_rest = "https://api.twitter.com/1.1/search/tweets.json"

# open csv for save tweets
csv_file = open('tweets.csv', 'w')
csv_writer = csv.writer(csv_file)

for word in words:
    # count : no of tweets to be retrieved per one call and parameters according to twitter API
    params = {'q': word['word'], 'count': 100, 'lang': 'pt',  'result_type': 'mixed'}
    print('Query for: '+word['word'])

    results = requests.get(url_rest, params=params, auth=auth)
    tweets = results.json()

    for tweet in tweets['statuses']:
        tweet['text'] = re.sub("\n","",tweet['text'])
        tweet['text'] = re.sub("'",'"',tweet['text'])

        # Patern to use WEKA
        tweet_normalized = "'" + tweet['text'].encode('utf-8') + "', " + str(word['value'])
        # Write on csv
        csv_writer.writerow([tweet_normalized])

print('Download tweets fineshed.')