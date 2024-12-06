from os import getcwd, path
from pytest import raises
from cookbook import Cookbook

class TestCookbook:

    def test_creation_correct(self):
        """Test cookbook creation with a correct recipes file."""
        cookbook = Cookbook.from_file(path.join(getcwd(), 'files', 'recipes.txt'))
        assert cookbook.cookbook == {
            'Омлет': [
                {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
                {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
                {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
            ],
            'Утка по-пекински': [
                {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
                {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
                {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
                {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
            ],
            'Запеченный картофель': [
                {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
                {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
                {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
            ],
            'Фахитос': [
                {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
                {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
                {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
                {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
                {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
            ],
        }

    def test_creation_wrong_count(self):
        """
        Test with an incorrect recipes file where one ingredient count
        is not a number.

        """
        with raises(TypeError) as error:
            Cookbook.from_file(path.join(getcwd(), 'files', 'recipes_wrong_count.txt'))
            assert error.value == 'Count of ingredients for Запеченный картофель must be an integer.'

    def test_creation_wrong_structure(self):
        """
        Test with an incorrect recipes file where one ingredient line
        has wrong structure (quantity is missing).

        """
        with raises(ValueError) as error:
            Cookbook.from_file(path.join(getcwd(), 'files', 'recipes_wrong_structure.txt'))
            assert error.value == 'Incorrect ingredient line format for Утка по-пекински: Мед | ст.л.'

    def test_creation_wrong_quantity(self):
        """
        Test with an incorrect recipes file where one ingredient
        quantity is not a number.

        """
        with raises(TypeError) as error:
            Cookbook.from_file(path.join(getcwd(), 'files', 'recipes_wrong_quantity.txt'))
            assert error.value == 'Quantity of Молоко for Омлет must be an integer.'

    def test_shopping_list(self):
        """Tests shopping list calculation."""
        cookbook = Cookbook.from_file(path.join(getcwd(), 'files', 'recipes.txt'))
        assert cookbook.get_shopping_list(['Запеченный картофель', 'Омлет'], 2) == {
            'Картофель': {'measure': 'кг', 'quantity': 2},
            'Молоко': {'measure': 'мл', 'quantity': 200},
            'Помидор': {'measure': 'шт', 'quantity': 4},
            'Сыр гауда': {'measure': 'г', 'quantity': 200},
            'Чеснок': {'measure': 'зубч', 'quantity': 6},
            'Яйцо': {'measure': 'шт', 'quantity': 4},
        }