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

# trxID value here
trx_id = 'rem_JCwU2KNIsqDBJlw6JN0oGF8MWLQ'

# Get transaction details by trxID
uri = os.getenv('base_url')+'/send/v1/partners/'+os.getenv('partner_id')+'/crossborder/'+trx_id
oauth = OAuth1RSA(consumer_key, signing_key)
header = {'Content-type' : 'application/json', 'Accept' : 'application/json'}

# Print response
response = requests.get(uri, auth=oauth, headers=header)
data = response.json()
print(data)
