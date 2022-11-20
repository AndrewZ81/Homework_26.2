from flask import Blueprint, render_template  # Подключаем для создания блюпринтов на основе шаблонов
from .dao.user_dao import UserDAO  # Подключаем для выборки постов данного пользователя
from config import FlaskConfig  # Подключаем для доступа к конфигурационным константам

user = UserDAO(FlaskConfig.POSTS_PATH)  # Создаём объект класса

# Создаём блюпринт страницы постов данного пользователя
user_posts_blueprint = Blueprint("user_posts_blueprint", __name__)


@user_posts_blueprint.route("/users/<user_name>")
def show_user_posts(user_name):
    """
    Создаёт эндпоинт для постов данного пользователя
    :return: Заполненный шаблон постов данного пользователя
    """
    user_posts = user.load_posts_by_user(user_name)
    return render_template("user-feed.html", posts=user_posts)
