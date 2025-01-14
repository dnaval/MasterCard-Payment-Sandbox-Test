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

# Encrypted value started with "eyJ"
encrypted_payload = "eyJlbmMiOi......"

# Read the private key
with open(os.getenv('mckey'), 'r') as f:
    private_key = f.read()

# Decrypt the payload
decrypted_payload = jwe.decrypt(encrypted_payload, private_key)

print("\n\nDecrypted Response:\n", decrypted_payload)

     