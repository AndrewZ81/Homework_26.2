from flask import Blueprint, render_template  # Подключаем для создания блюпринтов на основе шаблонов
from .dao.tag_dao import TagDAO  # Подключаем для выборки постов данного пользователя
from config import FlaskConfig  # Подключаем для доступа к конфигурационным константам

posts_with_tag = TagDAO(FlaskConfig.POSTS_PATH)  # Создаём объект класса

# Создаём блюпринт страницы постов данного пользователя
posts_with_tag_blueprint = Blueprint("posts_with_tag_blueprint", __name__)


@posts_with_tag_blueprint.route("/tag/<tag_name>")
def show_posts_with_tag(tag_name):
    """
    Создаёт эндпоинт для постов с данным тэгом
    :return: Заполненный шаблон постов с данным тэгом
    """
    _posts_with_tag = posts_with_tag.load_posts_by_tag_with_tags(tag_name)
    return render_template("tag.html", posts=_posts_with_tag, name=tag_name)
