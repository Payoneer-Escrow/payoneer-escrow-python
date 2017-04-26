from .base_resource import BaseResource
from .documents import Documents
from .notes import Notes


class Offers(BaseResource):
    """
    The offers resource.
    """

    RESOURCE_NAME = 'offers'

    def create(self, data):
        """
        Create a new offer with the supplied data.

        Args:
            data (dict): The offer creation parameters
        Return:
            The offer object
        """

        return self._request('POST', self.uri(), data)

    def update(self, offer_id, data):
        """
        Update the specified offer with the supplied (full) data.

        Args:
            offer_id (int): The offer_id of the offer in question
            data (dict): The full offer parameters
        Return:
            The offer object
        """

        return self._request('POST', self.uri(offer_id), data)

    def documents(self, offer_id):
        """
        Add or access documents on the specified offer.

        Args:
            offer_id (int): The offer_id of the offer in question
        """

        return Documents(self.host, self.authenticator, self.uri(offer_id))

    def notes(self, offer_id):
        """
        Add or access notes on the specified offer.

        Args:
            offer_id (int): The offer_id of the offer in question
        """

        return Notes(self.host, self.authenticator, self.uri(offer_id))
