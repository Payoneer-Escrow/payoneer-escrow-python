from .bank_accounts import BankAccounts
from .base_resource import BaseResource
from .orders import Orders
from .users import Users


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
        Update the specified account with the supplied (full) data.

        Args:
            account_id (int): The account_id of the account in question
            data (dict): The full account parameters
        Return:
            The account object
        """

        return self._request('POST', self.uri(account_id), data)

    def bank_accounts(self, account_id):
        """
        Access bank accounts on the specified account.
        """

        return BankAccounts(self.host, self.authenticator, self.uri(account_id))

    def orders(self, account_id):
        """
        Add or access orders on the specified account.
        """

        return Orders(self.host, self.authenticator, self.uri(account_id))

    def users(self, account_id):
        """
        Add or access users on the specified account.
        """

        return Users(self.host, self.authenticator, self.uri(account_id))
