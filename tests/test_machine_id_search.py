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
