from collections import namedtuple
import requests


PagedResult = namedtuple('PagedResult', ['items', 'record_count'])

def make_http_get_request(url, params=None):
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f'An error occured while processing the get request to {url}', 
                        response.status_code)
    return response

def make_http_post_request(url, body):
    response = requests.post(url, body=body)
    if response.status_code != 200:
        raise Exception(f'An error occured while process the post request to {url}',
                        response.status_code)
    return response
