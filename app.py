from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'some_secret_key'
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': None}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': 'An item with name '{}' already exists.'.format(name)}

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}

@app.route('/')
def home():
    return 'Hello world'

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')  

app.run(port=5000)