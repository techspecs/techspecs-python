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
