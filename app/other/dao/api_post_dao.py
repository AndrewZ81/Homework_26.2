# Импортируем модуль JSON для работы с этим форматом
import json
from json import JSONDecodeError
from app.other.loggers import info_logger, error_logger  # Подключаем логгеры


class APIPostDAO:  # Создаём DAO для выборки конкретного поста

    def __init__(self, path):
        """
        Создаёт атрибут path
        :param path: Путь к файлу со всеми постами
        """
        self.path = path

    def load_all_posts(self):
        """
        Загружает все посты
        :return: Список постов
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
            return all_posts

    def load_post_by_id(self, post_id):
        """
        Загружает пост по идентификатору
        :param post_id: Идентификатор поста для поиска
        :return: Пост в формате словаря
        """
        post_by_id = {}
        for i in self.load_all_posts():
            if i["pk"] == post_id:
                post_by_id.update(i)
                break

        # Обрабатываем ошибку, когда не существует постов с данным идентификатором
        try:
            if not len(post_by_id):
                error_logger.error(f"Запрос /api/posts/{post_id}")
                raise ValueError("Не существует постов с данным идентификатором")
        except ValueError:
            raise
        else:
            info_logger.info(f"Запрос /api/posts/{post_id}")
            return post_by_id
