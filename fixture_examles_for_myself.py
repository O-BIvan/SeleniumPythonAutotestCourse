import time
import pytest

# справка: тест-СЦЕНАРИЙ - набор кейсов (обычно объединен одной тематикой: смоук-тест, тестирование страницы с котом)
# фикстура в данном случае весь код после @pytest.fixture и до следующей @pytest.fixture
# н., def suite_data... ...Suite teardown")


@pytest.fixture(scope='class', autouse=True)  # "настройки" для тест-СЦЕНАРИЯ - запускаются для всех тестов в наборе
def suite_data():  # вызывается для всех классов -> class Test...
    print("\n> Suite setup")  # какие-то "действия" до выполнения тест-СЦЕНАРИЯ (например, log in)
    yield  # работает как разделитель между началом/окончанием тест-СЦЕНАРИЯ (может как return возвращать что-нибудь)
    print("> Suite teardown")


@pytest.fixture(scope='function')  # "настройки" для тест-КЕЙСА - запускаются для каждого тест-кейса
def case_data():  # вызывается для методов, путем указания конкретно ее (case_data) в методе
    print("\n   > Case setup")  # какие-то "действия" до выполнения тест-КЕЙСА (например, log in)
    yield time.time()  # здесь еще возвращает время для использования в КЕЙСЕ
    print("\n   > Case teardown")  # какие-то "действия" после выполнения тест-КЕЙСА (например, log out)


@pytest.fixture(scope='function')  # другие "настройки" для тест-КЕЙСА (исп-ся в TestSuite3)
def different_case_data():  # который находится в СЦЕНАРИИ с кейсами, использующими предыдущие (case_data)
    print("\n > Case setup (different)")  # к ниму применяются общие для сценария действия (н., запуск браузера), но
    yield time.time()
    print("\n > Case teardown (different)")  # разные "настройки" тест-КЕЙСА (вместо log out, удалить папку system32)

# код test_case_X для примера
# просто возвращает текущее время в секундах, переводит в int, сравнивает с 0 (соответственно тест проваливается)


class TestSuite1:  # выполняются действия заложенные в def suite_data() (которые до yield)

    def test_case_1(self, case_data):  # выполняются действия заложенные в def case_data() до yield
        time1 = int(case_data)
        print("      > case 1 ongoing")
        assert(time1 == 0)  # после assert выполняются действия заложенные в def case_data() после yield

    def test_case_2(self, case_data):  # снова выполняются действия заложенные в def case_data() до yield
        time2 = int(case_data)
        print("      > case 2 ongoing")
        assert(time2 == 0)  # снова, после assert выполняются действия заложенные в def case_data() после yield

# после выполнения последнего КЕЙСА в СЦЕНАРИИ, выполняется код после yield в фикстуре def suite_data()
# в данном случае: print("> Suite teardown")


class TestSuite2:

    def test_case_3(self, case_data):
        time3 = int(case_data)
        print("      > case 3 ongoing")
        assert (time3 == 0)


class TestSuite3:  # выполняются действия заложенные в def suite_data() (которые до yield)

    def test_case_4(self, case_data):  # выполняются действия заложенные в def case_data()
        time4 = int(case_data)
        print("      > case 4 ongoing")
        assert (time4 == 0)

    def test_case_5(self, case_data):  # выполняются действия заложенные в def case_data()
        time5 = int(case_data)
        print("      > case 5 ongoing")
        assert (time5 == 0)

    def test_case_diff(self, different_case_data):  # ВЫПОЛНЯЮТСЯ ДРУГИЕ ДЕЙСТВИЯ, заложенные в def different_case_data
        time6 = int(different_case_data)
        print("     > case different ongoing")  # ВЫПОЛНЯЮТСЯ действия заложенные в def different_case_data, после yield
        assert (time6 == 0)

# после выполнения последнего КЕЙСА в СЦЕНАРИИ, выполняется код после yield в фикстуре def suite_data()
# в данном случае: print("> Suite teardown")
