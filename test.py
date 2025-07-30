import unittest

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_items_and_total_cost(self):
        self.cart.add_item('Apple', 1.5)
        self.cart.add_item('Banana', 2.0)
        self.assertEqual(self.cart.total_cost(), 3.5)

    def test_empty_cart_total(self):
        self.assertEqual(self.cart.total_cost(), 0)

    def test_negative_price_raises_error(self):
        with self.assertRaises(ValueError):
            self.cart.add_item('Orange', -1.0)

if __name__ == '__main__':
    unittest.main()
