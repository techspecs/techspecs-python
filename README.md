![TechSpecs Logo](https://i.imgur.com/3sfBN8c.jpg)



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

The library needs to be configured with your account's api key which is
available in your [TechSpecs Dashboard](https://developer.dashboard.techspecs.io/). Set `techspecs_key` to its
value.

### Product Search

```python
import techspecs
import json


key = "techspecs_api_key"   # TechSpecs API Key

# Search Product
base = 'techspecs_base'     # TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
query = {
    'keyword': 'iphone 13', # Product name or version number to search
    'category': 'all',      # Product category to search
}
search = techspecs.search(base, query, key, mode='pretty') # Choose between "pretty" or "raw" mode for viewing response.
print(search)

```

### Product Details

```python
import techspecs
# Product Details

techspecs_key = ""          # TechSpecs API Key
techspecs_base = ""         # TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
techspecs_id = ""           # TechSpecs product id 

details = techspecs.detail(techspecs_base, techspecs_id, techspecs_key, mode='pretty') # Choose between "pretty" or "raw" mode for viewing response.
print(details)

```

### List all brands
```python
import techspecs
# returns a list of all brands

techspecs_key = ""          # TechSpecs API Key
techspecs_base = ""         # TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
brands = techspecs.brands(techspecs_base, techspecs_key, mode='pretty') # Choose between "pretty" or "raw" mode for viewing response.
print(brands)


```
### List all categories    
```python
import techspecs
# returns a list of all categories

techspecs_key = ""          # TechSpecs API Key
techspecs_base = ""         # TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
categories = techspecs.categories(techspecs_base, techspecs_key, mode='pretty') # Choose between "pretty" or "raw" mode for viewing response.
print(categories)

```
### List all products by brand, category and release date
```python
import techspecs
# returns a list of all products by brand, category and release date

techspecs_key = ""      # TechSpecs API Key
techspecs_base = ""     # TechSpecs base https://apis.dashboard.techspecs.io/{techspecs_base}
page = 1                # Enter the page number to fetch results from
brand = [""]            # Type in the name of the brand you're looking for or leave this field empty to see results from all brands
category = [""]         # Type in the name of the category you're looking for or leave this field empty to see results from all categories
date = {                # Please provide a date range to narrow your search. Leave this field empty to fetch all results from all dates.
    "from": "2010-01-01",   # From release date: to fetch results from YYYY-MM-DD
    "to": "2022-03-15"      # To release date: to fetch results from YYYY-MM-DD
}
all_products = techspecs.products(techspecs_base, brand, category, date, page, techspecs_key, mode='pretty') # Choose between "pretty" or "raw" mode for viewing response.
print(all_products)
```


