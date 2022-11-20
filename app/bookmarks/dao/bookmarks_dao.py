# Импортируем модуль JSON для работы с этим форматом
import json
from json import JSONDecodeError


class BookmarksDAO:  # Создаём DAO для работы с закладками

    def __init__(self, posts_path, bookmarks_path):
        """
        Создаёт атрибуты posts_path, bookmarks_path
        :param posts_path: Путь к файлу с лентой
        :param bookmarks_path: Путь к файлу с закладками
        """
        self.posts_path = posts_path
        self.bookmarks_path = bookmarks_path

    def load_all_posts(self):
        """
        Загружает все посты
        :return: Список постов
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
            return all_posts

    def load_all_bookmarks(self):
        """
        Загружает все закладки
        :return: Список закладок
        """
        try:
            file = open(self.bookmarks_path, encoding="utf-8")
            all_bookmarks = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.bookmarks_path} с постами для загрузки не найден")
        except JSONDecodeError:
            raise ValueError(f"Файл {self.bookmarks_path} с постами для загрузки не удалось считать")
        else:
            file.close()
            return all_bookmarks

    def load_all_bookmarks_with_tags(self):
        """
        Загружает все закладки, преобразуя слова с тэгом # в гиперссылки
        :return: Список закладок с преобразованными в гиперссылки словами с тэгом #
        """
        try:
            file = open(self.bookmarks_path, encoding="utf-8")
            all_bookmarks = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.bookmarks_path} с постами для загрузки не найден")
        except JSONDecodeError:
            raise ValueError(f"Файл {self.bookmarks_path} с постами для загрузки не удалось считать")
        else:
            file.close()
        for i in all_bookmarks:
            post_content_as_list = i["content"].split(" ")
            for k in range(len(post_content_as_list)):
                if post_content_as_list[k].startswith("#"):
                    old_value = post_content_as_list[k]
                    post_content_as_list[k] = f"<a href='/tag/{old_value[1:]}'>{old_value}</a>"
            post_content_as_str = " ".join(post_content_as_list)
            i["content"] = post_content_as_str
        return all_bookmarks

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
                raise ValueError("Не существует постов с данным идентификатором")
        except ValueError:
            raise
        else:
            return post_by_id

    def add_bookmark(self, post_id):
        """
        Добавляет пост в закладки
        :param post_id: Идентификатор поста для добавления в закладки
        :return: Сохраненный файл с закладками формата JSON после добавления закладки
        """
        bookmarks = self.load_all_bookmarks()
        new_bookmark = self.load_post_by_id(post_id)
        for i in bookmarks:
            if new_bookmark["pk"] == i["pk"]:
                return
        bookmarks.append(new_bookmark)
        file = open(self.bookmarks_path, "w", encoding="utf-8")
        return json.dump(bookmarks, file, indent=2, ensure_ascii=False)

    def remove_bookmark(self, post_id):
        """
        Удаляет пост из закладок
        :param post_id: Идентификатор поста для удаления из закладок
        :return: Сохраненный файл с закладками формата JSON после удаления закладки
        """
        bookmarks = self.load_all_bookmarks()
        trash_bookmark = self.load_post_by_id(post_id)
        for i in bookmarks:
            if trash_bookmark["pk"] == i["pk"]:
                bookmarks.remove(trash_bookmark)
                file = open(self.bookmarks_path, "w", encoding="utf-8")
                return json.dump(bookmarks, file, indent=2, ensure_ascii=False)
        return
