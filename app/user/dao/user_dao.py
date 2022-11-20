# Импортируем модуль JSON для работы с этим форматом
import json
from json import JSONDecodeError


class UserDAO:  # Создаём DAO для выборки постов данного пользователя

    def __init__(self, path):
        """
        Создаёт атрибут path
        :param path: Путь к файлу со всеми постами
        """
        self.path = path

    def load_all_posts_with_tags(self):
        """
        Загружает все посты, преобразуя слова с тэгом # в гиперссылки
        :return: Список постов с преобразованными в гиперссылки словами с тэгом #
        """
        try:
            file = open(self.path, encoding="utf-8")
            all_posts = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.path} с постами для загрузки не найден")
        except JSONDecodeError:
            raise ValueError(f"Файл {self.path} с постами для загрузки не удалось считать")
        else:
            file.close()
            for i in all_posts:
                post_content_as_list = i["content"].split(" ")
                for k in range(len(post_content_as_list)):
                    if post_content_as_list[k].startswith("#"):
                        old_value = post_content_as_list[k]
                        post_content_as_list[k] = f"<a href='/tag/{old_value[1:]}'>{old_value}</a>"
                post_content_as_str = " ".join(post_content_as_list)
                i["content"] = post_content_as_str
            return all_posts

    def load_posts_by_user(self, name):
        """
        Загружает выборку постов данного пользователя
        :param name: Ключевое слово для поиска имени пользователя
        :return: Выборку постов данного пользователя в формате списка
        """
        posts_by_user = []
        for i in self.load_all_posts_with_tags():
            if i["poster_name"].lower() == name.lower():
                posts_by_user.append(i)

        # Обрабатываем ошибку, когда не существует постов данного пользователя
        try:
            if not len(posts_by_user):
                raise ValueError("Не существует постов данного пользователя")
        except ValueError:
            raise
        else:
            return posts_by_user
