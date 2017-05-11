from __future__ import (absolute_import, print_function)
from payoneer_escrow_sdk.client import Client
from json import dumps
from requests.exceptions import HTTPError
# To run this example, you will need a working Sandbox API key, stored in a file
# called `api_credentials.py`. It should have your credentials in the following
# format:
#
# PAYONEER_ESCROW_API_KEY = "ENTER_YOUR_API_KEY_HERE"
# PAYONEER_ESCROW_SECRET = "ENTER_YOUR_API_SECRET_HERE"
#
from api_credentials import (
    PAYONEER_ESCROW_API_KEY as pe_api_key,
    PAYONEER_ESCROW_SECRET as pe_secret)


# Instantiate the client that we will use throughout
should_use_sandbox = True
client = Client(pe_api_key, pe_secret, should_use_sandbox)


def pretty_print(json_string):
    """Allow command line output to look nice"""
    print(dumps(json_string, sort_keys=True, indent=4, separators=(',', ': ')), "\n")


# Print which API key is being used
pe_key_name = 'Sandbox' if should_use_sandbox else 'Production'
pe_key_name = "API Key: {}".format(pe_key_name)
print("\n" + pe_key_name + "\n" + ('-' * len(pe_key_name)) + "\n")


# Get a set of accounts. On a fresh install, this will include only your own
# account.
accounts = client.accounts().all()


# Get the account_id of the first account returned
account = accounts[0]
account_id = account['account_id']


# It's also possible to get a single account using its account_id
account = client.accounts().get(account_id)
# Print out the information returned for the account
pretty_print(account)


# Get a list of users on the account. For a fresh install, this will be only the
# user who registered the API key
users = client.accounts().users(account_id).all()


# Get the user_id of the first user returned
user = users[0]
user_id = user['user_id']


# It's also possible to get a single user using its account_id and user_id
user = client.accounts().users(account_id).get(user_id)
# Print out the information returned for the account
pretty_print(user)


# This example file demonstrates calls against several API resources and will
# allow you to determine that your PAYONEER_ESCROW_API_KEY and
# PAYONEER_ESCROW_SECRET values are correct. The calls in this example have been
# carefully selected to ensure that they are safe and repeatable.
#
# Once you have this working, check the /examples directory for an example for
# the specific order type you intend to use.


# A note about raising HTTPError on 400+ status codes
#
# If the status code of the response is >= 400, it will raise an HTTPError. You
# will want to wrap your calls in a try/catch block to properly handle these.
# The Payoneer Escrow API returns detailed error messages, so if you have a call
# that is failing, these can provide insight.
try:
    client.accounts().get('test_catching_an_error')
except HTTPError as e:
    # We are printing here, but you will probably need to do some special
    # handling
    print("Status code: {}, Reason: {}".format(
        e.response.status_code, e.response.reason))
    pretty_print(e.response.json())
