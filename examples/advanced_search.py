import techspecs

# TechSpecs API Key
techspecs_key = "techspecs_api_key"     

# TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
techspecs_base = "a8TD3mkN49fhg2y"     

# enter the page number to fetch results from
page = 1    

# type in the name of the brand you're looking for or leave this field empty to see results from all brands
brand = ["Apple"]            

# type in the name of the category you're looking for or leave this field empty to see results from all categories
category = ["smartphone"] 

# please provide a date range to narrow your search. Leave this field empty to fetch all results from all dates
date = {                
    "from": "2010-01-01",   # YYYY-MM-DD
    "to": "2022-03-15"      # YYYY-MM-DD
}

# choose between "pretty" or "raw" mode for viewing response
response = techspecs.products(techspecs_base, brand, category, date, page, techspecs_key, mode='pretty') 

# print the search results
print(response)
