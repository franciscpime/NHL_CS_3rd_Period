from flask import Flask

vanity = Flask(__name__)

@vanity.route("/")
def index():
    return "Hello, World"