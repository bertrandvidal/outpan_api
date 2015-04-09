from __future__ import print_function
import base64
import warnings
import requests

from parse_this import create_parser, Self, parse_class

warnings.simplefilter('always', DeprecationWarning)


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


class OutpanApi(object):
    """Access outpan.com v1 API with your api key."""

    _API_URL = "https://api.outpan.com/v1/products/"

    def __init__(self, api_key):
        """
        Args:
            api_key -- the api key provided by outpan when you register
        """
        encoded_key = base64.encodestring(bytearray("%s:" % api_key, "utf-8"))
        self._auth_header = {"Authorization": "Basic %s"
                             % encoded_key.decode("ascii")}


@parse_class(description="Simply access the outpan.com API with your api key.")
class OutpanApiBeta(object):
    """Provides a simple way to access the outpan.com API.

    Usage:
        from outpan import OutpanApiBeta
        api = OutpanApiBeta(<you_api_key>)
        api.get_product("0078915030900")
    """

    _API_URL = "https://www.outpan.com/api"

    @create_parser(Self, str, delimiter_chars="--")
    def __init__(self, api_key):
        """
        Args:
            api_key -- the api key provided by outpan when you registered
        """
        self._api_key = api_key
        warnings.warn("The Beta OutpanApi will be deprecated on July 1, 2015",
                      DeprecationWarning)

    def _get_params(self, params):
        """Returns the given parameters extended with the api key parameter.

        Args:
            params -- parameters of the request you want to extend
        """
        params.update({"apikey": self._api_key})
        return params

    def _get_url(self, resource):
        """Return the full URL for the given resource

        Args:
            resource -- path to the resource you want to query
        """
        return "%s/%s" % (self._API_URL, resource)

    @create_parser(Self, str, delimiter_chars="--")
    def get_product(self, barcode):
        """Returns the product data specified by the barcode.

        Args:
            barcode -- the barcode you are looking for

        Returns:
            A dictionary containing the product data. It could be mostly empty
            if outpan doesn't have data for the product, it is up to the caller
            to verify the data
        """
        params = self._get_params({"barcode": barcode})
        full_url = self._get_url("get-product.php")
        response = requests.get(full_url, params=params)
        return _check_request_status(response)

    @create_parser(Self, str, str, delimiter_chars="--", name="add_edit_name")
    def add_edit_product_name(self, barcode, name):
        """Add or Edit the name of the product specify by the barcode.

        Args:
            barcode -- the barcode of the product you want to add/edit
            name -- name of the product you want to add/edit

        Note:
            Whether the barcode has already a name associateed with it or not,
            it will be replaced with the new name submitted by the API request.
            If the barcode exists the name will be replaced.

        Returns:
            Because the content of the request is empty the decorator used on
            this method will return None
        """
        params = self._get_params({"barcode": barcode, "name": name})
        full_url = self._get_url("edit-name.php")
        response = requests.get(full_url, params=params)
        return _check_request_status(response)

    @create_parser(Self, str, str, str, delimiter_chars="--",
                   name="add_edit_attr")
    def add_edit_product_attribute(self, barcode, attr_name, attr_value):
        """Add or edit an attribute to the product defined by the barcode.

        Args:
            barcode -- barcode of the object you want to edit
            attr_name -- name of the attribute to add/edit
            attr_value -- value of the attribute to add/edit

        Note:
            If the attribute already exists its value will be replaced

        Returns:
            Because the content of the request is empty the decorated used on
            this method will return None
        """
        params = self._get_params({"barcode": barcode, "attr_name": attr_name,
                                   "attr_value": attr_value})
        full_url = self._get_url("edit-attr.php")
        response = requests.get(full_url, params=params)
        return _check_request_status(response)


if __name__ == "__main__":
    RESULT = OutpanApiBeta.parser.call()
    print(RESULT if RESULT else "SUCCESS")
