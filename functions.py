import json

POST_PATH = "posts.json"


def load_posts():
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts
