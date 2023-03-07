<p align="center">
  <img src="https://techspecs.io/big-logo-light.svg" alt="TechSpecs Logo" width="200" height="200">
</p>

TechSpecs Python provides automatic access to the standardized technical specifications of the world's consumer electronics, including the latest smartphones, tablets, smartwatches, laptops, and more. 

# Database Stats

At TechSpecs, we are committed to providing the most comprehensive and up-to-date database of technical specifications for consumer electronics products. Here are some statistics on our current database:

Total number of products: 100,000+
-   Brands: 400+
-   Categories: 6 (Smartphones, Tablets, Smartwatches, Monitors, TVs, and Laptops)
-   Technical specifications: Over 300 for each product, including dimensions, weight, display features, connectivity options, and more.
-   Daily updates: We update our database on a daily basis to ensure that our API provides the most accurate and up-to-date technical specifications for the products you're interested in.

We take pride in providing a database that is comprehensive and reliable, and we are constantly working to expand and improve it. If you have any questions or issues, please don't hesitate to reach out to our support team for assistance.

## API Key

-   [Signup](https://techspecs.io/) to get your TechSpecs API Key

## Requirements

-   Python 3.6+


## Installation

```sh
pip install techspecs
```

## Usage

The library needs to be configured with your TechSpecs api key and base URL which is
available in your [TechSpecs Dashboard](https://techspecs.io/dashboard). 

Set `techspecs_api_key` to your key value and `techspecs_base_url` to your base value.

### Product Search

```python
# Search for a product by name, version or features
import techspecs
import json

# TechSpecs API base URL
techspecs_base_url = "https://api.techspecs.io"

# TechSpecs API bearer token
techspecs_api_key = "your_techspecs_api_key"

query = {
    'keyword': 'iPhone 13', # product name or version number to search 
    'category': '',      # product category to search (e.g. 'Smartphones', 'Tablets', or leave empty to search all categories)
    'page': 0                # page number to fetch results from
}

# Output mode ('raw' or 'pretty')
mode = 'pretty'

# Search for a product by name, version, or features
try:
    response = techspecs.product_search(techspecs_base_url, query, techspecs_api_key, mode=mode)
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")


```


### Product Details

```python
# Get the detailed specifications of a product
import techspecs

# TechSpecs API base URL
techspecs_base_url = "https://api.techspecs.io"

# TechSpecs API bearer token
techspecs_api_key = "your_techspecs_api_key"

# TechSpecs product ID
techspecs_product_id = "63e96260ff7af4b68a304e40"

# Query dictionary
query = {
    "productId": techspecs_product_id
}

# Output mode ('raw' or 'pretty')
mode = 'pretty'

try:
    # Validate techspecs_product_id
    if not isinstance(techspecs_product_id, str):
        raise ValueError('TechSpecs Product ID should be a string.')

    # Validate mode
    if mode not in ['raw', 'pretty']:
        raise ValueError('Invalid mode. Mode should be "raw" or "pretty".')

    # Call TechSpecs API to get product details
    response = techspecs.product_detail(techspecs_base_url, techspecs_product_id, techspecs_api_key, mode=mode)

    # Print the product details
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")


```


### List all categories    
```python
import techspecs

# TechSpecs API base URL
techspecs_base_url = "https://api.techspecs.io"

# TechSpecs API bearer token
techspecs_api_key = "your_techspecs_api_key"

# Output mode ('raw' or 'pretty')
mode = 'pretty'

# Define constants
DEFAULT_MODE = 'pretty'
VALID_MODES = ['pretty', 'raw']

# Validate parameters
def validate_parameters(mode=DEFAULT_MODE):
    if mode not in VALID_MODES:
        raise ValueError(f'Invalid mode: {mode}. Mode should be one of {VALID_MODES}.')

# Validate search parameters
try:
    validate_parameters(mode=mode)
except ValueError as e:
    print(f"Invalid search parameters: {e}")
    exit()

# Call TechSpecs API to get all categories
try:
    response = techspecs.get_all_categories(techspecs_base_url, techspecs_api_key, mode=mode)
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")


```


### List all brands
```python
import techspecs

# TechSpecs API base URL
techspecs_base_url = "https://api.techspecs.io"

# TechSpecs API bearer token
techspecs_api_key = "your_techspecs_api_key"

# Output mode ('raw' or 'pretty')
mode = 'pretty'

# Define function to validate parameters
def validate_parameters(mode):
    if mode not in ['raw', 'pretty']:
        raise ValueError(f'Invalid mode: {mode}. Mode should be one of ["raw", "pretty"].')

# Validate parameters
try:
    validate_parameters(mode)
except ValueError as e:
    print(f"Invalid parameters: {e}")
    exit()

# Call TechSpecs API to get all brands
try:
    response = techspecs.get_all_brands(techspecs_base_url, techspecs_api_key, mode=mode)
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")


```


### Advanced Search
```python
# List all products by brand, category and release date
import techspecs
import datetime

# TechSpecs API base URL
techspecs_base_url = "https://api.techspecs.io"

# TechSpecs API bearer token
techspecs_api_key = "your_techspecs_api_key"

# Output mode ('raw' or 'pretty')
mode = 'pretty'

# Set constants
DEFAULT_PAGE = 0
DEFAULT_MODE = 'pretty'
VALID_MODES = ['pretty', 'raw']

# Define function to validate date format
def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Define function to validate parameters
def validate_parameters(brand, category, date=None, page=DEFAULT_PAGE, mode=DEFAULT_MODE):
    if not isinstance(brand, list):
        raise ValueError('Brand should be a list.')
    
    if not isinstance(category, list):
        raise ValueError('Category should be a list.')
    
    if date is not None:
        if not isinstance(date, dict):
            raise ValueError('Invalid date format. Date should be a dictionary with keys "from" and "to".')
        elif 'from' not in date or 'to' not in date:
            raise ValueError('Invalid date format. Date dictionary should have keys "from" and "to".')
        elif not is_valid_date(date['from']) or not is_valid_date(date['to']):
            raise ValueError('Invalid date format. Date should be in the format YYYY-MM-DD.')
    
    if not isinstance(page, int) or page < 0:
        raise ValueError('Page should be a non-negative integer.')
    
    if mode not in VALID_MODES:
        raise ValueError(f'Invalid mode: {mode}. Mode should be one of {VALID_MODES}.')

# Define search parameters
brand = ["Apple"]
category = ["Smartphones"]
date = {
    "from": "2010-01-01",
    "to": "2022-03-15"
}
page = 0

# Validate search parameters
try:
    validate_parameters(brand, category, date=date, page=page, mode=mode)
except ValueError as e:
    print(f"Invalid search parameters: {e}")
    exit()


# Call TechSpecs API to get all products
try:
    response = techspecs.get_all_products(techspecs_base_url, techspecs_api_key, brand, category, date, page, mode=mode)
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")


```


### Machine ID Search
#### Search for Apple products by machine id
```python
# Search for an Apple product by machine id
import techspecs

# TechSpecs API base URL
techspecs_base_url = "https://api.techspecs.io"

# TechSpecs API bearer token
techspecs_api_key = "your_techspecs_api_key"

# Serial number of the Apple machine to look up machineid_or_codename ex iphone 11,6
machine_id = "iphone 11,6"

# Output mode ('raw' or 'pretty')
mode = 'pretty'

# Look up the Apple machine by its serial number
try:
    response = techspecs.machine_id_search(techspecs_base_url, techspecs_api_key, machine_id, mode)
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")


```



