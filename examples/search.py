import techspecs
# Search Product

techspecs_key = ""
techspecs_base = ""
query = {
    'keyword': '',
    'category': '',
}
search = techspecs.search(techspecs_base, query, techspecs_key, mode='pretty')
print(search)
