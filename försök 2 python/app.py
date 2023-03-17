from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)

@app.route('/')
def home():
    return 'Welcome to the Menu API!'

@app.route('/menu', methods=['GET'])
def get_menu_items():
    menu_items = MenuItem.query.all()
    output = []
    for item in menu_items:
        item_data = {'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price}
        output.append(item_data)
    return jsonify({'menu_items': output})

@app.route('/menu/<id>', methods=['GET'])
def get_menu_item(id):
    item = MenuItem.query.get(id)
    if not item:
        return jsonify({'message': 'Item not found'})
    item_data = {'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price}
    return jsonify({'menu_item': item_data})

@app.route('/menu', methods=['POST'])
def add_menu_item():
    data = request.get_json()
    new_item = MenuItem(name=data['name'], description=data['description'], price=data['price'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'New menu item added!'})

@app.route('/menu/<id>', methods=['PUT'])
def update_menu_item(id):
    item = MenuItem.query.get(id)
    if not item:
        return jsonify({'message': 'Item not found'})
    data = request.get_json()
    item.name = data['name']
    item.description = data['description']
    item.price = data['price']
    db.session.commit()
    return jsonify({'message': 'Menu item updated!'})

@app.route('/menu/<id>', methods=['DELETE'])
def delete_menu_item(id):
    item = MenuItem.query.get(id)
    if not item:
        return jsonify({'message': 'Item not found'})
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Menu item deleted!'})
