import requests
import configuration 
import data 

def create_order():
    url = configuration.BASE_URL + configuration.CREATE_ORDER_ENDPOINT
    order_data = data.body
    response = requests.post(url, json=order_data, headers = data.headers)
    return response

def get_order_by_track(track_number):
    url = configuration.BASE_URL + configuration.GET_ORDER_ENDPOINT
    params = {'t': track_number}
    response = requests.get(url, params=params, headers = data.headers)
    return response