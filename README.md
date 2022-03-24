![TechSpecs Logo](https://i.imgur.com/gqI6LJW.jpg)



# TechSpecs Python

This python library provides access to the standardized technical specifications of the world's consumer electronics, including smartphones, tablets, smartwatches, laptops, and more. 

## Documentation

-   See the [TechSpecs API Docs](https://techspecs.readme.io)

## API Key

-   Get a TechSpecs [API Key](https://developer.dashboard.techspecs.io/)


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

### Product Search

```python
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

```

### Product Details

```python
import techspecs
# Product Details

# TechSpecs API Key
techspecs_key = "techspecs_api_key"

# TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
techspecs_base = "a8TD3mkN49fhg2y"

# TechSpecs product id 
techspecs_id = "6186b047987cda5f88311983"           

# choose between "pretty" or "raw" mode for viewing response
details = techspecs.detail(techspecs_base, techspecs_id, techspecs_key, mode='pretty') 

# print the specifications of the product
print(details)

```

### List all brands
```python
import techspecs

# TechSpecs API Key
techspecs_key = "techspecs_api_key"          

# TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
techspecs_base = "a8TD3mkN49fhg2y"         

# choose between "pretty" or "raw" mode for viewing response
brands = techspecs.brands(techspecs_base, techspecs_key, mode='pretty') 

# print the list of all brands
print(brands)


```
### List all categories    
```python
import techspecs

# TechSpecs API Key
techspecs_key = "techspecs_api_key" 

# TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
techspecs_base = "a8TD3mkN49fhg2y"    

# choose between "pretty" or "raw" mode for viewing response
categories = techspecs.categories(techspecs_base, techspecs_key, mode='pretty') 

# print the list of all categories
print(categories)

```
### List all products by brand, category and release date
```python
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
all_products = techspecs.products(techspecs_base, brand, category, date, page, techspecs_key, mode='pretty') 

# print the search results
print(all_products)
```


