from .base_resource import BaseResource


class Accounts(BaseResource):
    """
    The accounts resource.
    """

    RESOURCE_NAME = 'accounts'

    def create(self, data):
        """
        Create a new account with the supplied data.

        Args:
            data (dict): The account creation parameters
        Return:
            The account object
        """

        return self._request('POST', self.uri(), data)

    def update(self, account_id, data):
        """
        Update the specified account with the supplied data.

        Args:
            account_id (int): The account_id of the account in question
            data (dict): The account parameters to change
        Return:
            The account object
        """

        return self._request('POST', self.uri(account_id), data)
