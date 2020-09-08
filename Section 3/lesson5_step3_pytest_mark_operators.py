import pytest


@pytest.fixture(scope="function")
def fixture_example():
    print("\nstart...")
    yield
    print("\nquit...")


class TestOperators:

    # Для вызова определенных тестов из набора можно использовать логические операторы
    # Они применяются к mark
    # Примеры использующие операторы  or / and / not
    # test_mark_X - зарегистрированны в pytest.ini
    @pytest.mark.test_mark_1
    @pytest.mark.test_mark_2
    def test_operators_a(self, fixture_example):  # Тест А
        print(" -> test A with marks 1 and 2")

    @pytest.mark.test_mark_2
    @pytest.mark.test_mark_3
    def test_operators_b(self, fixture_example):  # Тест B
        print(" -> test B with marks 2 and 3")

    # pytest -s -m "test_mark_1 and test_mark_2" test_name.py - исполнится только тест A, тк test_mark_1 и test_mark_2
    # одновременно есть только у этого теста
    # pytest -s -m "test_mark_1 or test_mark_2" test_name.py - исполнятся оба теста, тк достаточно наличия любой
    # из этих двух mark у теста (у теста А, есть ..mark_1, а у теста В - ..mark_2)
    # pytest -s -m "not test_mark_2" test_name.py - оба теста проигнорируются, тк ..mark_2 есть у обоих
    # pytest -s -m "not test_mark_3" test_name.py - исполниться только тест А, без ..mark_3
