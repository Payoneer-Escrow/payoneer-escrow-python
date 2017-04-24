from __future__ import absolute_import
from nose.tools import *
from payoneer_escrow_sdk.authenticator import Authenticator


def setup():
    pass


def teardown():
    pass


def test_secure_headers():
    """
    Verify that secure_headers has the right keys and (certain) values.

    We will test the value of the request signature below, but here we are at
    least verifying that it is the length we expect.
    """

    auth = Authenticator(
        'test_key', 'test_secret')
    method = 'POST'
    uri = '/accounts/5818958914?55811'
    secure_headers = auth.secure_headers(method, uri)

    assert type(secure_headers).__name__ == 'dict'
    assert len(secure_headers) == 3
    assert secure_headers['x-armorpayments-apikey'] == 'test_key'
    assert len(secure_headers['x-armorpayments-requesttimestamp']) == 25
    assert len(secure_headers['x-armorpayments-signature']) == 128


def test__request_signature():
    """
    Confirm that we have reproducable results with _request_signature.
    """

    auth = Authenticator(
        'test_key', 'test_secret')
    method = 'POST'
    uri = '/accounts/5818958914?55811'
    timestamp = '2017-04-24T02:52:53-00:00'
    actual = auth._request_signature(method, uri, timestamp)

    expected = 'c70a4b43a271cdc40db55c5b2ddfaeabc9fb448fd16b3f261027cb3ed06fd4954799e8e40b1d64781225a4c2ef71ea938ca7cdff8228ade561041a994f6dd299'

    assert actual == expected


def test__request_signature_variations_do_not_have_same_hash():
    """
    Confirm that we get different results when we vary each of the inputs.
    """

    auth = Authenticator(
        'test_key', 'test_secret')
    method = 'POST'
    uri = '/accounts/5818958914?55811'
    timestamp = '2017-04-24T02:52:53-00:00'
    alt_method = 'get'
    alt_uri = '/shipmentcarriers'
    alt_timestamp = '2017-04-24T02:52:54-00:00'
    actual = auth._request_signature(method, uri, timestamp)
    actual_alt_method = auth._request_signature(alt_method, uri, timestamp)
    actual_alt_uri = auth._request_signature(method, alt_uri, timestamp)
    actual_alt_timestamp = auth._request_signature(method, uri, alt_timestamp)

    actual_as_set = set([
        actual,
        actual_alt_method,
        actual_alt_uri,
        actual_alt_timestamp])

    expected = 'c70a4b43a271cdc40db55c5b2ddfaeabc9fb448fd16b3f261027cb3ed06fd4954799e8e40b1d64781225a4c2ef71ea938ca7cdff8228ade561041a994f6dd299'

    assert actual == expected
    assert len(actual_as_set) == 4


def test__request_signature_method_case_does_not_matter():
    """
    Confirm that the case of the method does not change the result.
    """

    auth = Authenticator(
        'test_key', 'test_secret')
    method = 'POST'
    lowercase_method = 'post'
    uri = '/accounts/5818958914?55811'
    timestamp = '2017-04-24T02:52:53-00:00'
    actual = auth._request_signature(method, uri, timestamp)
    actual_lowercase = auth._request_signature(lowercase_method, uri, timestamp)

    expected = 'c70a4b43a271cdc40db55c5b2ddfaeabc9fb448fd16b3f261027cb3ed06fd4954799e8e40b1d64781225a4c2ef71ea938ca7cdff8228ade561041a994f6dd299'

    assert actual == expected
    assert actual_lowercase == expected
