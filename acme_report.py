from random import randint, sample, uniform
from acme import Product

ADJS = ['Awesome ', 'Shiny ', 'Impressive ', 'Portable ', 'Improved ']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Slingshot']

def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        name = sample(ADJS, 1)[0]+sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        products.append(Product(name, price = price, weight = weight, flammability= flammability))
    return products

def inventory_report(products):
    s = set()
    total_of_prices = 0
    total_weights = 0
    total_flam = 0
    for i in products:
        s.add(i)
        total_of_prices += i.price
        total_weights += i.weight
        total_flam += i.flammabilty

    print(f'Unique product names: {len(s)}')
    print(f'Average price: {total_of_prices / len(s)}')
    print(f'Average weight: {total_weights/len(s)}')
    print(f'Average flammability:  {total_flam / len(s)}')

if __name__ == '__main__':
    inventory_report(generate_products())
