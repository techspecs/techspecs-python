![image info](https://www.techspecs.io/big-logo-light.svg)

# TechSpecs Python Library

TechSpecs provides access to standardized technical specifications of the world's consumer electronics, including smartphones, tablets, smartwatches, laptops, and more. This library makes it easy to search and quickly get the specs of any device you are interested in.

## Documentation

See the [TechSpecs API docs](https://techspecs.readme.io).

### API Key

Get a TechSpecs [API Key](https://developer.dashboard.techspecs.io/)


## Installation

```sh
pip install techspecs
```

### Requirements

-   Python 2.7+ or Python 3.4+ (PyPy supported)

## Usage

The library needs to be configured with your account's api key which is
available in your [TechSpecs Dashboard][api-keys]. Set `stripe.api_key` to its
value:

### Product Search

```python
import techspecs
import json


key = "techspecs_api_key" #Enter your TechSpecs API Key here

# Search Product
base = 'techspecs_base'   # Enter your TechSpecs base here
query = {
    'keyword': 'iphone 13',
    'category': 'smartphone',
}
search = techspecs.search(base, query, key, mode='pretty')
print(search)

```

### Product Details

```python
import techspecs
# Product Details

techspecs_key = ""
techspecs_base = ""
techspecs_id = ""

details = techspecs.detail(techspecs_base, techspecs_id, techspecs_key, mode='pretty')
print(details)

```

### List all brands
```python
import techspecs
# All brands

techspecs_key = ""
techspecs_base = ""
brands = techspecs.brands(techspecs_base, techspecs_key, mode='pretty')
print(brands)


```
### list all categories
```python
import techspecs
# All Categories

techspecs_key = ""
techspecs_base = ""
categories = techspecs.categories(techspecs_base, techspecs_key, mode='pretty')
print(categories)

```
### List all products by brand, category and release date
```python
import techspecs
# All Products By Brand And Category

techspecs_key = ""
techspecs_base = ""
page = 1
brand = [""]
category = [""]
date = {
    "from": "2010-01-01",
    "to": "2022-03-15"
}
all_products = techspecs.products(techspecs_base, brand, category, date, page, techspecs_key, mode='pretty')
print(all_products)
```


