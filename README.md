Outpan.com API
==============

[![PyPI latest version badge][pypi_version]][pypi_link] [![PyPI monthly downloads][pypi_downloads]][pypi_link]

Python client for the [![Outpan.com API][outpan_api]]

Usage
-----

You'll first need to [![create an account][outpan_register]] and get your API key.

Once you have your API key and the package is installed - see below - you are
set and ready to go.

### Getting ready

To access the Outpan API you'll need to create an instance of `OutpanApi` with
your API key. You'll use this objcet to access the API.

```python
from outpan import OutpanApi
api = OutpanApi(my_api_key)
```

### Getting a product's data

Now that you are set it is time to make calls to the API. The first thing you
will want to do is retrieve a product information. For our test we'll use the
test barcode `078915030900`.

```python
api.get_product("078915030900")
```

This call will return the product's data as a `dict`:

```json
{'attributes': {'Care': 'Dishwasher safe',
                'Colors': 'White',
                'Manufacturer': 'Progressive International',
                'Material': 'Plastic, Stainless Steel',
                'Part Number': 'GPC-5000'},
 'barcode': '0078915030900',
 'images': ['https://outpan-images.s3.amazonaws.com/rg6j1l9iqd-0078915030900.jpg',
            'https://outpan-images.s3.amazonaws.com/835ggkjjq0-0078915030900.png',
            'https://outpan-images.s3.amazonaws.com/8fn652ptobh3ecw886.jpg',
            'https://outpan-images.s3.amazonaws.com/26naopw9flteq3qrcs.jpg',
            'https://outpan-images.s3.amazonaws.com/uhqq6sdj47-0078915030900.jpg'],
 'name': 'Progressive International Cherry-It Pitter',
 'outpan_url': 'http://www.outpan.com/view_product.php?barcode=0078915030900',
 'videos': ['https://outpan-images.s3.amazonaws.com/lo0e22j0nj-0078915030900.mp4',
            'https://outpan-images.s3.amazonaws.com/nkvaonl839-0078915030900.mp4',
            'https://outpan-images.s3.amazonaws.com/pjkhqlbgwl-0078915030900.mp4']}
```

### Creating or editing a product's name

If you want to create a new object or edit an existing product you can use the
method `api.add_edit_product_name` as showed below:

```python
api.add_edit_product_name("078915030900", "new_name")
```

Note that this method does not return anything and will replace any existing name.


### Creating or editing a product's attribute

You can also edit or create a product's attribute using the method
`add_edit_product_attribute` as follow:

```python
api.add_edit_product_attribute("078915030900", "attribute_name", "attribute_value")
```

Note that this method does return anything and will replace any existing attribute.


INSTALLING OUTPAN
-----------------

`outpan` can be installed using the following command:

```bash
pip install outpan
```

or using `easy_install`:

```bash
easy_install outpan
```

[outpan_api]: http://www.outpan.com/developers.php
[outpan_register]: http://www.outpan.com/index.php
[pypi_link]: https://pypi.python.org/pypi/parse_this "parse_this on PyPI"
[pypi_version]: https://pypip.in/v/parse_this/badge.png "PyPI latest version"
[pypi_downloads]: https://pypip.in/d/parse_this/badge.png "PyPI monthly downloads"
