from flask import Blueprint, render_template, request
from functions import load_posts, upload_posts
import logging

logging.basicConfig(filename="basic.log",encoding='utf-8',level=logging.INFO)

loader_blueprint = Blueprint('loader', __name__, template_folder='templates', url_prefix='/post')


@loader_blueprint.route('/form/', )
def form():
    return render_template('post_form.html')


@loader_blueprint.route('/upload/', methods=["POST"])
def upload():
    try:
        file = request.files['picture']
        filename = file.filename
        content = request.values['content']
        posts = load_posts()
        posts.append({
            'pic': f'/uploads/images/{filename}',
            'content': content,
        })
        upload_posts(posts)
        file.save(f"uploads/images/{filename}")
        if filename.split('.')[-1] not in ['png','jpeg','jpg']:
            logging.info('Файл не изображение')
    except FileNotFoundError:
        logging.error("Ошибка при загрузке файла")
        return "<h1> File not found </h1>"
    else:
        return render_template("post_uploaded.html", pic=f'/uploads/images/{filename}',content=content)
