from flask import Blueprint, jsonify  # Подключаем для создания блюпринтов
from .dao.api_all_posts_dao import APIAllPostsDAO  # Подключаем для выборки всех постов
from config import FlaskConfig  # Подключаем для доступа к конфигурационным константам

api_all_posts = APIAllPostsDAO(FlaskConfig.POSTS_PATH)  # Создаём объект класса

# Создаём блюпринт страницы всех постов
api_all_posts_blueprint = Blueprint("api_all_posts_blueprint", __name__)


@api_all_posts_blueprint.route("/api/posts")
def show_all_posts():
    """
    Создаёт эндпоинт для всех постов
    :return: Список всех постов в формате json
    """
    all_posts = api_all_posts.load_all_posts()
    return jsonify(all_posts)
