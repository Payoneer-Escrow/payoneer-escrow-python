from .base_resource import BaseResource


class Shipments(BaseResource):
    """
    The shipments resource.
    """

    RESOURCE_NAME = 'shipments'

    def create(self, data):
        """
        Create a new shipment.

        Args:
            data (dict): The shipment parameters
        Return:
            The shipment object
        """

        return self._request('POST', self.uri(), data)
