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
            host (string): The base_url for our current environment
            authenticator (Authenticator): Object that generates secure headers
                for requests
            uri_root (string): The uri_root for this resource; may have been
                built from resources lower in the chain
        """

        self.host = host
        self.authenticator = authenticator
        self.uri_root = uri_root

    def uri(self, object_id=None):
        """
        Build up the uri from the uri_root and the resource name.

        Args:
            object_id (string): The ID of a specific object on this resource
        Return:
            (string) The full uri
        """

        uri = "{}/{}".format(self.uri_root, self.RESOURCE_NAME)
        if object_id:
            uri += "/{}".format(object_id)
        return uri
