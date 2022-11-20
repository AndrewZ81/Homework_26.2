from flask import Blueprint, render_template, redirect  # Подключаем для создания блюпринтов на основе шаблонов
from .dao.bookmarks_dao import BookmarksDAO  # Подключаем для выборки закладок
from config import FlaskConfig  # Подключаем для доступа к конфигурационным константам

bookmark = BookmarksDAO(FlaskConfig.POSTS_PATH, FlaskConfig.BOOKMARKS_PATH)  # Создаём объект класса

# Создаём блюпринт для работы с закладками
bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, url_prefix="/bookmarks")


@bookmarks_blueprint.route("/")
def show_all_bookmarks():
    """
    Создаёт эндпоинт для отображения закладок
    :return: Заполненный шаблон закладок
    """
    all_bookmarks = bookmark.load_all_bookmarks_with_tags()
    return render_template("bookmarks.html", bookmarks=all_bookmarks)


@bookmarks_blueprint.route("/add/<int:post_id>")
def add_bookmark(post_id):
    """
    Создаёт эндпоинт для добавления закладки
    :return:
    """
    bookmark.add_bookmark(post_id)
    return redirect("/", code=302)


@bookmarks_blueprint.route("/remove/<int:post_id>")
def remove_bookmark(post_id):
    """
    Создаёт эндпоинт для добавления закладки
    :return:
    """
    bookmark.remove_bookmark(post_id)
    return redirect("/", code=302)
