import os
from requests_oauthlib import OAuth1Session
from urllib.parse import urlparse, parse_qsl
from dotenv import load_dotenv

url_usos = 'https://apps.usos.pwr.edu.pl/services/'

load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')

url_request_token = url_usos + 'oauth/request_token?scopes=studies|offline_access'
url_authorize = url_usos + 'oauth/authorize'
url_access_token = url_usos + 'oauth/access_token'

def request_for_link():
    usos_request = OAuth1Session(CONSUMER_KEY, client_secret = CONSUMER_SECRET, callback_uri = "oob")
    response = usos_request.fetch_request_token(url_request_token)
    
    oauth_token = response.get('oauth_token')
    oauth_token_secret = response.get('oauth_token_secret')
    
    usos_request = OAuth1Session(CONSUMER_KEY, client_secret = CONSUMER_SECRET, resource_owner_key = oauth_token, resource_owner_secret = oauth_token_secret)

    return usos_request.authorization_url(url_authorize), oauth_token, oauth_token_secret


def authenticate(verifier, oauth_token, oauth_token_secret):
    usos_request = OAuth1Session(CONSUMER_KEY, client_secret = CONSUMER_SECRET, resource_owner_key = oauth_token, resource_owner_secret = oauth_token_secret, verifier = verifier)
    
    tokens = usos_request.fetch_access_token(url_access_token)
    resource_owner_key = tokens.get('oauth_token')
    resource_owner_secret = tokens.get('oauth_token_secret')
    
    return resource_owner_key, resource_owner_secret

def fetch_data(resource_owner_key, resource_owner_secret, user_arguments):
    usos_request = OAuth1Session(CONSUMER_KEY, client_secret = CONSUMER_SECRET, resource_owner_key = resource_owner_key, resource_owner_secret = resource_owner_secret)
    
    return usos_request.get(url_usos+user_arguments).json()