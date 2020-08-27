import pytest

# Отметьте ниже только те тестовые методы, которые будут найдены и выполнены PyTest при запуске следующей команды:
# pytest -v -m "smoke and not beta_users" test_task_run_1.py
# Внимание: mark AND not mark


class TestMainPage:
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):  # выполниться
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):  # нет необходимых отметок
        assert True


class TestBasket:
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):  # будет пропущен, skip у функции
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):  # выполниться
        assert True


@pytest.mark.skip
class TestBookPage:
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):  # будет пропущен - mark.skip у класса
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):  # skip у класса, нет необходимых отметок
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):  # будет пропущен, тк есть mark.beta_users
    assert True

# Ответ: 1,4
