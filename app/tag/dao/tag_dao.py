# Импортируем модуль JSON для работы с этим форматом
import json
from json import JSONDecodeError


class TagDAO:  # Создаём DAO для выборки постов по ключевому тэгу

    def __init__(self, path):
        """
        Создаёт атрибут path
        :param path: Путь к файлу со всеми постами
        """
        self.path = path

    def load_posts_by_tag(self, tag):
        """
        Загружает выбранные по тэгу посты
        :return: Список выбранных по тэгу постов
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
            posts_by_tag = []
            searching_tag = "#" + tag.lower()
            for i in all_posts:
                post_content_as_list = i["content"].split(" ")
                for k in range(len(post_content_as_list)):
                    if post_content_as_list[k].lower() == searching_tag:
                        posts_by_tag.append(i)
                        break
            return posts_by_tag

    def load_posts_by_tag_with_tags(self, tag):
        """
        Загружает все выбранные по тэгу посты, преобразуя тэги в гиперссылки
        :return: Список выбранных по тэгу постов с преобразованными в гиперссылки тэгами
        """
        all_posts = self.load_posts_by_tag(tag)
        for i in all_posts:
            post_content_as_list = i["content"].split(" ")
            for k in range(len(post_content_as_list)):
                if post_content_as_list[k].startswith("#"):
                    old_value = post_content_as_list[k]
                    post_content_as_list[k] = f"<a href='/tag/{old_value[1:]}'>{old_value}</a>"
            post_content_as_str = " ".join(post_content_as_list)
            i["content"] = post_content_as_str
        return all_posts
