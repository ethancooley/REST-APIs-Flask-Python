from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = [
    {
        
    }
]

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}

@app.route('/')
def home():
    return 'Hello world'

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')  

app.run(port=5000)