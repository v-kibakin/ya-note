# test_content.py
import pytest
from pytest_lazy_fixtures import lf
from django.urls import reverse



@pytest.mark.parametrize(
    # Задаём названия для параметров:
    'parametrized_client, note_in_list',
    (
        # Передаём фикстуры в параметры при помощи "ленивых фикстур":
        (lf('author_client'), True),
        (lf('not_author_client'), False),
    )
)
# Используем фикстуру заметки и параметры из декоратора:
def test_notes_list_for_different_users(
    note, parametrized_client, note_in_list
):
    url = reverse('notes:list')
    # Выполняем запрос от имени параметризованного клиента:
    response = parametrized_client.get(url)
    object_list = response.context['object_list']
    # Проверяем истинность утверждения "заметка есть в списке":
    assert (note in object_list) is note_in_list
