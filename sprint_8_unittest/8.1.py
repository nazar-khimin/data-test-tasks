import unittest


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    total_price = 0
    def __init__(self, product_list=None):
        self.product_list = product_list if product_list else []

    def add_product(self, product: Product):
        self.product_list.append(product)

    def get_total_price(self):
        count_discounts = {
            5: 0.05,
            7: 0.10,
            10: 0.20,
            20: 0.30,
            21: 0.50,
        }

        for product in self.product_list:
            discount_value = max((discount_value
                                  for count, discount_value in count_discounts.items()
                                  if product.count >= count),
                                 default=0)
            product_price = product.price * product.count
            discount_price = product_price * discount_value
            self.total_price = self.total_price + (product_price - discount_price)

        return self.total_price


class CartTest(unittest.TestCase):

    def test_add_product(self):
        cart = Cart()
        product = Product("Apple", 1.0, 3)
        cart.add_product(product)
        self.assertEqual(len(cart.product_list), 1)

    def test_calculate_total_price_no_discount(self):
        cart = Cart()
        cart.add_product(Product("Banana", 1.5, 2))
        cart.add_product(Product("Orange", 2.0, 2))
        self.assertEqual(cart.get_total_price(), 7.0)

    def test_calculate_total_price_with_discount(self):
        cart = Cart()
        cart.add_product(Product("Apple", 1.0, 5))
        cart.add_product(Product("Banana", 2.0, 5))
        self.assertEqual(cart.get_total_price(), 14.25)

    def test_calculate_total_price_high_discount(self):
        cart = Cart()
        cart.add_product(Product("Grapes", 5.0, 21))
        self.assertEqual(cart.get_total_price(), 52.5)

    def test_all_options(self):
        products = (Product('p1', 10, 4),
                    Product('p2', 100, 5),
                    Product('p3', 200, 6),
                    Product('p4', 300, 7),
                    Product('p5', 400, 9),
                    Product('p6', 500, 10),
                    Product('p7', 1000, 20))
        cart = Cart(products)
        self.assertEqual(cart.get_total_price(), 24785.0)

if __name__ == "__main__":
    unittest.main()