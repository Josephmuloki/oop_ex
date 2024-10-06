class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        # Initialize the product with a name, price, and quantity in stock
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        # Display the product's details
        print(f"Product: {self.product_name}, Price: {self.price}, Quantity in stock: {self.quantity_in_stock}")

class ShoppingCart:
    # Class variable to track the total number of shopping carts created
    total_carts = 0

    def __init__(self):
        # Initialize the cart with an empty list of items
        self.items = []
        # Increment the total cart count
        ShoppingCart.total_carts += 1

    def add_to_cart(self, product, quantity):
        # Check if the requested quantity is available in stock
        if quantity <= product.quantity_in_stock:
            # Add the product and quantity to the cart
            self.items.append((product, quantity))
            # Reduce the quantity in stock
            product.quantity_in_stock -= quantity
            print(f"Added {quantity} of {product.product_name} to the cart.")
        else:
            print(f"Not enough stock for {product.product_name}.")

    def remove_from_cart(self, product):
        # Iterate through the items in the cart
        for item in self.items:
            if item[0] == product:
                # Remove the product from the cart
                self.items.remove(item)
                # Restore the quantity in stock
                product.quantity_in_stock += item[1]
                print(f"Removed {item[1]} of {product.product_name} from the cart.")
                return
        print(f"{product.product_name} not found in the cart.")

    def display_cart(self):
        # Check if the cart is empty
        if not self.items:
            print("The cart is empty.")
        else:
            # Display all items in the cart
            print("Cart contents:")
            for product, quantity in self.items:
                print(f"{product.product_name}: {quantity}")

    def calculate_total(self):
        # Calculate the total price of items in the cart
        total = sum(product.price * quantity for product, quantity in self.items)
        return total

# Creating Product objects
product1 = Product("Laptop", 1000, 10)
product2 = Product("Smartphone", 500, 20)
product3 = Product("Headphones", 100, 50)

# Displaying product information
product1.display_product_info()
product2.display_product_info()
product3.display_product_info()

# Creating ShoppingCart instances
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Performing operations on cart1
cart1.add_to_cart(product1, 2)  # Adds 2 Laptops to cart1
cart1.add_to_cart(product2, 1)  # Adds 1 Smartphone to cart1
cart1.display_cart()  # Displays the contents of cart1
print(f"Total amount due for cart1: {cart1.calculate_total()}")  # Calculates and displays the total amount for cart1

# Performing operations on cart2
cart2.add_to_cart(product3, 5)  # Adds 5 Headphones to cart2
cart2.add_to_cart(product2, 3)  # Adds 3 Smartphones to cart2
cart2.remove_from_cart(product2)  # Removes Smartphones from cart2
cart2.display_cart()  # Displays the contents of cart2
print(f"Total amount due for cart2: {cart2.calculate_total()}")  # Calculates and displays the total amount for cart2
