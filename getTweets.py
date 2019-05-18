import requests
import bs4
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1

auth_params = {
    'app_key':'API Key',
    'app_secret':'API secret',
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

# url according to twitter API
url_rest = "https://api.twitter.com/1.1/search/tweets.json"

# getting rid of retweets in the extraction results and filtering all replies to the tweet often uncessary for the analysis
q = '%40amazonIN -filter:retweets -filter:replies' # Twitter handle of Amazon India

# count : no of tweets to be retrieved per one call and parameters according to twitter API
params = {'q': q, 'count': 2000, 'lang': 'en',  'result_type': 'recent'}
results = requests.get(url_rest, params=params, auth=auth)

tweets = results.json()

messages = [BeautifulSoup(tweet['text'], 'html5lib').get_text() for tweet in tweets['statuses']]
print(messages)