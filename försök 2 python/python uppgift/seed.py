import json
from app import db, MenuItem

with open('menu_items.json') as f:
    menu_items = json.load(f)

for item in menu_items:
    name = item['name']
    description = item['description']
    price = item['price']
    new_item = MenuItem(name=name, description=description, price=price)
    db.session.add(new_item)

db.session.commit()
