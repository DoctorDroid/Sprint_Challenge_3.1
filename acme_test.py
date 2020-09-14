import unittest
from acme import Product
from acme_report import generate_products, ADJS, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    def test_default_product_weight(self):
        """Test default product price being 10."""
        prod = Product('Test Product 2')
        self.assertEqual(prod.weight, 20)

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        list = generate_products()
        self.assertEqual(len(list), 30)

if __name__ == '__main__':
    unittest.main()