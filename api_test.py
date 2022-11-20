from main import app
import pytest


# Тестируем API
def test_api():
    posts_response = app.test_client().get("/api/posts")
    post_response = app.test_client().get("/api/posts/1")
    post_keys = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]

    # Тестируем правильность возвращаемых типов данных
    assert isinstance(posts_response.json, list), "Должен возвращаться список!"
    assert isinstance(post_response.json, dict), "Должен возвращаться словарь"

    # Тестируем правильность возвращаемых ключей и правильную длину словарей
    for i in posts_response.json:
        assert len(i) == 7, "Отсутствует один из ключей словаря!"
        for k in i.keys():
            assert k in post_keys, f"{k} не является верным ключом словаря!"
    for i in post_response.json.keys():
        assert i in post_keys, f"{i} не является верным ключом словаря!"
    assert len(post_response.json) == 7, "Отсутствует один из ключей словаря!"
