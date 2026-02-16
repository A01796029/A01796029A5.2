import json
import argparse
import time
from pathlib import Path
from typing import List
from models.product import Product
from models.sale import Sale


class DataManager:
    """Class to manage products and sales data"""

    def __init__(self):
        self.products: List[Product] = []
        self.sales: List[Sale] = []

    def load_products(self, filepath: str) -> None:
        """Load products from JSON file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.products = [Product.from_dict(item) for item in data]
        print(f"Loaded {len(self.products)}"
              f"products from {Path(filepath).name}")

    def get_product_by_title(self, title: str) -> Product:
        """Get a product by its title"""
        for product in self.products:
            if product.title == title:
                return product
        raise ValueError(f"Product with title '{title}' not found")

    def load_sales(self, filepath: str) -> None:
        """Load sales from JSON file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.sales = [Sale.from_dict(item) for item in data]
        print(f"Loaded {len(self.sales)} sales from {Path(filepath).name}")

    def get_summary(self) -> str:
        """Get a summary of loaded data"""
        return (f"\n--- Data Summary ---\n"
                f"Total Products: {len(self.products)}\n"
                f"Total Sales: {len(self.sales)}\n"
                f"-------------------")


def save_to_file(results, input_path, output_path):
    """Write the results in a text file"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"=== Results for: {input_path} ===\n")
            f.write(f"{results}\n")
            f.write("-" * 40 + "\n")
        print("File saved successfully!")
    except IOError as e:
        print(f"Failed to save file: {e}")


def main():
    """Main function to run the CLI"""
    start_time = time.time()
    parser = argparse.ArgumentParser(
        description='Load and manage products and sales data from JSON files'
    )
    parser.add_argument(
        'products_file',
        type=str,
        help='Path to the products JSON file (e.g., TC1.ProductList.json)'
    )
    parser.add_argument(
        'sales_file',
        type=str,
        help='Path to the sales JSON file (e.g., TC1.Sales.json)'
    )

    args = parser.parse_args()

    # Create data manager instance
    manager = DataManager()

    # Load data from files
    try:
        manager.load_products(args.products_file)
        manager.load_sales(args.sales_file)

        # Display summary
        print(manager.get_summary())
        sales_total = 0
        for sale in manager.sales:
            try:
                product = manager.get_product_by_title(sale.product)
                sales_total += product.price * sale.quantity
            except ValueError as e:
                print(f"Warning: {e}")
        output = f"Total Sales Revenue: ${sales_total:.2f}"
        end_time = time.time()
        output += "\nTotal Execution Time:"
        output += f" {end_time - start_time:.2f} seconds"
        print(output)
        save_to_file(output, args.sales_file, "results.txt")

    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
    except KeyError as e:
        print(f"Error: Missing required field - {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
