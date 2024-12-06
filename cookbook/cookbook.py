class Cookbook:
    """Cookbook class that can parse recipes from a file."""

    def __init__(self, cookbook):
        self.cookbook = cookbook

    @staticmethod
    def from_file(filename):
        """
        Creates a new cookbook instance by parsing a file of recipes.

        """
        cookbook = {}
        with open(filename, encoding='UTF-8') as file:
            while line := file.readline():
                # A dish name goes first in each recipe block.
                dish_name = line.strip()
                if dish_name:
                    cookbook[dish_name] = []

                    # Second goes a number of ingredients, and we
                    # should check if it's actually a positive whole
                    # number.
                    line = file.readline().strip()
                    try:
                        ingredient_count = int(line)
                    except:
                        raise TypeError(f'Count of ingredients for {dish_name} must be an integer.')
                    if ingredient_count <= 0:
                        raise ValueError(f'Count of ingredients for {dish_name} must be a positive number.')

                    for i in range(ingredient_count):
                        # Finally, we have several lines of ingredients.
                        # We ensure that each ingredient line consists
                        # of exactly 3 items separated by " | ", and
                        # that the second item is a positive whole
                        # number.
                        line = file.readline().strip()
                        parts = line.split(' | ')
                        if len(parts) != 3:
                            raise ValueError(f'Incorrect ingredient line format for {dish_name}: {line}.')
                        try:
                            quantity = int(parts[1])
                        except:
                            raise TypeError(f'Quantity of {parts[0]} for {dish_name} must be an integer.')
                        if quantity <= 0:
                            raise ValueError(f'Quantity of {parts[0]} for {dish_name} must be a positive number.')

                        # After all sane checks, add ingredient data to
                        # the cookbook.
                        cookbook[dish_name].append({
                            'ingredient_name': parts[0],
                            'quantity': quantity,
                            'measure': parts[2],
                        })
        return Cookbook(cookbook)

    def get_shopping_list(self, dishes, person_count):
        """
        Returns a shopping list (i.e. a list of ingredients to obtain)
        given a list of dishes to cook and a number of people to cook
        for.

        """
        # This is a temporary _unsorted_ shopping list.
        tmp = {}
        for dish_name in dishes:
            if dish_name in self.cookbook:
                for item in self.cookbook[dish_name]:
                    ing_name = item['ingredient_name']
                    if ing_name not in tmp:
                        tmp[ing_name] = {
                            'measure': item['measure'],
                            'quantity': 0,
                        }
                    tmp[ing_name]['quantity'] += person_count * item['quantity']
            else:
                raise ValueError(f'{dish_name} is missing from the cookbook.')
        # Sort the shopping list by ingredient names before
        # output.
        return dict(sorted(tmp.items()))
