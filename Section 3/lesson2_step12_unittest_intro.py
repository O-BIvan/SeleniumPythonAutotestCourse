import unittest  # unittest - это framework для тестирования, входящий в стандартную библиотеку языка Python


# Создать класс, который должен наследоваться от класса TestCase: class TestAbs(unittest.TestCase)
# (класс TestCase определен в библиотеке unittest)

# Общее правило для всех фреймворков: название тестового метода должно начинаться со слова "test_"

class TestAbs(unittest.TestCase):
    # Превратить тестовые функции в методы, добавив ссылку на экземпляр
    # класса self в качестве первого аргумента функции
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()
