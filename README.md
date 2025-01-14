# MasterCard-Payment-Sandbox-Test

Python script for test purposes that use mastercard sandbox API for specific task like below with and without encryption/decryption sample:
- Get card rate
- Get Balance
- Get Balance by Account ID
- Get Payment ny Transaction ID
- Post payment

### Description ###

* These scripts will help a developer understand the MC API and a good start with any payment project with MC API.
* Version 1

### Dependencies ###

* Python      (POGRAMMING LANGUAGE)


### Executing program
* Create a developer account via this url: https://developer.mastercard.com/account/log-in/ save all the password and passphrase you entered for each file.
* Make sure you choose "Mastercard Cross-Border Services" and download the keys files.
* Create a folder name "keys" and place the files below in this folder:
    - sandbox-signing.p12
    - client-encryption-key.pem
    - mastercard-encryption-key.p12
* Convert the mastercard encryption key from p12 to pem
    - openssl pkcs12 -in ./keys/mastercard-encryption-key.p12 -nodes | openssl pkcs8 -topk8 -nocrypt -out ./keys/mastercard-encryption-key.pem
* Update .env.example file and then rename it to .env (the variable pwd_secret value is the OAuth keys password before production use a better way to protect this info)
* Run pip install -r requirements.txt

### Authors ###

* Daniel Naval 
[@navald27](https://twitter.com/navald27)
