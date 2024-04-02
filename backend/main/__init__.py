from flask import Flask
from dotenv import load_dotenv


def creat_app():
    app = Flask(__name__)
    load_dotenv()

    return app