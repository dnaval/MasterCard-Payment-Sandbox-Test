import oauth1.authenticationutils as authenticationutils
from oauth1.oauth import OAuth
from oauth1.oauth_ext import OAuth1RSA
from dotenv import load_dotenv
import requests
import json
import os
from jose import jwe
from jose.constants import ALGORITHMS

load_dotenv()

consumer_key = os.getenv('consumer_key')
signing_key = authenticationutils.load_signing_key(os.getenv('signing_key'), os.getenv('pwd_secret'))

uri = os.getenv('base_url')+'/send/partners/'+os.getenv('partner_id')+'/crossborder/accounts?include_balance=true'
oauth = OAuth1RSA(consumer_key, signing_key)
header = {'Content-type' : 'application/json', 'Accept' : 'application/json'}

# Operation for get call
response = requests.get(uri, auth=oauth, headers=header)
data = response.json()

print("Encrypted response:\n",json.dumps(data))
encrypted_payload = data['encrypted_payload']['data']

# Read the private key
with open(os.getenv('mckey'), 'r') as f:
    private_key = f.read()

# Decrypt the payload
decrypted_payload = jwe.decrypt(encrypted_payload, private_key)

print("\n\nDecrypted response:\n", decrypted_payload.decode('utf8'))
