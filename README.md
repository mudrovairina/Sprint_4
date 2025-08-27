# Unit-тестирование BooksCollector

Приложение **BooksCollector** позволяет управлять книгами: добавлять их в словарь, устанавливать жанры, фильтровать книги по возрастным ограничениям и управлять избранным.

## Тесты

| Метод                           | Тест                                                                             | Суть проверки                                                          |
| ------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `__init__`                      | `test_init_books_genre_is_empty_dict`                                            | `books_genre` пуст при создании                                        |
|                                 | `test_init_favorites_is_empty_list`                                              | `favorites` пуст                                                       |
|                                 | `test_init_genre_is_default_list`                                                | `genre` содержит все доступные жанры                                   |
|                                 | `test_init_genre_age_rating_is_default_list`                                     | `genre_age_rating` содержит запрещённые жанры                          |
| `add_new_book`                  | `test_add_new_book_valid_name_added` (параметризация)                            | Добавление книг с корректными названиями                               |
|                                 | `test_add_new_book_invalid_name_not_added` (параметризация)                      | Некорректные названия не добавляются                                   |
|                                 | `test_add_new_book_duplicate_name_not_added`                                     | Дубликаты не добавляются                                               |
| `set_book_genre`                | `test_set_book_genre_book_in_dict_and_genre_available_genre_set`                 | Жанр существующей книги из списка доступных жанров устанавливается     |
|                                 | `test_set_book_genre_book_not_in_dict_genre_not_set`                             | Жанр не устанавливается для отсутствующей книги                        |
|                                 | `test_set_book_genre_unavailable_genre_not_set`                                  | Жанр не устанавливается, если он отсутствует в списке доступных        |
| `get_book_genre`                | `test_get_book_genre_book_in_dict_returns_genre`                                 | Возвращается жанр существующей книги                                   |
|                                 | `test_get_book_genre_book_not_in_dict_returns_none`                              | Для несуществующей книги возвращается None                             |
| `get_books_with_specific_genre` | `test_get_books_with_specific_genre_available_genre_returns_books`               | Возвращается список книг указанного доступного жанра                   |
|                                 | `test_get_books_with_specific_genre_unavailable_genre_returns_empty_list` (парам.) | Пустой список для недоступного или отсутствующего жанра                |
| `get_books_genre`               | `test_get_books_genre_one_book_with_genre_returns_dict`                          | Один объект с жанром возвращается                                      |
|                                 | `test_get_books_genre_two_books_with_genre_returns_dict`                         | Два объекта с жанрами возвращаются                                     |
|                                 | `test_get_books_genre_one_book_without_genre_returns_dict`                       | Книга без жанра возвращается с пустой строкой                          |
|                                 | `test_get_books_genre_no_books_returns_empty_dict`                               | Возвращается пустой словарь, если книг нет                             |
| `get_books_for_children`        | `test_get_books_for_children_with_allowed_genre_returns_list`                    | Книги с разрешёнными жанрами возвращаются                              |
|                                 | `test_get_books_for_children_with_forbidden_genre_returns_empty_list`            | Книги с возрастным ограничением исключаются                            |
|                                 | `test_get_books_for_children_with_mixed_genre_returns_only_allowed_book`         | Возвращаются только разрешённые книги при смешанных жанрах             |
|                                 | `test_get_books_for_children_no_books_returns_empty_list`                        | Пустой список, если книг нет                                           |
|                                 | `test_get_books_for_children_book_without_genre_returns_empty_list`              | Книги без жанра не возвращаются                                        |
| `add_book_in_favorites`         | `test_add_book_in_favorites_existing_books_added` (параметризация)               | Книги, присутствующие в словаре, добавляются в избранное               |
|                                 | `test_add_book_in_favorites_duplicate_book_not_added`                            | Дубликаты не добавляются                                               |
|                                 | `test_add_book_in_favorites_nonexistent_book_not_added` (параметризация)         | Несуществующие книги или пустое имя не добавляются                     |
| `delete_book_from_favorites`    | `test_delete_book_from_favorites_existing_book_removed`                          | Существующая книга удаляется                                           |
|                                 | `test_delete_book_from_favorites_nonexistent_book_list_unchanged`                | Несуществующая книга не влияет на список                               |
|                                 | `test_delete_book_from_favorites_one_of_two_books_removed_only_that_one`         | Удаляется только выбранная книга                                       |
|                                 | `test_delete_book_from_favorites_empty_favorites_list_unchanged`                 | Если список пуст, ничего не происходит                                 |
|                                 | `test_delete_book_from_favorites_already_removed_book_list_unchanged`            | Повторное удаление книги не влияет                                     |
| `get_list_of_favorites_books`   | `test_get_list_of_favorites_books_one_book_returns_list`                         | Возвращается список с одной книгой                                     |
|                                 | `test_get_list_of_favorites_books_two_books_returns_list`                        | Возвращается список с двумя книгами                                    |
|                                 | `test_get_list_of_favorites_books_no_books_returns_empty_list`                   | Возвращается пустой список                                             |

## Запуск тестов

```bash
pytest -v test_books_collector.py