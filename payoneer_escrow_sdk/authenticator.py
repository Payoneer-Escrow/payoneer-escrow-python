from __future__ import absolute_import
from datetime import datetime
from hashlib import sha512


class Authenticator:
    """
    Functionality used to authenticate all requests made to Payoneer Escrow.
    """

    def __init__(self, api_key, api_secret):
        """
        Initialize an Authenticator.

        Args:
            api_key (string): Your API key
            api_secret (string): Your API secret
        """

        self.api_key = api_key
        self.api_secret = api_secret

    def secure_headers(self, method, uri):
        """
        Generate secure request authentication headers for Payoneer Escrow.

        Payoneer Escrow used to be called Armor Payments, and the headers still
        have that vestage.

        Args:
            method (string): The HTTP request method ('POST', 'GET', etc.)
            uri (string): The request URI
        """

        timestamp = self._current_timestamp()
        return dict({
            'x-armorpayments-apikey': self.api_key,
            'x-armorpayments-requesttimestamp': timestamp,
            'x-armorpayments-signature': self._request_signature(
                method, uri, timestamp),
            })

    def _current_timestamp(self):
        """
        Return a timestamp in the ISO 8601 format of 'YYYY-MM-DDTHH:MM:SS-HH:MM'
        """

        current_time = datetime.utcnow().replace(microsecond=0).isoformat()
        if len(current_time) == 19:
            current_time += '-00:00'
        return current_time

    def _request_signature(self, method, uri, timestamp):
        """
        Generate the unique request signature.

        Args:
            method (string): The HTTP request method ('POST', 'GET', etc.)
            uri (string): The request URI
            timestamp (string): The current time in ISO 8601 format
        """

        method = method.upper()
        # For the authentication process, trim any params off of the URI
        uri = uri.split('?')[0]
        # Build the plain-text signature
        signature = "{}:{}:{}:{}".format(self.api_secret, method, uri, timestamp)
        # Return the sha512 hash represented with only hexidecimal digits
        return sha512(signature.encode('utf-8')).hexdigest()
