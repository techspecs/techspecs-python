import techspecs

# TechSpecs API base URL
techspecs_base_url = "https://api.techspecs.io"

# TechSpecs API bearer token
techspecs_api_key = "your_techspecs_api_key"

# Output mode ('raw' or 'pretty')
mode = 'pretty'

# Call TechSpecs API to get all brand logos
try:
    response = techspecs.get_all_brand_logos(techspecs_base_url, techspecs_api_key, mode=mode)
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")
