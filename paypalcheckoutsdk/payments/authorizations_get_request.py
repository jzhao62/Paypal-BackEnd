# This class was generated on Tue, 10 Jul 2018 10:40:35 PDT by version 0.1.0-dev+0ee05a-dirty of Braintree SDK Generator
# authorizations_get_request.py
# @version 0.1.0-dev+0ee05a-dirty
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class AuthorizationsGetRequest:
    """
    Shows details for an authorized payment, by ID.
    """
    def __init__(self, authorization_id):
        self.verb = "GET"
        self.path = "/v2/payments/authorizations/{authorization_id}?".replace("{authorization_id}", quote(str(authorization_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
