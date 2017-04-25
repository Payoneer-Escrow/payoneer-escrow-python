from __future__ import absolute_import
from .authenticator import Authenticator
from .api.accounts import Accounts


class Client:

    def __init__(self, api_key, api_secret, sandbox=False):
        """
        Initialize an API client.

        Args:
            api_key (string): Your API key
            api_secret (string): Your API secret
            sandbox (bool): Use the testing Sandbox environment (rather than
                Production)?
        """

        self.authenticator = Authenticator(api_key, api_secret)
        self.sandbox = sandbox

    def accounts(self):
        """
        Access to the accounts associated with your API key.
        """

        return Accounts(self._base_url(), self.authenticator, '')

    def _base_url(self):
        """
        Return the proper base url depending on the environment.
        """

        if self.sandbox:
            subdomain = 'sandbox'
        else:
            subdomain = 'app'
        return 'https://' + subdomain + '.armorpayments.com'
