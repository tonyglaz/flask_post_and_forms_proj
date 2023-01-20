import logging

from flask import Flask,send_from_directory

# from functions import ...
from main.main import main_blueprint
from loader.loader import loader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

logging.basicConfig(filename="basic.log", level=logging.INFO)
app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

@app.route("/uploads/images/<path:path>")
def static_dir(path):
    return send_from_directory("uploads/images",path)


app.run(debug=True)
