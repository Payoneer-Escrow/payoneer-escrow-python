import requests


class BaseResource:
    """
    The base resource class for accessing the Payoneer Escrow API.
    """

    # The name this resource uses in the uri
    RESOURCE_NAME = ''

    def __init__(self, host, authenticator, uri_root):
        """
        Initialize the resource.

        Args:
            host (string): The base_url specific to the environment used by the
                Client
            authenticator (Authenticator): Object that generates secure headers
                for requests
            uri_root (string): The uri_root for this resource; may have been
                built from resources lower in the chain
        """

        self.host = host
        self.authenticator = authenticator
        self.uri_root = uri_root

    def all(self):
        """
        Get all objects matching this resource.
        """

        return self._request('GET', self.uri())

    def get(self, object_id):
        """
        Get a single object with the specified ID.
        """

        return self._request('GET', self.uri(object_id))

    def uri(self, object_id=None):
        """
        Build up the uri from the uri_root and the resource name.

        Args:
            object_id (string): The ID of a specific object on this resource
        Return:
            (string) The full URI
        """

        uri = "{}/{}".format(self.uri_root, self.RESOURCE_NAME)
        if object_id:
            uri += "/{}".format(object_id)
        return uri

    def _request(self, method, uri, params=dict()):
        """
        Execute the specified request.

        Args:
            method (string): The HTTP request method ('POST', 'GET', etc.)
            uri (string): The request URI
            params (dict): Any parameters to include in the query string
        Return:
            A dict or object, decoded from the API JSON response.
        """

        full_url = self.host + uri
        auth_headers = self.authenticator.secure_headers(method, uri)
        method = method.upper()
        if method == 'GET':
            r = requests.get(full_url, json=params, headers=auth_headers)
        elif method == 'POST':
            r = requests.post(full_url, json=params, headers=auth_headers)

        # If there was a 4xx or 5xx error, raise an HTTPError
        r.raise_for_status()

        try:
            # If we received a json-encoded response, decode it
            r_decoded = r.json()
        except ValueError:
            # Otherwise, just return the text
            r_decoded = r.text

        return r_decoded
