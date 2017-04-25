from __future__ import (absolute_import, print_function)
#  from nose.tools import *
from payoneer_escrow_sdk.client import Client
from payoneer_escrow_sdk.authenticator import Authenticator
from payoneer_escrow_sdk.api.base_resource import BaseResource


def setup():
    pass


def teardown():
    pass


def test_uri_empty_object():
    """
    Ensure we are creating the URI correctly without an object.
    """

    client = Client('key', 'secret', True)
    auth = Authenticator('key', 'secret')
    resource = BaseResource(client._base_url, auth, '')

    assert resource.uri() == '/'


def test_uri_with_object():
    """
    Ensure we are creating the URI correctly with an object.
    """

    client = Client('key', 'secret', True)
    auth = Authenticator('key', 'secret')
    resource = BaseResource(client._base_url, auth, '')
    object_id = '12345'

    print(resource.uri(object_id))
    assert resource.uri(object_id) == '//' + object_id
