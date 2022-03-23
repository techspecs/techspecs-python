import techspecs
import json

# TechSpecs API Key
key = "techspecs_api_key"   

# TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
base = 'a8TD3mkN49fhg2y'     

query = {
    'keyword': 'iPhone 13', # product name or version number to search 
    'category': 'all',      # product category to search
}

# choose between "pretty" or "raw" mode for viewing response
search = techspecs.search(base, query, key, mode='pretty') 

# print the search results
print(search)
