from functools import wraps
import requests


class OutpanException(Exception):
    """Exception raised when a requests fails."""


def check_request_status(func):
    """Decorator for OutpanAPI method to check if an error occured.

    Args:
        func -- the function to be decorated
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        response = func(*args, **kwargs)
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
    return decorated


class OutpanApi(object):
    """Access the Outpan API.

    Usage:
        from outpan import OutpanAPI
        api = OutpanAPI(<you_api_key>)
        api.get_product("0078915030900")
    """

    _API_URL = "http://www.outpan.com/api"

    def __init__(self, api_key):
        """
        Args:
            api_key -- the api key provided by outpan when you register
        """
        self._api_key = api_key

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
        return "%s/%s" % (self.__class__._API_URL, resource)

    @check_request_status
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
        return requests.get(full_url, params=params)

    @check_request_status
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
        return requests.get(full_url, params=params)

    @check_request_status
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
        return requests.get(full_url, params=params)

