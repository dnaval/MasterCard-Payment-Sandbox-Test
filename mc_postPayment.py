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

# Post payment payload
uri = os.getenv('base_url')+'/send/v1/partners/'+os.getenv('partner_id')+'/crossborder/payment'
oauth = OAuth1RSA(consumer_key, signing_key)
header = {'Content-type' : 'application/json', 'Accept' : 'application/json'}

payload = {
            "paymentrequest": {
                "transaction_reference": "ddan-f5f18b386d29b272",
                "payment_type": "P2P",
                "payment_amount": {
                    "amount": "10",
                    "currency": "USD"
                },
                "additional_data": {
                    "data_field": [
                        {
                            "name": "701",
                            "value": "AUS"
                        }
                    ]
                },
                "sender": {
                    "first_name": "George",
                    "last_name": "Washington",
                    "address": {
                        "line1": "Sapodilla Bld Pinewood Gdns",
                        "country": "BHS"
                    }
                },
                "recipient": {
                    "first_name": "Paul",
                    "last_name": "Hogan",
                    "address": {
                        "line1": "57 Cunningham Street",
                        "city": "Wallumbilla",
                        "postal_code": 4428,
                        "country": "AUS"
                    }
                },
                "bank_code": "182-512",
                "payment_origination_country": "USA",
                "sender_account_uri": "ban:7456298452;bic=123103729",
                "recipient_account_uri": "ban:011623852;bic=INYTAU31"
            }
        }

response = requests.post(uri, json=payload, auth=oauth, headers=header)

# Print response
data = response.json()
print(data)

