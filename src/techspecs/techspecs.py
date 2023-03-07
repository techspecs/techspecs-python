import json
import requests

def product_search(techspecs_base_url, query: dict, techspecs_api_key, mode='raw'):
    """
    Search for products that match the specified query.

    :param base_url: the base URL of the TechSpecs API
    :param query: a dictionary that contains the search query parameters
    :param bearer_token: the bearer token for API authentication
    :param mode: the output mode ('raw' or 'pretty')
    :return: the search results in the specified output mode
    """
    q = query["keyword"].strip()
    url = f'{techspecs_base_url}/v4/product/search?query={q}'
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {techspecs_api_key}",
        "Content-Type": "application/json"
    }
    payload = {"category": query['category'].strip()}
    response = requests.post(url, json=payload, headers=headers).json()
    if mode == 'raw':
        return response
    elif mode == 'pretty':
        try:
            mod_list = response['data']
            return json.dumps(mod_list, indent=4)
        except KeyError:
            return response
    else:
        return 'Invalid Mode'


def product_detail(techspecs_base_url, techspecs_product_id, techspecs_api_key, mode='raw'):
    """
    Get detailed information about a specific product.

    :param base_url: the base URL of the TechSpecs API
    :param product_id: the ID of the product to get information about
    :param bearer_token: the bearer token for API authentication
    :param mode: the output mode ('raw' or 'pretty')
    :return: the product information in the specified output mode
    """
    url = f'{techspecs_base_url}/v4/product/detail'
    params = {
        'productId': techspecs_product_id.strip()
    }
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {techspecs_api_key}",
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as error:
        return f"HTTP error occurred: {error}"
    except requests.exceptions.RequestException as error:
        return f"An error occurred: {error}"
    except ValueError as error:
        return f"Failed to decode JSON: {error}"
    
    if mode == 'raw':
        return data
    elif mode == 'pretty':
        try:
            mod_list = data['data']
            modified_data = []
            for m in mod_list:
                mod_dict = {}
                for a, b in m.items():
                    try:
                        mod_dict[a] = b
                    except TypeError:
                        for x, y in b:
                            mod_dict[x] = y
                modified_data.append(mod_dict)
            return json.dumps(modified_data, indent=4)
        except KeyError:
            return data
    else:
        return 'Invalid Mode'



def get_all_brands(techspecs_base_url, techspecs_api_key, mode='raw'):
    """
    Get a list of all brands.

    :param base_url: the base URL of the TechSpecs API
    :param bearer_token: the bearer token for API authentication
    :param mode: the output mode ('raw' or 'pretty')
    :return: the list of brands in the specified output mode
    """
    url = f'{techspecs_base_url}/v4/brand/all'
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {techspecs_api_key}"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as error:
        return f"HTTP error occurred: {error}"
    except requests.exceptions.RequestException as error:
        return f"An error occurred: {error}"
    except ValueError as error:
        return f"Failed to decode JSON: {error}"
    
    if mode == 'raw':
        return data
    elif mode == 'pretty':
        try:
            mod_list = data['data']
            return json.dumps(mod_list, indent=4)
        except KeyError:
            return data
    else:
        return 'Invalid Mode'



def get_all_categories(techspecs_base_url, techspecs_api_key, mode='raw'):
    """
    Get a list of all categories.

    :param base_url: the base URL of the TechSpecs API
    :param bearer_token: the bearer token for API authentication
    :param mode: the output mode ('raw' or 'pretty')
    :return: the list of categories in the specified output mode
    """
    url = f'{techspecs_base_url}/v4/category/all'
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {techspecs_api_key}"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as error:
        return f"HTTP error occurred: {error}"
    except requests.exceptions.RequestException as error:
        return f"An error occurred: {error}"
    except ValueError as error:
        return f"Failed to decode JSON: {error}"
    
    if mode == 'raw':
        return data
    elif mode == 'pretty':
        try:
            mod_list = data['data']
            return json.dumps(mod_list, indent=4)
        except KeyError:
            return data
    else:
        return 'Invalid Mode'



def get_all_products(techspecs_base_url, techspecs_api_key, brand=[], category=[], date={}, page=0, mode='raw'):
    """
    Get a list of products matching the specified criteria.

    :param base_url: the base URL of the TechSpecs API
    :param bearer_token: the bearer token for API authentication
    :param brand: a list of brand names to include in the search (default: [])
    :param category: a list of category names to include in the search (default: [])
    :param date: a dictionary containing 'from' and 'to' date strings to limit the search (default: {})
    :param page: the page number of the search results to retrieve (default: 0)
    :param mode: the output mode ('raw' or 'pretty')
    :return: the list of products in the specified output mode
    """
    url = f'{techspecs_base_url}/v4/product/all?page={page}'
    payload = {
        "brand": brand,
        "category": category,
        "from": date.get('from', ''),
        "to": date.get('to', '')
    }
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {techspecs_api_key}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as error:
        return f"HTTP error occurred: {error}"
    except requests.exceptions.RequestException as error:
        return f"An error occurred: {error}"
    except ValueError as error:
        return f"Failed to decode JSON: {error}"
    
    if mode == 'raw':
        return data
    elif mode == 'pretty':
        try:
            mod_list = data['data']
            return json.dumps(mod_list, indent=4)
        except KeyError:
            return data
    else:
        return 'Invalid Mode'




def get_all_brand_logos(techspecs_base_url, techspecs_api_key, mode='raw'):
    """
    Get a list of all brand logos.

    :param base_url: the base URL of the TechSpecs API
    :param bearer_token: the bearer token for API authentication
    :param mode: the output mode ('raw' or 'pretty')
    :return: the list of brand logos in the specified output mode
    """
    url = f'{techspecs_base_url}/v4/brandlogo/all'
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {techspecs_api_key}"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as error:
        return f"HTTP error occurred: {error}"
    except requests.exceptions.RequestException as error:
        return f"An error occurred: {error}"
    except ValueError as error:
        return f"Failed to decode JSON: {error}"
    
    if mode == 'raw':
        return data
    elif mode == 'pretty':
        try:
            mod_list = data['data']
            return json.dumps(mod_list, indent=4)
        except KeyError:
            return data
    else:
        return 'Invalid Mode'




def machine_id_search(techspecs_base_url, techspecs_api_key, machine_id, mode='raw'):
    """
    Look up a product by its machine ID or code name.

    :param base_url: the base URL of the TechSpecs API
    :param bearer_token: the bearer token for API authentication
    :param machine_id: the machine ID or code name of the product to look up
    :param mode: the output mode ('raw' or 'pretty')
    :return: the search results in the specified output mode
    """
    url = f'{techspecs_base_url}/v4/product/search/machineid?query={machine_id.strip()}'
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {techspecs_api_key}"
    }
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as error:
        return f"HTTP error occurred: {error}"
    except requests.exceptions.RequestException as error:
        return f"An error occurred: {error}"
    except ValueError as error:
        return f"Failed to decode JSON: {error}"
    
    if mode == 'raw':
        return data
    elif mode == 'pretty':
        return json.dumps(data, indent=4)
    else:
        return 'Invalid Mode'

