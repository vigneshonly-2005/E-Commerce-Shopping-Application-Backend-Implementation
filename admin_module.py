class Admin:
    def __init__(self):
        self.admins = {"admin": "adminpass"}
    
    def admin_panel(self, session_id):
        if session_id:
            print("\nAdmin Panel:")
            print("1. Add Product\n2. Remove Product\n3. Logout")
            input("Enter choice: ")
            print("\nAdmin action executed.")
        else:
            print("\nAccess Denied.")