import logging

from flask import Flask

# from functions import ...
from main.main import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

logging.basicConfig(filename="basic.log", level=logging.INFO)
app = Flask(__name__)
app.register_blueprint(main_blueprint)

# @app.route("/")
# def page_index():
#     pass
#
#
# @app.route("/tag")
# def page_tag():
#     pass
#
#
# @app.route("/post", methods=["GET", "POST"])
# def page_post_create():
#     pass
#
#
# @app.route("/uploads/<path:path>")
# def static_dir(path):
#     return send_from_directory("uploads", path)


app.run(debug=True)
