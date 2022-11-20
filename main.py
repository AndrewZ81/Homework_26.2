from flask import Flask  # Подключаем необходимые инструменты из модуля flask
from config import FlaskConfig  # Подключаем конфигурационный класс

# Подключаем блюпринты
from app.main.all_posts_views import all_posts_blueprint  # Для вывода ленты
from app.post.post_view import post_with_comments_blueprint  # Для вывода поста с комментариями
from app.search.search_view import posts_by_keyword_blueprint # Для вывода выбранных постов по ключу
from app.user.user_view import user_posts_blueprint  # Для вывода постов данного пользователя
from app.other.api_all_posts_view import api_all_posts_blueprint  # Для вывода постов в формате json
from app.other.api_post_view import api_post_by_id_blueprint  # Для вывода поста в формате json
from app.bookmarks.bookmarks_view import bookmarks_blueprint  # Для работы с закладками
from app.tag.tag_view import posts_with_tag_blueprint  # Для вывода выбранных по тэгу постов

app = Flask(__name__)  # Создаём наше приложение
app.config.from_object(FlaskConfig)  # Подключаем для доступа к конфигурационным константам

# Регистрируем блюпринты
app.register_blueprint(all_posts_blueprint)
app.register_blueprint(post_with_comments_blueprint)
app.register_blueprint(posts_by_keyword_blueprint)
app.register_blueprint(user_posts_blueprint)
app.register_blueprint(api_all_posts_blueprint)
app.register_blueprint(api_post_by_id_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(posts_with_tag_blueprint)


# Добавляем обработчики ошибок
@app.errorhandler(500)
def internal_server_error(error):
    return """<h3>Похоже, такого поста или пользователя не существует.
           Либо проблема с базой данных. Вернитесь на главную и попробуйте снова</h3>
           <a href='/'>На главную</a>""", 500


@app.errorhandler(404)
def page_not_found(error):
    return """<h3>Похоже, такого пути не существует.
              Вернитесь на главную и попробуйте снова</h3>
              <a href='/'>На главную</a>""", 404


if __name__ == "__main__":
    app.run()
