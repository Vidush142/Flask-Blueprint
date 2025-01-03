from flask import Flask
from sample_blueprint import sample_blueprint

app = Flask(__name__)
app.register_blueprint(sample_blueprint)