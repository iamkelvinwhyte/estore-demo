class eStore():
    """
    EStore Class Helper to View Product, Add item to basket, View Backet,Empty Backet,Add Discount Offer, View Offer
    Empty Offer and Display Pricing .
    """

    def __init__(self):
        self.baskets = []
        self.offers = []
        self.products = [{"name": "Soup", "price": 0.65, "qty": 5, 'type': "tin"},
                         {"name": "Bread", "price": 0.8, "qty": 5, 'type': "loaf"},
                         {"name": "Milk", "price": 1.30,
                             "qty": 5, 'type': "bottle"},
                         {"name": "Apples", "price": 1, "qty": 5, 'type': "bag"},
                         ]

    def view_product(self):
        return self.products

    def add_to_basket(self, item):
        """
         Add item to basket.
         ----------
         :param String : eg Apples Milk Bread
        """

        try:
            item_list = [x for x in item.split()]
            if len(item_list) == 0:
                return "No item added"
            for product in self.products:
                if product['name'] in item_list:
                    found = False
                    for index, basket in enumerate(self.baskets):
                        if product['name'] == basket['name']:
                            self.baskets[index]['qty'] += 1
                            found = True
                    if found == False:
                        self.baskets.append(
                            {"name": product['name'], "qty": 1, "price": product['price']})

            return f"{len(self.baskets)} Item added to cart"
        except Exception as inst:
            print(f"{type(inst)} - {inst.args}-{inst}")

    def view_basket(self):
        """
         View item in basket.
        """
        if len(self.baskets)==0:
            return "Cart is empty "
        else:
            return self.baskets

    def empty_basket(self):
        """
         Empty item in basket.
        """
        self.baskets.clear()
        return "Basket Cleared"

    def add_offer(self, **kwargs):
        """
         Add special off to product.
         ----------
         :param String item : eg Bread
         :param Int offer_value : eg 20
         :param Int no_of_buy : eg 2
         :param String no_of_buy : eg Bread
        """
        item = kwargs.get('item', None)
        offer_value = self.validator(kwargs.get('offer_value', 0))
        no_of_buy = self.validator(kwargs.get('no_of_buy', 0))
        prod_discount = kwargs.get('prod_discount', None)
        print(no_of_buy)

        try:
            for index, product in enumerate(self.products):
                if item == product['name']:
                    found = False
                    for index, offer in enumerate(self.offers):
                        if product['name'] == offer['name']:
                            self.offers[index]['offer_value'] = offer_value
                            self.offers[index]['no_of_buy'] = no_of_buy
                            self.offers[index]['offer_value'] = prod_discount
                            found = True

                    if found == False:
                        self.offers.append(
                            {"name": product['name'], "offer_value": offer_value, "no_of_buy": no_of_buy, "prod_discount": prod_discount})
            return f"{len(self.offers)} discount added"
        except Exception as inst:
            print(f"{type(inst)} - {inst.args}-{inst}")

    def view_offer(self):
        """
         View Product offer.
        """
        return self.offers

    def c_filter(self, num):
        return f'{round(num,2)}'

    def empty_offer(self):
        """
         Empty Product offer.
        """
        self.offers.clear()
        return "Discount Cleared"

    def pricing(self):
        """
         View Pricing.
        """
        Subtotal = 0
        discount = 0
        discount_offer = ""
        if len(self.baskets)==0:
            return "Cart is empty"
        try:
            for i, basket in enumerate(self.baskets):

                for index, offer in enumerate(self.offers):

                    if basket['name'] in self.offers[index]["name"]:

                        if offer["prod_discount"] == basket["name"]:
                    
                            if int(basket["qty"]) >= int(offer["no_of_buy"]):
                                discount_price = basket["price"] * (int(offer["offer_value"])/100)
                                discount += discount_price*basket["qty"]
                                discount_offer += f'{offer["prod_discount"]} {offer["offer_value"]}% off : {(discount_price*basket["qty"])}'
                        else:
                            for i, basket in enumerate(self.baskets):
                                if offer["prod_discount"] in self.baskets[i]["name"]:

                                    if int(basket["qty"]) >= int(offer["no_of_buy"]):
                                        discount_price = basket["price"] *  (int(offer["offer_value"])/100)
                                        discount += discount_price *  basket["qty"]
                                        discount_offer += f'{offer["prod_discount"]} {offer["offer_value"]}% off : {(discount_price*basket["qty"])}'
                Subtotal += (basket["price"]*basket["qty"])

            print(f"Subtotal: {self.c_filter(Subtotal)}")
            print(discount_offer)
            print(f"Total: {self.c_filter(Subtotal-discount)}")
 
        except Exception as inst:
            print(f"{type(inst)} - {inst.args}-{inst}")


    def validator(self,val):
        if val=="":
            return 0
        else:
            return val

        
