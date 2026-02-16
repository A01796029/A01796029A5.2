# Ejercicio 2 - Products and Sales Data Loader

![Flake8](https://github.com/A01796029/A01796029A5.2/actions/workflows/flake8.yml/badge.svg)

This project provides a command-line interface to load and manage product and sales data from JSON files.

## Project Structure

```
/
├── src/
│   └── main.py          # Main application file
├── A5.2 Archivos de Apoyo/
│   ├── TC1/
│   │   ├── TC1.ProductList.json
│   │   └── TC1.Sales.json
│   ├── TC2/
│   │   └── TC2.Sales.json
│   └── TC3/
│       └── TC3.Sales.json
└── README               # This file
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Classes

The application includes three main classes:

- **Product**: Represents a product with attributes like title, type, description, price, rating, etc.
- **Sale**: Represents a sale transaction with sale ID, date, product name, and quantity.
- **DataManager**: Manages the loading and storage of products and sales data.

## Usage

### Basic Usage

Run the program from the command line by providing the paths to the products and sales JSON files:

```bash
python src/main.py <products_file_path> <sales_file_path>
```

### Example

To load data from Test Case 1:

```bash
python src/main.py "A5.2 Archivos de Apoyo/TC1/TC1.ProductList.json" "A5.2 Archivos de Apoyo/TC1/TC1.Sales.json"
```

### Help

To see all available options and usage information:

```bash
python src/main.py --help
```

## Output

The program will:
1. Load products from the specified JSON file
2. Load sales from the specified JSON file
3. Display a summary showing the total number of products and sales loaded

Example output:
```
✓ Loaded 50 products from TC1.ProductList.json
✓ Loaded 100 sales from TC1.Sales.json

--- Data Summary ---
Total Products: 50
Total Sales: 100
-------------------
```

## Error Handling

The application handles common errors:
- **FileNotFoundError**: If the specified files don't exist
- **JSONDecodeError**: If the JSON files are malformed
- **KeyError**: If required fields are missing from the JSON data

## Author

Santiago
