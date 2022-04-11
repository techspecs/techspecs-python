![TechSpecs Logo](https://i.imgur.com/JZ3GqAU.jpg)

# Introducing TechSpecs Python

This python library provides automatic access to the standardized technical specifications of the world's consumer electronics, including the latest smartphones, tablets, smartwatches, laptops, and more. 


## Documentation

-   See the [TechSpecs API Docs](https://techspecs.readme.io)

## API Key

-   Get an API key [here](https://developer.dashboard.techspecs.io/)


## Requirements

-   Python 3.6+


## Installation

```sh
pip install techspecs
```

## Usage

The library needs to be configured with your account's api key and base which is
available in your [TechSpecs Dashboard](https://developer.dashboard.techspecs.io/). 

Set `techspecs_key` to your key value and `techspecs_base` to your base value.

### Basic Search
#### Search for a device by specifying it's model name, version number or features 

```python
# Search for a product by name, version or features
import techspecs
import json

# TechSpecs API Key
techspecs_key = "techspecs_api_key"   

# TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
techspecs_base = 'a8TD3mkN49fhg2y'     

query = {
    'keyword': 'iPhone 13', # product name or version number to search 
    'category': 'all',      # product category to search
}

# choose between "pretty" or "raw" mode for viewing response
response = techspecs.search(base, query, key, mode='pretty') 

# print the search results
print(response)

```

### Advanced Search
#### List all products by brand, category and release date
```python
# List all products by brand, category and release date
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
```

### Apple Machine ID Search
#### Search for Apple products by machine id
```python
# Search for an Apple product by machine id
import techspecs

# TechSpecs API Key
techspecs_key = "techspecs_api_key"

# TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
techspecs_base = "a8TD3mkN49fhg2y"

# machine id to search
machine_id = "iphone8,3"

# choose between "pretty" or "raw" mode for viewing response
response = techspecs.apple_machine_id(techspecs_base, machine_id, techspecs_key, mode='pretty')

# print the specifications of the product
print(response)
```

### Product Details

```python
# Get the standardized specifications of a specified product
import techspecs

# TechSpecs API Key
techspecs_key = "techspecs_api_key"

# TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
techspecs_base = "a8TD3mkN49fhg2y"

# TechSpecs product id 
techspecs_id = "6186b047987cda5f88311983"           

# choose between "pretty" or "raw" mode for viewing response
response = techspecs.detail(techspecs_base, techspecs_id, techspecs_key, mode='pretty') 

# print the specifications of the product
print(response)

```

### List all brands
```python
import techspecs

# TechSpecs API Key
techspecs_key = "techspecs_api_key"          

# TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
techspecs_base = "a8TD3mkN49fhg2y"         

# choose between "pretty" or "raw" mode for viewing response
response = techspecs.brands(techspecs_base, techspecs_key, mode='pretty') 

# print the list of all brands
print(response)


```
### List all categories    
```python
import techspecs

# TechSpecs API Key
techspecs_key = "techspecs_api_key" 

# TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
techspecs_base = "a8TD3mkN49fhg2y"    

# choose between "pretty" or "raw" mode for viewing response
response = techspecs.categories(techspecs_base, techspecs_key, mode='pretty') 

# print the list of all categories
print(response)

```



