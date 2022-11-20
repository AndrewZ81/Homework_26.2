from flask import Blueprint, render_template, request  # Подключаем для создания блюпринтов на основе шаблонов
from .dao.search_dao import SearchDAO  # Подключаем для выборки постов по ключевому слову
from config import FlaskConfig  # Подключаем для доступа к конфигурационным константам

posts_by_keyword = SearchDAO(FlaskConfig.POSTS_PATH)  # Создаём объект класса

# Создаём блюпринт страницы выбранных постов по ключевому слову
posts_by_keyword_blueprint = Blueprint("posts_by_keyword_blueprint", __name__)


@posts_by_keyword_blueprint.route("/search/")
def show_posts_by_keyword():
    """
    Создаёт эндпоинт для выбранных постов по ключевому слову
    :return: Заполненный шаблон выбранных постов
    """
    key_for_search = request.args.get("s")
    if not key_for_search:
        return f"<h3>Вы не ввели текст для поиска. " \
               f"Вернитесь на главную и попробуйте снова</h3>" \
               f"<a href='/'>На главную</a>"
    else:
        _posts_by_keyword = posts_by_keyword.load_posts_by_keyword_with_tags(key_for_search)
        posts_count = len(_posts_by_keyword)
        return render_template("search.html", posts=_posts_by_keyword, count=posts_count)
