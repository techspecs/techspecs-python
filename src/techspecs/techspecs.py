import json
import requests


def search(techspecs_base, query: dict, key, mode='raw'):
    url = f'https://apis.dashboard.techspecs.io/{techspecs_base}/api/product/search?'
    header = {
        "Accept": "application/json",
        "x-blobr-key": key,
        "Content-Type": "application/json"
    }
    parameter = {'query': query['keyword'].replace(' ', '%20')}
    payload = {"category": query['category']}
    req = requests.post(url, params=parameter, json=payload, headers=header).json()
    if mode == 'raw':
        return req
    elif mode == 'pretty':
        try:
            mod_list = req['data']['results']
            return json.dumps(mod_list, indent=4)
        except:
            return req

    else:
        return 'Invalid Mode'


def detail(techspecs_base, techspecs_id, key, mode='raw'):
    url = f'https://apis.dashboard.techspecs.io/{techspecs_base}/api/product/get/'
    header = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "x-blobr-key": key
    }
    req = requests.get(url + techspecs_id, headers=header).json()
    if mode == 'raw':
        return req
    elif mode == 'pretty':
        try:
            mod_list = req['data']['product']
            modified_data = []
            for m in mod_list:
                mod_dict = {}
                for a, b in m.items():
                    try:
                        mod_dict[a] = b
                    except:
                        for x, y in b:
                            mod_dict[x] = y
                modified_data.append(mod_dict)
            return json.dumps(modified_data, indent=4)
        except:
            return req
    else:
        return 'Invalid Mode'


def brands(techspecs_base, key, mode='raw'):
    url = f'https://apis.dashboard.techspecs.io/{techspecs_base}/api/product/brands'
    header = {
        "Accept": "application/json",
        "x-blobr-key": key
    }
    req = requests.get(url, headers=header).json()
    if mode == 'raw':
        return req
    elif mode == 'pretty':
        try:
            mod_list = req['data']['brands']
            return json.dumps(mod_list, indent=4)
        except:
            return req
    else:
        return 'Invalid Mode'


def categories(techspecs_base, key, mode='raw'):
    url = f'https://apis.dashboard.techspecs.io/{techspecs_base}/api/category/getAll'
    header = {
        "Accept": "application/json",
        "x-blobr-key": key
    }
    req = requests.get(url, headers=header).json()
    if mode == 'raw':
        return req
    elif mode == 'pretty':
        try:
            mod_list = req['data']['Category']
            return json.dumps(mod_list[1], indent=4)
        except:
            return req
    else:
        return 'Invalid Mode'


def products(techspecs_base, brand: list, category: list, date: dict, page, key, mode='raw'):
    url = f"https://apis.dashboard.techspecs.io/{techspecs_base}/api/product/getAll?page=" + str(page)
    payload = {
        "brand": brand,
        "category": category,
        "from": date['from'],
        "to": date['to']
    }
    header = {
        "Accept": "application/json",
        "X-BLOBR-KEY": key,
        "Content-Type": "application/json"
    }
    req = requests.post(url, json=payload, headers=header).json()
    if mode == 'raw':
        return req
    elif mode == 'pretty':
        try:
            mod_list = req['data']['product']
            return json.dumps(mod_list, indent=4)
        except:
            return req
    else:
        return 'Invalid Mode'
