from .base_resource import BaseResource


class Notes(BaseResource):
    """
    The notes resource.
    """

    RESOURCE_NAME = 'notes'

    def create(self, data):
        """
        Create a new note.

        Args:
            data (dict): The note parameters
        Return:
            The note object
        """

        return self._request('POST', self.uri(), data)
