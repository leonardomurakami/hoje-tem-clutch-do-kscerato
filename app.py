from flask import Flask
from src.layout import create_root

app = Flask(__name__, static_folder="static", template_folder="templates")

create_root(app)