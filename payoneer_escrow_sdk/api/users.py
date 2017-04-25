from .base_resource import BaseResource


class Users(BaseResource):
    """
    The users resource.
    """

    RESOURCE_NAME = 'users'

    def create(self, data):
        """
        Create a new user with the supplied data.

        Args:
            data (dict): The user creation parameters
        Return:
            The user object
        """

        return self._request('POST', self.uri(), data)

    def update(self, user_id, data):
        """
        Update the specified user with the supplied (full) data.

        Args:
            user_id (int): The user_id of the user in question
            data (dict): The full user parameters
        Return:
            The user object
        """

        return self._request('POST', self.uri(user_id), data)
