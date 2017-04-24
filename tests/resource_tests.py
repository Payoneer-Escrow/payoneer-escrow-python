from __future__ import absolute_import
from nose.tools import *
from payoneer_escrow_sdk.client import Client
from payoneer_escrow_sdk.authenticator import Authenticator
from payoneer_escrow_sdk.api.resource import Resource


def setup():
    pass


def teardown():
    pass


def test_uri_empty_object():
    """
    Ensure we are creating the uri correctly without an object.
    """

    client = Client('key', 'secret', True)
    auth = Authenticator('key', 'secret')
    resource = Resource(client._base_url, auth, '')

    assert resource.uri() == '/'


def test_uri_with_object():
    """
    Ensure we are creating the uri correctly with an object.
    """

    client = Client('key', 'secret', True)
    auth = Authenticator('key', 'secret')
    resource = Resource(client._base_url, auth, '')
    object_id = '12345'

    print(resource.uri(object_id))
    assert resource.uri(object_id) == '//' + object_id
