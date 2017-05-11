===============
Payoneer Escrow
===============

This is intended to be a clean, idiomatic client for the `Payoneer Escrow API
<https://escrow.payoneer.com/api>`_. This will handle generating the
authenticated headers and constructing the properly nested request URI, as well
as parsing any response JSON for you.

Installation
------------

You can install using pip_ or from source_.

.. _pip:

pip
~~~

Installation via pip is as easy as any other Python package.

.. code-block:: sh

    $ pip install payoneer-escrow-sdk

    # Alternatively, add to your requirements file and install from there
    $ echo 'payoneer-escrow-sdk' >> requirements.txt

    $ pip install -r requirements.txt

.. _source:

Source
~~~~~~

Download the payoneer-escrow-python source:

.. code-block:: sh

    $ git clone https://github.com/Payoneer-Escrow/payoneer-escrow-python

    $ cd payoneer-escrow-python

    # Install the package
    $ python setup.py install

Quickstart
----------

This project's GitHub repo contains example files to help you get going. To
avoid any potential risk, these files are not included in the package installed
via ``pip``. ``example.py`` is recommended for all who are new to this SDK—it
allows you to confirm your api credentials and shows example handling of an
``HTTPError`` encountered by a bad request. There is also an end-to-end goods
milestone order  in the ``examples/`` directory to demonstrate use of the API
with one of the more complicated order types.

.. code-block:: sh

    # If you installed via pip, you will need to get the example file
    $ curl https://raw.githubusercontent.com/Payoneer-Escrow/payoneer-escrow-python/master/example.py > example.py

    # Replace the key and secret values with your own credentials
    $ echo 'PAYONEER_ESCROW_API_KEY = "ENTER_YOUR_API_KEY_HERE"
    PAYONEER_ESCROW_SECRET = "ENTER_YOUR_API_SECRET_HERE"' > api_credentials.py

    $ python example.py

Usage
-----

The Payoneer Escrow API is REST-ish and nested, so the client relies on
chaining. We return an object (or array of objects) decoded from the JSON
response, if possible.

.. code-block:: python

    from payoneer_escrow_sdk.client import Client

    # `should_use_sandbox` is a boolean passed to Client, indicating which
    # Payoneer Escrow environment should be used; default is Production.

    client = Client('your-key', 'your-secret', should_use_sandbox)

    # There are two top-level resources: accounts and shipmentcarriers
    # Querying users and orders requires an account_id

    client.accounts().all()
    client.accounts().get(account_id)

    client.shipmentcarriers().all()
    client.shipmentcarriers().get(carrier_id)

    # From accounts, we chain users, orders, bank accounts

    client.accounts().users(account_id).all()
    client.accounts().users(account_id).get(user_id)

    client.accounts().orders(account_id).all()
    client.accounts().orders(account_id).get(order_id)

    client.accounts().bankaccounts(account_id).all()
    client.accounts().bankaccounts(account_id).get(bank_account_id)

    # From orders, many things chain: documents, notes, disputes, shipments,
    # payment instructions, order events, and order ledgers

    client.accounts().orders(account_id).documents(order_id).all()
    client.accounts().orders(account_id).documents(order_id).get(document_id)

    client.accounts().orders(account_id).notes(order_id).all()
    client.accounts().orders(account_id).notes(order_id).get(note_id)

    client.accounts().orders(account_id).disputes(order_id).all()
    client.accounts().orders(account_id).disputes(order_id).get(dispute_id)

    client.accounts().orders(account_id).shipments(order_id).all()
    client.accounts().orders(account_id).shipments(order_id).get(shipment_id)

    client.accounts().orders(account_id).paymentinstructions(order_id).all()

    client.accounts().orders(account_id).orderevents(order_id).all()
    client.accounts().orders(account_id).orderevents(order_id).get(event_id)

    client.accounts().orders(account_id).orderledgers(order_id).all()
    client.accounts().orders(account_id).orderledgers(order_id).get(ledger_entry_id)

    # From disputes, further things chain: documents, notes, offers

    client.accounts().orders(account_id).disputes(order_id).documents(
    dispute_id).all()
    client.accounts().orders(account_id).disputes(order_id).documents(
    dispute_id).get(document_id)

    client.accounts().orders(account_id).disputes(order_id).notes(
    dispute_id).all()
    client.accounts().orders(account_id).disputes(order_id).notes(
    dispute_id).get(note_id)

    client.accounts().orders(account_id).disputes(order_id).offers(
    dispute_id).all()
    client.accounts().orders(account_id).disputes(order_id).offers(
    dispute_id).get(offer_id)

    # From offers, documents and notes chain

    client.accounts().orders(account_id).disputes(order_id).offers(
    dispute_id).documents(offer_id).all()
    client.accounts().orders(account_id).disputes(order_id).offers(
    dispute_id).documents(offer_id).get(document_id)

    client.accounts().orders(account_id).disputes(order_id).offers(
    dispute_id).notes(offer_id).all()
    client.accounts().orders(account_id).disputes(order_id).offers(
    dispute_id).notes(offer_id).get(note_id)

Some of the resource endpoints support Create/Update `POST` operations, and
this client aims to support those as well:

.. code-block:: python

    # Account-related
    client.accounts().create(your_data)
    client.accounts().update(account_id, your_data)

    client.accounts().users(account_id).create(your_data)
    client.accounts().users(account_id).update(user_id, your_data)


    # Authenticate a URI for display in a lightbox
    client.accounts().users(account_id).authentications(user_id).create(your_data)


    # Order-related
    client.accounts().orders(account_id).create(your_data)
    client.accounts().orders(account_id).update(order_id, your_data)

    client.accounts().orders(account_id).documents(order_id).create(your_data)

    client.accounts().orders(account_id).notes(order_id).create(your_data)

    client.accounts().orders(account_id).shipments(order_id).create(your_data)


    # Dispute-related
    client.accounts().orders(account_id).disputes(order_id).create(your_data)

    client.accounts().orders(account_id).disputes(order_id).documents(
    dispute_id).create(your_data)

    client.accounts().orders(account_id).disputes(order_id).notes(
    dispute_id).create(your_data)

    client.accounts().orders(account_id).disputes(order_id).offers(
    dispute_id).create(your_data)
    client.accounts().orders(account_id).disputes(order_id).offers(
    dispute_id).update(offer_id, your_data)

    client.accounts().orders(account_id).disputes(order_id).offers(
    dispute_id).documents(offer_id).create(your_data)

    client.accounts().orders(account_id).disputes(order_id).offers(
    dispute_id).notes(offer_id).create(your_data)

Contributing
------------

1. Fork it
2. Create your feature branch (``git checkout -b my-new-feature``)
3. Commit your changes (``git commit -am 'Add some feature'``)
4. Push to the branch (``git push origin my-new-feature``)
5. Create new Pull Request
