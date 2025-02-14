# E-Commerce Shopping Application (Backend-Only)

## Overview
This is a backend-only implementation of an e-commerce shopping application built using Python. The system allows user and admin authentication, product management, a shopping cart system, and payment processing.

## Features
### User Features
- **User Registration**: Users can create an account with a unique username and password.
- **User Login**: Secure login with credential verification.
- **Logout**: Users can log out anytime.
- **View Products**: Browse available products in different categories.
- **Add to Cart**: Add items to the shopping cart.
- **Remove from Cart**: Remove selected items from the cart.
- **View Cart**: Display items in the cart along with the total price.
- **Generate Bill**: View an itemized bill before checkout.
- **Checkout & Payment**:
  - UPI (Online Transaction)
  - Credit/Debit Card
  - Cash on Delivery (COD)
  
### Admin Features
- **Admin Login**: Secure login for the admin using predefined credentials.
- **View Products**: Check the list of available products.
- **Add Products**: Add new products to the inventory.
- **Remove Products**: Delete existing products from the inventory.
- **View Registered Users**: Display a list of registered users.
- **Logout**: Secure logout for admin users.

## Installation & Setup
### Prerequisites
- Python 3.x installed on your system.
- A terminal or command prompt to run the script.

### Steps to Run
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your-username/ecommerce-shopping-app.git
   cd ecommerce-shopping-app
   ```
2. **Run the Application:**
   ```sh
   python main.py
   ```
3. **Login Options:**
   - If you are a **new user**, register first.
   - If you are an **existing user**, log in with your credentials.
   - If you are an **admin**, use:
     ```
     Username: admin
     Password: admin@123
     ```

## Usage
- After logging in as a user, you can browse products, add/remove items from your cart, and proceed to checkout.
- If logged in as an admin, you can manage the product inventory and view registered users.
- Users can log out anytime to end the session.

## File Structure
```
Ecommerce-Shopping-App/
│-- main.py                # Entry point for the application
│-- user.py                # User-related functions (register, login, cart management)
│-- admin.py               # Admin functionalities (product & user management)
│-- products.py            # Product catalog & operations
│-- cart.py                # Shopping cart system
│-- payments.py            # Payment processing
│-- README.md              # Project documentation
```

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is open-source and available under the [MIT License](LICENSE).


