from flask import Flask 
from flask_cors import CORS 

app = Flask(__name__)

CORS(app, resources={r"/api/news":{
    "origins": ["https://sevinc995.github.io"],
    "methods": ["GET"]
}})
