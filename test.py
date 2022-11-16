import unittest
from Class import eStore
e = eStore()

class TestStore(unittest.TestCase):

    def setUp(self):
        self.item = "Apples Milk Bread"
        self.invalid_item = "Orange Goat"
 
    def test_for_empty_item_added_to_basket(self):
        response=e.add_to_basket("")
        self.assertEqual(response, "No item added")

    def test_for_invalid_item_added_to_basket(self):
        response = e.add_to_basket(self.invalid_item)
        self.assertEqual(response, "0 Item added to cart")

    def test_for_valid_item_added_to_basket(self):
        response = e.add_to_basket(self.item)
        self.assertNotEqual(response, "0 Item added to cart")

    def test_for_offer_added(self):
        response = e.add_offer(item="Apples", offer_value=10,
                               no_of_buy="", prod_discount="Apples")
        self.assertEqual(response, "1 discount added")

    def test_for_Invalid_offer_added(self):
        response = e.add_offer(item="Orange", offer_value=10,
                               no_of_buy="", prod_discount="Apples")
        self.assertEqual(response, "0 discount added")

    def test_if_pricing_cart_is_empty(self):
        e.empty_basket()
        response = e.pricing()
        self.assertEqual(response, "Cart is empty")

if __name__ == '__main__':
    unittest.main()
