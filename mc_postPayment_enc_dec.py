import oauth1.authenticationutils as authenticationutils
from oauth1.oauth import OAuth
from oauth1.oauth_ext import OAuth1RSA
from dotenv import load_dotenv
import requests
import json
import os
from jose import jwe, exceptions
from jose.constants import ALGORITHMS

load_dotenv()

# Get key values
consumer_key = os.getenv('consumer_key')
signing_key = authenticationutils.load_signing_key(os.getenv('signing_key'), os.getenv('pwd_secret'))

# Post encrypted payment payload
uri = os.getenv('base_url')+'/send/v1/partners/'+os.getenv('partner_id')+'/crossborder/payment'
oauth = OAuth1RSA(consumer_key, signing_key)
header = {'Content-type' : 'application/json', 'Accept' : 'application/json', 'x-encrypted': 'TRUE'}

payload = {
    "paymentrequest": {
        "transaction_reference": "PTO2024092465486012-n2gns01",
        "payment_type": "P2P",
        "payment_amount": {
            "amount": "10.0",
            "currency": "USD"
        },
        "additional_data": {
            "data_field": [
                {
                    "name": "630",
                    "value": "P"
                },
                {
                    "name": "701",
                    "value": "USA"
                }
            ]
        },
        "fx_type": {
            "reverse": {
                "sender_currency": "USD"
            }
        },
        "sender": {
            "first_name": "JEAN JACQUES",
            "last_name": "DESSALINE",
            "address": {
                "line1": "1804 WEST BAY ST.",
                "city": "Nassau",
                "country": "BHS"
            }
        },
        "recipient": {
            "first_name": "Henry",
            "last_name": "Christophe",
            "address": {
                "line1": "1806 Old Fort St",
                "city": "Nassau",
                "postal_code": "00000",
                "country_subdivision": "NP",
                "country": "BHS"
            }
        },
        "bank_code": "182-512",
        "payment_origination_country": "USA",
        "sender_account_uri": "ban:7456298452;bic=123103729",
        "recipient_account_uri": "ban:011623852;bic=INYTAU31"
    }
}

# Read the public key
with open(os.getenv('clientkey'), 'r') as f:
    public_key = f.read()

# Convert Payload to JSON
payload_json = json.dumps(payload) 

# Encrypt the payload
encrypted_payload = jwe.encrypt(payload_json, public_key, algorithm=ALGORITHMS.RSA_OAEP_256, encryption=ALGORITHMS.A256GCM)

encrypted_payload_json = {
    "encrypted_payload": {
        "data": encrypted_payload.decode('utf8')
    }
}


# Print Encrypted data
print("Encrypted Payload:\n", encrypted_payload_json)

response = requests.post(uri, json=encrypted_payload_json, auth=oauth, headers=header)

# Print Response
data = response.json()

# Decrypt the payload
encrypted_response = data['encrypted_payload']['data']

# Read the private key
with open(os.getenv('mckey'), 'r') as f:
    private_key = f.read()

decrypted_payload = jwe.decrypt(encrypted_response, private_key)

print("\n\nDecrypted Response:\n", decrypted_payload)
     