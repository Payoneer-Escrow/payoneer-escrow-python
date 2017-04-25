from .base_resource import BaseResource


class Authentications(BaseResource):
    """
    The authentications resource.

    This resource is used to authenticate actions taken by users, such as
    displaying an authenticated light box.
    """

    RESOURCE_NAME = 'authentications'

    def create(self, data):
        """
        Create a new user authentication.

        Args:
            data (dict): The authentication parameters (e.g., uri, action)
        Return:
            The authentication object
        """

        return self._request('POST', self.uri(), data)
