# Food City System

A console-based shop management system written in Python. This system allows shop owners (sellers) to manage inventory, update stock, and generate bills for customers.

## 🚀 Features

- **User Authentication:** Secure login for the seller section.
- **Billing System:** 
  - Add items to a bill.
  - Calculate total amounts.
  - Generate and print receipts.
- **Inventory Management:**
  - Add new products to the system.
  - Update stock quantities (add/remove stock).
  - Data is persistently stored in text files (`_product_price.txt`, `_product_quantity_list.txt`).
- **Interactive Console UI:** Simple text-based menus to navigate through the system.

## 📁 Project Structure

- `main.py`: The entry point of the application. Handles the main menu and authentication.
- `seller_section.py`: Contains the core logic for seller operations (billing, inventory management).
- `update_products.py`: Handles reading and writing product data (prices and quantities) to text files.
- `bill_print.py`: Responsible for formatting and printing the final bill/receipt.

## 🛠️ Prerequisites

- Python 3.x installed on your system.

## 🏃‍♂️ How to Run

1. Clone the repository or download the source code.
2. Open your terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command:
   ```bash
   python main.py
   ```

## 🔐 Default Credentials

To access the Seller Management System, use the following credentials when prompted:

- **Username:** `seller123`
- **Password:** `sel12345`

## 📋 Usage Guide

1. **Main Menu:** Upon starting, you can choose to enter the shop management system (Seller) or the customer section (currently a placeholder).
2. **Seller Menu:** After logging in, you can choose to:
   - **Type 1:** Create a new bill. Enter product names and quantities. Press `#` to calculate the total and print the bill.
   - **Type 2:** Add a new item to the inventory (requires product name, unit price, and initial quantity).
   - **Type 3:** Update the quantity of an existing item.
   - **Type 4:** Go back to the main menu.

## 🏗️ Software Engineering Principles Applied

This project demonstrates several core Software Engineering principles to maintain clean, readable, and scalable code:

- **Object-Oriented Programming (OOP):** The system uses classes (`SellerSection`, `Products`, `Bill`) to encapsulate data and behavior together.
- **Separation of Concerns (SoC):** The application logic is divided into distinct modules based on functionality:
  - `main.py` is responsible for routing and authentication.
  - `seller_section.py` manages seller-specific workflows.
  - `update_products.py` acts as the data access layer handling file I/O operations.
  - `bill_print.py` handles the presentation logic of generating receipts.
- **Single Responsibility Principle (SRP):** Each class has one primary responsibility. For example, the `Bill` class focuses solely on calculating totals and formatting the print output without worrying about how products are saved to the database.
- **Modularity:** By splitting the code across multiple files, the codebase is easier to maintain, debug, and expand in the future.

## 📝 Note

This project uses basic text files (`.txt`) as a database to store product prices and quantities. Ensure these files are in the same directory as the scripts and have read/write permissions.
