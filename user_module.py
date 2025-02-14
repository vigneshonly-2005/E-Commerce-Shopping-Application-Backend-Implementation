import random

class User:
    def __init__(self):
        self.users = {"user1": "password1", "user2": "password2"}
        self.sessions = {}
        self.products = {
            "P101": {"name": "Nike Shoes", "category": "Footwear", "price": 3000},
            "P102": {"name": "Adidas T-Shirt", "category": "Clothing", "price": 1500},
            "P103": {"name": "JBL Headphones", "category": "Electronics", "price": 2500},
            "P104": {"name": "Leather Jacket", "category": "Clothing", "price": 5000},
        }
        self.carts = {}
    
    def login(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if username in self.users and self.users[username] == password:
            session_id = random.randint(1000, 9999)
            self.sessions[session_id] = {"role": "user", "username": username}
            print(f"\nUser '{username}' logged in successfully. Session ID: {session_id}")
            return session_id
        else:
            print("\nInvalid username or password.")
            return None
    
    def view_products(self):
        print("\nAvailable Products:")
        for pid, details in self.products.items():
            print(f"{pid} - {details['name']} ({details['category']}) - Rs. {details['price']}")
    
    def add_to_cart(self, session_id):
        if session_id:
            product_id = input("Enter Product ID: ")
            quantity = int(input("Enter Quantity: "))
            if session_id not in self.carts:
                self.carts[session_id] = {}
            self.carts[session_id][product_id] = self.carts[session_id].get(product_id, 0) + quantity
            print(f"\n{quantity} x {self.products[product_id]['name']} added to cart.")
        else:
            print("Login required.")
    
    def remove_from_cart(self, session_id):
        if session_id in self.carts:
            product_id = input("Enter Product ID to remove: ")
            if product_id in self.carts[session_id]:
                del self.carts[session_id][product_id]
                print("\nItem removed from cart.")
            else:
                print("\nItem not found in cart.")
    
    def view_cart(self, session_id):
        if session_id in self.carts and self.carts[session_id]:
            print("\nYour Cart:")
            total = 0
            for pid, qty in self.carts[session_id].items():
                item_total = self.products[pid]['price'] * qty
                total += item_total
                print(f"{self.products[pid]['name']} x {qty} = Rs. {item_total}")
            print(f"Total Amount: Rs. {total}")
        else:
            print("\nYour cart is empty.")
    
    def checkout(self, session_id):
        if session_id in self.carts and self.carts[session_id]:
            self.view_cart(session_id)
            print("\nChoose Payment Method: 1. UPI 2. Debit Card 3. Net Banking")
            input("Enter choice: ")
            print("\nYour order has been placed successfully!")
            self.carts[session_id] = {}
        else:
            print("\nYour cart is empty. Add items before checkout.")