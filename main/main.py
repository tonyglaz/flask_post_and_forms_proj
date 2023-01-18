from flask import Blueprint, render_template, request
from functions import load_posts

main_blueprint = Blueprint('main', __name__, template_folder='templates',url_prefix='/main')


@main_blueprint.route('/', )
def main():
    return render_template('index.html')


@main_blueprint.route('/search/',)
def search():
    search_by = request.args['s']
    posts = [post for post in load_posts() if search_by.lower() in post['content'].lower()]
    return render_template("post_list.html", search_by=search_by, posts=posts)


# @main_blueprint.route('/kek/',)
# def kek():
#     return '<h2> its a kek </h2>'
