from flask import Blueprint

sample_blueprint = Blueprint('sample_blueprint', __name__)

@sample_blueprint.route('/')
def index():
    return "Hello World!"

