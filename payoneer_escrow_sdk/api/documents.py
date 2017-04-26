from .base_resource import BaseResource


class Documents(BaseResource):
    """
    The documents resource.
    """

    RESOURCE_NAME = 'documents'

    def create(self, data):
        """
        Create a new document.

        Args:
            data (dict): The document parameters
        Return:
            The document object
        """

        return self._request('POST', self.uri(), data)
