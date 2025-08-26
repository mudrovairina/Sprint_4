import pytest


class TestBooksCollector:

    # тесты для метода __init__
    def test_init_books_genre_is_empty_dict(self, collector):
        """После инициализации словарь books_genre пустой"""
        assert collector.books_genre == {}

    def test_init_favorites_is_empty_list(self, collector):
        """После инициализации список favorites пустой"""
        assert collector.favorites == []

    def test_init_genre_is_default_list(self, collector):
        """После инициализации список жанров совпадает с дефолтным"""
        assert collector.genre == [
            'Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'
        ]

    def test_init_genre_age_rating_is_default_list(self, collector):
        """После инициализации список жанров с возрастным ограничением
        совпадает с дефолтным"""
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    # тесты для добавления новой книги
    @pytest.mark.parametrize(
        'name',
        [
            "The Green Mile",
            "T",  # длина 1
            "T" * 2,
            "T" * 39,
            "T" * 40,
        ])
    def test_add_new_book_valid_name_added(self, collector, name):
        """Книга с допустимой длиной названия добавляется"""
        collector.add_new_book(name)
        assert collector.books_genre == {name: ''}

    @pytest.mark.parametrize(
        "name",
        [
            "",  # пустое название
            "T" * 41,
            "T" * 42,
            "T" * 45
        ])
    def test_add_new_book_invalid_name_not_added(self, collector, name):
        """Книга с недопустимой длиной названия не добавляется"""
        collector.add_new_book(name)
        assert collector.books_genre == {}

    def test_add_new_book_duplicate_name_not_added(self, collector):
        """Книга с повторяющимся названием не добавляется повторно"""
        collector.add_new_book('The Green Mile')
        collector.add_new_book('The Green Mile')
        assert collector.books_genre == {'The Green Mile': ''}

    # тесты для устанавливания книге жанра
    def test_set_book_genre_book_in_dict_and_genre_available_genre_set(
            self, collector):
        """Книге из словаря можно установить доступный жанр"""
        collector.add_new_book('The Green Mile')
        collector.set_book_genre('The Green Mile', 'Фантастика')
        assert collector.books_genre['The Green Mile'] == 'Фантастика'

    def test_set_book_genre_book_not_in_dict_genre_not_set(self, collector):
        """Если книги нет в словаре, жанр не устанавливается"""
        collector.set_book_genre('Fight Club', 'Фантастика')
        assert 'Fight Club' not in collector.books_genre

    def test_set_book_genre_unavailable_genre_not_set(self, collector):
        """Если жанра нет в списке доступных, он не устанавливается"""
        collector.add_new_book('The Green Mile')
        collector.set_book_genre('The Green Mile', 'Про любовь')
        assert collector.books_genre['The Green Mile'] == ''

    # тесты для получения жанра книги
    def test_get_book_genre_book_in_dict_returns_genre(self, collector):
        """Для книги в словаре возвращается её жанр"""
        collector.add_new_book('The Green Mile')
        collector.set_book_genre('The Green Mile', 'Фантастика')
        assert collector.get_book_genre('The Green Mile') == 'Фантастика'

    def test_get_book_genre_book_not_in_dict_returns_none(self, collector):
        """Для книги, которой нет в словаре, возвращается None"""
        assert collector.get_book_genre('Fight Club') is None

    # тесты для получения списка книг по жанру
    def test_get_books_with_specific_genre_available_genre_returns_books(
            self, collector):
        """Возвращает список книг с заданным жанром"""
        collector.add_new_book('The Green Mile')
        collector.set_book_genre('The Green Mile', 'Фантастика')
        books_with_specific_genre = collector.get_books_with_specific_genre(
            'Фантастика')
        assert books_with_specific_genre == ['The Green Mile']

    @pytest.mark.parametrize(
        "genre",
        [
            "",  # пустой жанр
            "Про любовь",  # жанра нет в списке
            "Fantasy",  # жанр на другом языке
        ])
    def test_get_books_with_specific_genre_unavailable_genre_returns_empty_list(
            self, collector, genre):
        """Если жанра нет в списке доступных — возвращается пустой список"""
        collector.add_new_book('The Green Mile')
        collector.set_book_genre('The Green Mile', 'Фантастика')
        books_with_specific_genre = collector.get_books_with_specific_genre(
            genre)
        assert books_with_specific_genre == []

    # тесты для получения словаря books_genre
    def test_get_books_genre_one_book_with_genre_returns_dict(self, collector):
        """Словарь с одной книгой и установленным жанром
        возвращается корректно"""
        collector.add_new_book('The Green Mile')
        collector.set_book_genre('The Green Mile', 'Фантастика')
        assert collector.get_books_genre() == {'The Green Mile': 'Фантастика'}

    def test_get_books_genre_two_books_with_genre_returns_dict(
            self, collector):
        """Словарь с двумя книгами и их жанрами возвращается корректно"""
        collector.add_new_book('The Green Mile')
        collector.set_book_genre('The Green Mile', 'Фантастика')
        collector.add_new_book('Fight Club')
        collector.set_book_genre('Fight Club', 'Фантастика')
        assert collector.get_books_genre() == {
            'The Green Mile': 'Фантастика',
            'Fight Club': 'Фантастика'
        }

    def test_get_books_genre_one_book_without_genre_returns_dict(
            self, collector):
        """Книга без жанра возвращается в словаре со значением '' """
        collector.add_new_book('The Green Mile')
        assert collector.get_books_genre() == {'The Green Mile': ''}

    def test_get_books_genre_no_books_returns_empty_dict(self, collector):
        """Если книг нет, возвращается пустой словарь"""
        assert collector.get_books_genre() == {}

    # тесты для получения книг, подходящих детям
    def test_get_books_for_children_with_allowed_genre_returns_list(
            self, collector):
        """Возвращается список книг с разрешённым жанром"""
        collector.add_new_book('Harry_Potter')
        collector.set_book_genre('Harry_Potter', 'Фантастика')
        assert collector.get_books_for_children() == ['Harry_Potter']

    def test_get_books_for_children_no_books_returns_empty_list(
            self, collector):
        """Если книг нет, возвращается пустой список"""
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_book_without_genre_returns_empty_list(
            self, collector):
        """Книга без жанра не попадает в список для детей"""
        collector.add_new_book('Harry_Potter')
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_with_forbidden_genre_returns_empty_list(
            self, collector):
        """Книга с запрещённым жанром не попадает в список для детей"""
        collector.add_new_book('The Shining')
        collector.set_book_genre('The Shining', 'Ужасы')
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_with_mixed_genre_returns_only_allowed_book(
            self, collector):
        """Возвращаются только книги с разрешёнными жанрами"""
        collector.add_new_book('Harry_Potter')
        collector.set_book_genre('Harry_Potter', 'Фантастика')
        collector.add_new_book('The Shining')
        collector.set_book_genre('The Shining', 'Ужасы')
        assert collector.get_books_for_children() == ['Harry_Potter']

    # тесты для добавления книги в Избранное
    @pytest.mark.parametrize("books", [
        ['The Green Mile'],
        ['The Green Mile', 'Harry_Potter'],
    ])
    def test_add_book_in_favorites_existing_books_added(
            self, collector, books):
        """Книги, которые есть в словаре, можно добавить в избранное"""
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        assert collector.favorites == books

    def test_add_book_in_favorites_duplicate_book_not_added(self, collector):
        """Одна и та же книга не может добавляться в избранное дважды"""
        collector.add_new_book('The Green Mile')
        collector.add_book_in_favorites('The Green Mile')
        collector.add_book_in_favorites('The Green Mile')
        assert collector.favorites == ['The Green Mile']

    @pytest.mark.parametrize("book", ['Fight Club', ''])
    def test_add_book_in_favorites_nonexistent_book_not_added(
            self, collector, book):
        """Книги, которых нет в словаре или пустое название,
        не добавляются в избранное"""
        collector.add_book_in_favorites(book)
        assert collector.favorites == []

    # тесты для удаления книги из Избранного
    def test_delete_book_from_favorites_existing_book_removed(self, collector):
        """Книга из избранного удаляется"""
        collector.add_new_book('The Green Mile')
        collector.add_book_in_favorites('The Green Mile')
        collector.delete_book_from_favorites('The Green Mile')
        assert collector.favorites == []

    def test_delete_book_from_favorites_nonexistent_book_list_unchanged(
            self, collector):
        """Попытка удалить книгу, которой нет в избранном, не меняет список"""
        collector.add_new_book('The Green Mile')
        collector.add_book_in_favorites('The Green Mile')
        collector.delete_book_from_favorites('Fight Club')
        assert collector.favorites == ['The Green Mile']

    def test_delete_book_from_favorites_one_of_two_books_removed_only_that_one(
            self, collector):
        """Удаляется только выбранная книга, остальные остаются"""
        collector.add_new_book('The Green Mile')
        collector.add_book_in_favorites('The Green Mile')
        collector.add_new_book('Fight Club')
        collector.add_book_in_favorites('Fight Club')
        collector.delete_book_from_favorites('The Green Mile')
        assert collector.favorites == ['Fight Club']

    def test_delete_book_from_favorites_empty_favorites_list_unchanged(
            self, collector):
        """Попытка удалить книгу из пустого списка не вызывает ошибок"""
        collector.delete_book_from_favorites('The Green Mile')
        assert collector.favorites == []

    def test_delete_book_from_favorites_already_removed_book_list_unchanged(
            self, collector):
        """Повторное удаление книги из избранного не вызывает ошибок"""
        collector.add_new_book('The Green Mile')
        collector.add_book_in_favorites('The Green Mile')
        collector.delete_book_from_favorites('The Green Mile')  # первый раз
        collector.delete_book_from_favorites('The Green Mile')  # второй раз
        assert collector.favorites == []

    # тесты для получения списка избранных книг
    def test_get_list_of_favorites_books_one_book_returns_list(
            self, collector):
        """Список избранных книг с одной книгой возвращается корректно"""
        collector.add_new_book('The Green Mile')
        collector.add_book_in_favorites('The Green Mile')
        assert collector.get_list_of_favorites_books() == ['The Green Mile']

    def test_get_list_of_favorites_books_two_books_returns_list(
            self, collector):
        """Список избранных книг с двумя книгами возвращается корректно"""
        collector.add_new_book('The Green Mile')
        collector.add_book_in_favorites('The Green Mile')
        collector.add_new_book('Fight Club')
        collector.add_book_in_favorites('Fight Club')
        assert collector.get_list_of_favorites_books() == [
            'The Green Mile', 'Fight Club'
        ]

    def test_get_list_of_favorites_books_no_books_returns_empty_list(
            self, collector):
        """Если избранных книг нет, возвращается пустой список"""
        assert collector.get_list_of_favorites_books() == []
