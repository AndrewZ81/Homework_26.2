from flask import Blueprint, jsonify  # Подключаем для создания блюпринтов
from .dao.api_post_dao import APIPostDAO  # Подключаем для выборки поста по идентификатору
from config import FlaskConfig  # Подключаем для доступа к конфигурационным константам

api_post_by_id = APIPostDAO(FlaskConfig.POSTS_PATH)  # Создаём объект класса

# Создаём блюпринт страницы поста
api_post_by_id_blueprint = Blueprint("api_post_by_id_blueprint", __name__)


@api_post_by_id_blueprint.route("/api/posts/<int:post_id>")
def show_post_by_id(post_id):
    """
    Создаёт эндпоинт для выборки поста по идентификатору
    :return: Выбранный пост формате словаря json
    """
    post_by_id = api_post_by_id.load_post_by_id(post_id)
    return jsonify(post_by_id)
