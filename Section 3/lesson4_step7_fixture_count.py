import pytest

# Выполняется в начале тестов def test_ (выводит: "^-^") и после них (выводит: ":3"), тк есть yield
# Выполниться, если даже вызвана только в одно из тестов
# Если не вызвана не в одном тесте, то не выполняется, если нет autouse = True


@pytest.fixture(scope="class")  # 2
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


# Выполниться в первом тесте, тк не указан scope, то следовательно function  по-умолчанию
# Вызывается она только в первом тесте (выводит: ":)")


@pytest.fixture()
def very_important_fixture():  # 1
    print(":)", "\n")


# Scope = function по-умолчанию
# Стоит autouse = True
# Следовательно сработает для всех (autouse) функций (scope по-умолч.)
# Выводит: ":-Р" для каждой функции


@pytest.fixture(autouse=True)  # 2
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces:
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass

    def test_second_smiling_faces(self, prepare_faces):
        pass
