import requests
import bs4
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1
import csv

auth_params = {
    'app_key':'API key',
    'app_secret':'API secret key',
    'oauth_token':'Access token',
    'oauth_token_secret':'Access token secret'
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
    'bad',
    'triste',
    'tristeza',
    'repudio',
    ':(',
    'sad',
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
    'apaixonada',
    'apaixonado',
    'paz',
    ':)',
    'felicidade',
    'top',
    'topzera',
]

# url according to twitter API
url_rest = "https://api.twitter.com/1.1/search/tweets.json"

for word in words:
    # count : no of tweets to be retrieved per one call and parameters according to twitter API
    params = {'q': word, 'count': 100, 'lang': 'pt',  'result_type': 'mixed'}
    results = requests.get(url_rest, params=params, auth=auth)
    tweets = results.json()

    # open csv for save tweets
    csvFile = open('tweets-'+word+'.csv', 'w')
    csvWriter = csv.writer(csvFile)

    for tweet in tweets['statuses']:
        # Write on csv
        csvWriter.writerow([tweet['text'].encode('utf-8')])

print('Download tweets fineshed.')