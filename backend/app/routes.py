from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return {"message": "Welcome to the Backend!"}
