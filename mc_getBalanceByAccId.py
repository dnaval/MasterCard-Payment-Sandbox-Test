import oauth1.authenticationutils as authenticationutils
from oauth1.oauth import OAuth
from oauth1.oauth_ext import OAuth1RSA
from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

# Get key values
consumer_key = os.getenv('consumer_key')
signing_key = authenticationutils.load_signing_key(os.getenv('signing_key'), os.getenv('pwd_secret'))

# Get Balance by Account ID
uri = os.getenv('base_url')+'/send/partners/'+os.getenv('partner_id')+'/crossborder/accounts/'+os.getenv('account_id')+'?include_balance=true'
oauth = OAuth1RSA(consumer_key, signing_key)
header = {'Content-type' : 'application/json', 'Accept' : 'application/json'}

# Print Response
response = requests.get(uri, auth=oauth, headers=header)
data = response.json()
print(data)
