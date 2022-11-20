from flask import Blueprint, render_template  # Подключаем для создания блюпринтов на основе шаблонов
from .dao.all_posts_dao import AllPostsDAO  # Подключаем для выборки всех постов
from app.bookmarks.dao.bookmarks_dao import BookmarksDAO  # Подключаем для выборки закладок
from config import FlaskConfig  # Подключаем для доступа к конфигурационным константам

all_posts = AllPostsDAO(FlaskConfig.POSTS_PATH)  # Создаём объекты классов
bookmark = BookmarksDAO(FlaskConfig.POSTS_PATH, FlaskConfig.BOOKMARKS_PATH)

# Создаём блюпринт главной страницы (далее - ленты)
all_posts_blueprint = Blueprint("all_posts_blueprint", __name__)


@all_posts_blueprint.route("/")
def show_all_posts():
    """
    Создаёт эндпоинт для ленты
    :return: Заполненный шаблон ленты
    """
    _bookmarks = bookmark.load_all_bookmarks()
    _all_posts = all_posts.load_all_posts_with_tags()
    return render_template("index.html", posts=_all_posts, quantity=len(_bookmarks))
