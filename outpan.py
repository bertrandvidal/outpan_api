from __future__ import print_function
import base64
import requests
from pprint import pprint

from parse_this import create_parser, Self, parse_class


class OutpanException(Exception):
    """Exception raised when a requests fails."""


def _check_request_status(response):
    """Help method to check if an error occured.

    Args:
        response -- API server response
    """
    if not response.content:
        # Some method return an empty string we just return None
        return None
    try:
        data = response.json()
    except ValueError:
        # We couldn't decode a json object we just return the
        # response object
        return response
    else:
        # We raise if an error occurred, if not we return the json data
        if "error" in data:
            raise OutpanException("%(message)s - code: %(code)s"
                                  % data["error"])
        return data


@parse_class(description="Simply access the outpan.com API with you api key.")
class OutpanApi(object):
    """Access outpan.com v2 API with your api key."""

    @create_parser(Self, str, delimiter_chars="--")
    def __init__(self, api_key):
        """
        Args:
            api_key -- the api key provided by outpan when you register
        """
        self._api_key = api_key

    @create_parser(Self, str, delimiter_chars="--")
    def get_product(self, barcode):
        """Return all the info about the given barcode.

        Args:
            barcode -- the barcode/GTIN of the product
        """
        response = requests.get("https://api.outpan.com/v2/products/%s?apikey=%s"
                               % (barcode, self._api_key))
        return _check_request_status(response)


@parse_class(description="Simply access the outpan.com API with your api key.")
class OutpanApiV1(object):
    """Access outpan.com v1 API with your api key."""

    _API_URL = "https://api.outpan.com/v1/products/"

    @create_parser(Self, str, delimiter_chars="--")
    def __init__(self, api_key):
        """
        Args:
            api_key -- the api key provided by outpan when you register
        """
        encoded_key = base64.encodestring(bytearray("%s:" % api_key, "utf-8"))
        self._auth_header = {"Authorization": "Basic %s"
                             % encoded_key.decode("ascii")}

    def _get_resource(self, resource_path):
        """Send a GET request to a specific path.

        Args:
            resource_path -- the API path to query
        """
        response = requests.get(self._API_URL + "/" + resource_path,
                                headers=self._auth_header)
        return _check_request_status(response)

    @create_parser(Self, str, delimiter_chars="--")
    def get_product(self, barcode):
        """Returns the name, attributes, images and videos of the product
        identified by the barcode.

        Args:
            barcode -- the barcode/GTIN of the product
        """
        return self._get_resource(barcode)

    @create_parser(Self, str, delimiter_chars="--")
    def name(self, barcode):
        """Returns a dict containing the barcode and name of the product.

        Args:
            barcode -- the barcode of the product
        """
        return self._get_resource("%s/name" % barcode)

    @create_parser(Self, str, delimiter_chars="--")
    def attributes(self, barcode):
        """Returns a dict containing the barcode and attributes of the product.

        Args:
            barcode -- the barcode of the product
        """
        return self._get_resource("%s/attributes" % barcode)

    @create_parser(Self, str, delimiter_chars="--")
    def images(self, barcode):
        """Returns a dict containing the barcode and image links of the product.

        Args:
            barcode -- the barcode of the product
        """
        return self._get_resource("%s/images" % barcode)

    @create_parser(Self, str, delimiter_chars="--")
    def videos(self, barcode):
        """Returns a dict containing the barcode and videos links of the
        product.

        Args:
            barcode -- the barcode of the product
        """
        return self._get_resource("%s/videos" % barcode)


def run_cli():
    result = OutpanApiV1.parser.call()
    pprint(result if result else "SUCCESS")


if __name__ == "__main__":
    RESULT = OutpanApiV1.parser.call()
    pprint(RESULT if RESULT else "SUCCESS")
