from .base_resource import BaseResource
from .documents import Documents
from .notes import Notes
from .offers import Offers


class Disputes(BaseResource):
    """
    The disputes resource.
    """

    RESOURCE_NAME = 'disputes'

    def create(self, data):
        """
        Create a new dispute with the supplied data.

        Args:
            data (dict): The dispute creation parameters
        Return:
            The dispute object
        """

        return self._request('POST', self.uri(), data)

    def documents(self, dispute_id):
        """
        Add or access documents on the specified dispute.

        Args:
            dispute_id (int): The dispute_id of the dispute in question
        """

        return Documents(self.host, self.authenticator, self.uri(dispute_id))

    def notes(self, dispute_id):
        """
        Add or access notes on the specified dispute.

        Args:
            dispute_id (int): The dispute_id of the dispute in question
        """

        return Notes(self.host, self.authenticator, self.uri(dispute_id))

    def offers(self, dispute_id):
        """
        Add or access offers on the specified dispute.

        Args:
            dispute_id (int): The dispute_id of the dispute in question
        """

        return Offers(self.host, self.authenticator, self.uri(dispute_id))
