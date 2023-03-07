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
