from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "ece0f5241f0eb4ff5a78633379b8cc13e9c8a4366252dd3a17d54b04b97fabba"
