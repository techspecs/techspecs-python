import techspecs

# TechSpecs API Key
techspecs_key = "techspecs_api_key"          

# TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
techspecs_base = "a8TD3mkN49fhg2y"         

# choose between "pretty" or "raw" mode for viewing response
brands = techspecs.brands(techspecs_base, techspecs_key, mode='pretty') 

# print the search results
print(brands)

