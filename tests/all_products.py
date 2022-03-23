import techspecs
# All Products By Brand And Category

techspecs_key = ""
techspecs_base = ""
page = 1
brand = [""]
category = [""]
time = {
    "from": "2010-01-01", # YYYY-MM-DD
    "to": "2022-03-15"    # YYYY-MM-DD
}
all_products = techspecs.products(techspecs_base, brand, category, time, page, techspecs_key, mode='pretty')
print(all_products)
