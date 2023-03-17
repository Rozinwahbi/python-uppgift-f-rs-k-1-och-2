import requests

BASE_URL = 'http://localhost:5000'

def get_menu_items():
    response = requests.get(f'{BASE_URL}/menu')
    if response.status_code == 200:
        return response.json()
    else:
        return []

def add_menu_item(name, description, price):
    data = {'name': name, 'description': description, 'price': price}
    response = requests.post(f'{BASE_URL}/menu', json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def update_menu_item(id, name, description, price):
    data = {'name': name, 'description': description, 'price': price}
    response = requests.put(f'{BASE_URL}/menu/{id}', json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def delete_menu_item(id):
    response = requests.delete(f'{BASE_URL}/menu/{id}')
    if response.status_code == 200:
        return True
    else:
        return False
