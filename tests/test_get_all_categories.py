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
