# Импортируем модуль JSON для работы с этим форматом
import json
from json import JSONDecodeError


class PostDAO:  # Создаём DAO для выборки конкретного поста и комментариев к нему

    def __init__(self, posts_path, comments_path):
        """
        Создаёт атрибуты posts_path, comments_path
        :param posts_path: Путь к файлу со всеми постами
        :param comments_path: Путь к файлу со всеми комментариями
        """
        self.posts_path = posts_path
        self.comments_path = comments_path

    def load_all_posts_with_tags(self):
        """
        Загружает все посты, преобразуя слова с тэгом # в гиперссылки
        :return: Список постов с преобразованными в гиперссылки словами с тэгом #
        """
        try:
            file = open(self.posts_path, encoding="utf-8")
            all_posts = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.posts_path} с постами для загрузки не найден")
        except JSONDecodeError:
            raise ValueError(f"Файл {self.posts_path} с постами для загрузки не удалось считать")
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

    def load_all_comments(self):
        """
        Загружает все комментарии
        :return: Список комментариев
        """
        try:
            file = open(self.comments_path, encoding="utf-8")
            all_comments = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.comments_path} с комментариями для загрузки не найден")
        except JSONDecodeError:
            raise ValueError(f"Файл {self.comments_path} с комментариями для загрузки не удалось считать")
        else:
            file.close()
            return all_comments

    def load_post_with_comments(self, post_id):
        """
        Загружает выбранный пост полностью с комментариями
        :return: Выбранный пост полностью с комментариями в формате списка
        """
        post_with_comments = []
        for i in self.load_all_posts_with_tags():
            if i["pk"] == post_id:
                post_with_comments.append(i)
                break

        # Обрабатываем ошибку, когда пост с данным идентификатором не существует
        try:
            if not len(post_with_comments):
                raise ValueError("Пост с данным идентификатором не существует")
        except ValueError:
            raise
        else:
            for i in self.load_all_comments():
                if i["post_id"] == post_id:
                    post_with_comments.append(i)
            return post_with_comments
