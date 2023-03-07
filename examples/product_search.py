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
