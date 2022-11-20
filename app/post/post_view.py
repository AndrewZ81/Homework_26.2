from flask import Blueprint, render_template  # Подключаем для создания блюпринтов на основе шаблонов
from .dao.post_dao import PostDAO  # Подключаем для выборки конкретного поста и комментариев к нему
from config import FlaskConfig  # Подключаем для доступа к конфигурационным константам

post_with_comments = PostDAO(FlaskConfig.POSTS_PATH, FlaskConfig.COMMENTS_PATH)  # Создаём объект класса

# Создаём блюпринт страницы поста с комментариями
post_with_comments_blueprint = Blueprint("post_with_comments_blueprint", __name__)


@post_with_comments_blueprint.route("/posts/<int:post_id>")
def show_post_with_comments(post_id):
    """
    Создаёт эндпоинт для поста с комментариями
    :return: Заполненный шаблон поста с комментариями
    """
    _post_with_comments = post_with_comments.load_post_with_comments(post_id)
    comments_count = len(_post_with_comments) - 1
    return render_template("post.html", posts=_post_with_comments, count=comments_count)
