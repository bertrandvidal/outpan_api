Outpan.com API
==============

|PyPI latest version badge|\ |Code health|

Python client for the `Outpan.com
API <http://www.outpan.com/developers.php>`__

Usage
-----

You'll first need to `create an
account <http://www.outpan.com/index.php>`__ and get your API key.

Once you have your API key and the package is installed - see below -
you are set and ready to go.

Getting ready
~~~~~~~~~~~~~

To access the Outpan API you'll need to create an instance of
``OutpanApi`` with your API key. You'll use this object to access the
API.

.. code:: python

    from outpan import OutpanApi
    api = OutpanApi(my_api_key)

Getting a product's data
~~~~~~~~~~~~~~~~~~~~~~~~

Now that you are set it is time to make calls to the API. The first
thing you will want to do is retrieve a product information. For our
test we'll use the test barcode ``078915030900``.

.. code:: python

    api.get_product("078915030900")

This call will return the product's data as a ``dict``:

.. code:: javascript

    {'attributes': {'Care': 'Dishwasher safe',
                    'Colors': 'White',
                    'Manufacturer': 'Progressive International',
                    'Material': 'Plastic, Stainless Steel',
                    'Part Number': 'GPC-5000'},
     'gtin': '0078915030900',
     'images': ['https://outpan-images.s3.amazonaws.com/rg6j1l9iqd-0078915030900.jpg',
                'https://outpan-images.s3.amazonaws.com/835ggkjjq0-0078915030900.png',
                'https://outpan-images.s3.amazonaws.com/8fn652ptobh3ecw886.jpg',
                'https://outpan-images.s3.amazonaws.com/26naopw9flteq3qrcs.jpg',
                'https://outpan-images.s3.amazonaws.com/uhqq6sdj47-0078915030900.jpg'],
     'name': 'Progressive International Cherry-It Pitter',
     'videos': ['https://outpan-images.s3.amazonaws.com/lo0e22j0nj-0078915030900.mp4',
                'https://outpan-images.s3.amazonaws.com/nkvaonl839-0078915030900.mp4',
                'https://outpan-images.s3.amazonaws.com/pjkhqlbgwl-0078915030900.mp4']}

The ``v1`` API allows you to retrieve specific attributes of a product
using the following methods:

.. code:: python

    api.name("078915030900")
    api.attributes("078915030900")
    api.images("078915030900")
    api.videos("078915030900")

The output of these calls is the ``JSON`` as returned by the API.

From the command line
---------------------

Thanks to the awesome python package
`parse\_this <https://github.com/bertrandvidal/parse_this>`__ the Outpan
API is accessible directly from the command line!!!

.. code:: bash

    python outpan.py --help

will give you the help message to know how to use it.

A quick overview of the previous methods we've already talked about:

.. code:: bash

    python outpan.py 123456789 get-product 0796435419035
    python outpan.py 123456789 name 0796435419035
    python outpan.py 123456789 attributes 0796435419035
    python outpan.py 123456789 images 0796435419035
    python outpan.py 123456789 videos 0796435419035

These command lines use the (fake) API key 123456789 to 1. Retrieve the
full info of product 0796435419035 2. Retrieve the name of product
0796435419035 3. Retrieve the attributes of product 0796435419035 4.
Retrieve the image links of product 0796435419035 5. Retrieve the video
links of product 0796435419035

Beta API - available until July 1, 2015
---------------------------------------

`The ``beta`` version of the
API <https://www.outpan.com/developers-legacy.php>`__ is still available
via the ``OutpanApiBeta`` class that can be used in the same way as the
previous class.

Creating or editing a product's name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to create a new object or edit an existing product you can
use the method ``api.add_edit_product_name`` as showed below:

.. code:: python

    api.add_edit_product_name("078915030900", "new_name")

Note that this method does not return anything and will replace any
existing name.

Creating or editing a product's attribute
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also edit or create a product's attribute using the method
``add_edit_product_attribute`` as follow:

.. code:: python

    api.add_edit_product_attribute("078915030900", "attribute_name", "attribute_value")

Note that this method does not return anything and will replace any
existing attribute.

INSTALLING OUTPAN
-----------------

``outpan`` can be installed using the following command:

.. code:: bash

    pip install outpan

or using ``easy_install``:

.. code:: bash

    easy_install outpan

.. |PyPI latest version badge| image:: https://badge.fury.io/py/outpan.svg
   :target: https://pypi.python.org/pypi/outpan
.. |Code health| image:: https://landscape.io/github/bertrandvidal/outpan_api/master/landscape.png
   :target: https://landscape.io/github/bertrandvidal/outpan_api/master
