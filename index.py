from flask import Flask
from api.CatApi import cat_api
from api.DogApi import dog_api

app = Flask(__name__)
app.register_blueprint(cat_api)
app.register_blueprint(dog_api)