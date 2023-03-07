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
