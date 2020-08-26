import time
import pytest

# Справка: тест-СЦЕНАРИЙ - набор кейсов (обычно объединен одной тематикой: смоук-тест, тестирование страницы с котом)
# Фикстура, в данном случае, весь код после @pytest.fixture и до следующей @pytest.fixture
# н., def suite_data... ...Suite teardown")
# yield - генератор (см. lesson3_step5_fixture_example4.py)


@pytest.fixture(scope='class', autouse=True)  # "Настройки" для тест-СЦЕНАРИЯ - запускаются для всех тестов в наборе
def suite_data():  # Вызывается для всех классов -> class Test...
    print("\n> Suite setup")  # Какие-то "действия" до выполнения тест-СЦЕНАРИЯ (например, запуск браузера)
    yield  # Работает как разделитель между началом/окончанием тест-СЦЕНАРИЯ (может как return возвращать что-нибудь)
    print("> Suite teardown") # Какие-то "действия" после выполнения тест-КЕЙСА (например, закрытие браузера)


@pytest.fixture(scope='function')  # "Настройки" для тест-КЕЙСА - запускаются для каждого тест-кейса
def case_data():  # Вызывается для методов, путем указания конкретно ее (case_data) в методе
    print("\n   > Case setup")  # Какие-то "действия" до выполнения тест-КЕЙСА (например, log in)
    yield time.time()  # Здесь еще возвращает время для использования в КЕЙСЕ
    print("\n   > Case teardown")  # Какие-то "действия" после выполнения тест-КЕЙСА (например, log out)

# Другие "настройки" для тест-КЕЙСА (исп-ся в TestSuite3)
# Этот тест-КЕЙС находится в СЦЕНАРИИ с кейсами, использующими предыдущие (case_data)
# К ниму применяются общие для сценария действия (н., запуск браузера)
# Но другие "настройки" тест-КЕЙСА (н., вместо log out - переход на др. страницу)


@pytest.fixture(scope='function')
def different_case_data():
    print("\n > Case setup (different)")
    yield time.time()
    print("\n > Case teardown (different)")

# Код test_case_X для примера
# Просто возвращает текущее время в секундах, переводит в int, сравнивает с 0 (соответственно тест проваливается)


class TestSuite1:  # Выполняются действия заложенные в def suite_data() (которые до yield)

    def test_case_1(self, case_data):  # Выполняются действия заложенные в def case_data() до yield
        time1 = int(case_data)
        print("      > case 1 ongoing")
        assert(time1 == 0)  # После assert выполняются действия заложенные в def case_data() после yield

    def test_case_2(self, case_data):  # Снова выполняются действия заложенные в def case_data() до yield
        time2 = int(case_data)
        print("      > case 2 ongoing")
        assert(time2 == 0)  # Снова, после assert выполняются действия заложенные в def case_data() после yield

# После выполнения последнего КЕЙСА в СЦЕНАРИИ, выполняется код после yield в фикстуре def suite_data()
# В данном случае: print("> Suite teardown")


class TestSuite2:

    def test_case_3(self, case_data):
        time3 = int(case_data)
        print("      > case 3 ongoing")
        assert (time3 == 0)


class TestSuite3:  # Выполняются действия заложенные в def suite_data() (которые до yield)

    def test_case_4(self, case_data):  # Выполняются действия заложенные в def case_data()
        time4 = int(case_data)
        print("      > case 4 ongoing")
        assert (time4 == 0)

    def test_case_5(self, case_data):  # Выполняются действия заложенные в def case_data()
        time5 = int(case_data)
        print("      > case 5 ongoing")
        assert (time5 == 0)

    def test_case_diff(self, different_case_data):  # ВЫПОЛНЯЮТСЯ ДРУГИЕ ДЕЙСТВИЯ, заложенные в def different_case_data
        time6 = int(different_case_data)
        print("     > case different ongoing")  # ВЫПОЛНЯЮТСЯ действия заложенные в def different_case_data, после yield
        assert (time6 == 0)

# После выполнения последнего КЕЙСА в СЦЕНАРИИ, выполняется код после yield в фикстуре def suite_data()
# В данном случае: print("> Suite teardown")
