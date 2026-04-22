# ecommerce.py

import random
from datetime import datetime

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def check_stock(self):
        return self.stock > 0

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.order_history = []

    def place_order(self, product, quantity):
        if not product.check_stock():
            raise OutOfStockException(f"Out of stock for {product.name}")
        
        total_price = product.price * quantity
        
        # Simulate payment processing (for demonstration purposes)
        print(f"{self.name} placed an order for {quantity} {product.name}s at a total price of ${total_price}.")
        
        self.order_history.append((datetime.now(), product, quantity))

class OrderManager:
    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self, name, price, stock):
        product = Product(name, price, stock)
        self.products.append(product)

    def add_customer(self, name, email, address):
        customer = Customer(name, email, address)
        self.customers.append(customer)

    def generate_dummy_records(self, num_records=500):
        for _ in range(num_records):
            product_name = random.choice(['Product A', 'Product B', 'Product C'])
            price = round(random.uniform(10.0, 200.0), 2)
            stock = random.randint(1, 100)

            self.add_product(product_name, price, stock)

    def process_transactions(self):
        for customer in self.customers:
            for _ in range(5):  # Simulate multiple orders per customer
                product_name = random.choice([p.name for p in self.products])
                quantity = random.randint(1, 10)
                
                try:
                    product = next(p for p in self.products if p.name == product_name)
                    customer.place_order(product, quantity)
                except OutOfStockException as e:
                    print(e)

    def export_database_state(self):
        # Simulate database state export to JSON
        data = {
            'products': [p.__dict__ for p in self.products],
            'customers': [c.__dict__ for c in self.customers]
        }
        
        with open('database_state.json', 'w') as f:
            json.dump(data, f)

# Usage example
if __name__ == '__main__':
    manager = OrderManager()
    
    # Generate dummy records
    manager.generate_dummy_records(500)
    
    # Process transactions
    manager.process_transactions()
    
    # Export database state to JSON
    manager.export_database_state()