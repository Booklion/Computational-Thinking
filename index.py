from flask import Flask
from api.CatApi import cat_api

app = Flask(__name__)
app.register_blueprint(cat_api)