from .base_resource import BaseResource
from .disputes import Disputes
from .documents import Documents
from .milestones import Milestones
from .notes import Notes
from .order_events import OrderEvents
from .order_ledgers import OrderLedgers
from .payment_instructions import PaymentInstructions
from .shipments import Shipments


class Orders(BaseResource):
    """
    The orders resource.
    """

    RESOURCE_NAME = 'orders'

    def create(self, data):
        """
        Create a new order with the supplied data.

        Args:
            data (dict): The order creation parameters
        Return:
            The order object
        """

        return self._request('POST', self.uri(), data)

    def update(self, order_id, data):
        """
        Update the specified order with the supplied data.

        Args:
            account_id (int): The order_id of the order in question
            data (dict): The order parameters
        Return:
            The order object
        """

        return self._request('POST', self.uri(order_id), data)

    def disputes(self, order_id):
        """
        Add or access disputes on the specified order.

        Args:
            order_id (int): The order_id of the order in question
        """

        return Disputes(self.host, self.authenticator, self.uri(order_id))

    def documents(self, order_id):
        """
        Add or access documents on the specified order.

        Args:
            order_id (int): The order_id of the order in question
        """

        return Documents(self.host, self.authenticator, self.uri(order_id))

    def milestones(self, order_id):
        """
        Access milestones on the specified order.

        Args:
            order_id (int): The order_id of the order in question
        """

        return Milestones(self.host, self.authenticator, self.uri(order_id))

    def notes(self, order_id):
        """
        Add or access notes on the specified order.

        Args:
            order_id (int): The order_id of the order in question
        """

        return Notes(self.host, self.authenticator, self.uri(order_id))

    def order_events(self, order_id):
        """
        Access order events on the specified order.

        Args:
            order_id (int): The order_id of the order in question
        """

        return OrderEvents(self.host, self.authenticator, self.uri(order_id))

    def order_ledgers(self, order_id):
        """
        Access order ledgers on the specified order.

        Args:
            order_id (int): The order_id of the order in question
        """

        return OrderLedgers(self.host, self.authenticator, self.uri(order_id))

    def payment_instructions(self, order_id):
        """
        Access payment instructions for the specified order.

        Args:
            order_id (int): The order_id of the order in question
        """

        return PaymentInstructions(self.host, self.authenticator, self.uri(order_id))

    def shipments(self, order_id):
        """
        Add or access shipments on the specified order.

        Args:
            order_id (int): The order_id of the order in question
        """

        return Shipments(self.host, self.authenticator, self.uri(order_id))
