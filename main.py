from user_module import User
from admin_module import Admin

class ShoppingApp:
    def __init__(self):
        self.user = User()
        self.admin = Admin()
    
    def main_menu(self):
        session_id = None
        while True:
            print("\nWelcome to Demo Marketplace!")
            print("1. Login\n2. View Products\n3. Add to Cart\n4. Remove Product from Cart\n5. View Cart\n6. Checkout\n7. Admin Panel\n8. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                session_id = self.user.login()
            elif choice == "2":
                self.user.view_products()
            elif choice == "3":
                self.user.add_to_cart(session_id)
            elif choice == "4":
                self.user.remove_from_cart(session_id)
            elif choice == "5":
                self.user.view_cart(session_id)
            elif choice == "6":
                self.user.checkout(session_id)
            elif choice == "7":
                self.admin.admin_panel(session_id)
            elif choice == "8":
                print("Exiting Application.")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    app = ShoppingApp()
    app.main_menu()