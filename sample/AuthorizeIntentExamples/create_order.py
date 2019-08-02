from sample import PayPalClient
from paypalcheckoutsdk.orders import OrdersCreateRequest
import json


class CreateOrder(PayPalClient):
        
    """Setting up the complete JSON request body for creating the Order. The Intent in the
        request body should be set as "AUTHORIZE" for capture intent flow."""
    @staticmethod
    def build_complete_request_body():
        """Method to create body with AUTHORIZE intent"""
        return \
            {
                "intent": "sale",
                "payer": {
                    "payment_method": "paypal"},
                "redirect_urls": {
                    "return_url": "http://localhost:3000/payment/execute",
                    "cancel_url": "http://localhost:3000/"},
                "transactions": [{
                    "item_list": {
                        "items": [{
                            "name": "item",
                            "sku": "item",
                            "price": "5.00",
                            "currency": "USD",
                            "quantity": 1}]},
                    "amount": {
                        "total": "5.00",
                        "currency": "USD"},
                    "description": "This is the payment transaction description."}]
            }

    """Setting up the minimum required JSON request body for creating the Order. The Intent in the
        request body should be set as "AUTHORIZE" for capture intent flow."""
    @staticmethod
    def build_minimum_request_body():
        """Method to create body with AUTHORIZE intent"""
        return \
            {
                "intent": "AUTHORIZE",
                "application_context": {
                    "return_url": "https://www.example.com",
                    "cancel_url": "https://www.example.com"
                },
                "purchase_units": [
                    {
                        "amount": {
                            "currency_code": "USD",
                            "value": "220.00"
                            }
                    }
                ]
            }

    """This function can be used to create an order with complete request body"""
    def create_order(self, debug=False):
        request = OrdersCreateRequest()
        request.headers['prefer'] = 'return=representation'
        request.request_body(self.build_complete_request_body())
        response = self.client.execute(request)
        if debug:
            print 'Order With Complete Payload:'
            print 'Status Code:', response.status_code
            print 'Status:', response.result.status
            print 'Order ID:', response.result.id
            print 'Intent:', response.result.intent
            print 'Links:'
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            print 'Total Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
                                               response.result.purchase_units[0].amount.value)
            json_data = self.object_to_json(response.result)
            print "json_data: ", json.dumps(json_data,indent=4)
        return response

    """This function can be used to create an order with minimum required request body"""
    def create_order_with_minimum_payload(self, debug=False):
        request = OrdersCreateRequest()
        request.prefer('return=representation')
        request.request_body(self.build_minimum_request_body())
        response = self.client.execute(request)
        if debug:
            print 'Order With Minimum Payload:'
            print 'Status Code:', response.status_code
            print 'Status:', response.result.status
            print 'Order ID:', response.result.id
            print 'Intent:', response.result.intent
            print 'Links:'
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            print 'Total Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
                                               response.result.purchase_units[0].amount.value)
            json_data = self.object_to_json(response.result)
            print "json_data: ", json.dumps(json_data,indent=4)
        return response

"""This is the driver function which invokes the createOrder function to create
   an sample order."""
if __name__ == "__main__":
    CreateOrder().create_order(debug=True)
    CreateOrder().create_order_with_minimum_payload(debug=True)
