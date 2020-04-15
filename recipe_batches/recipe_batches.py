#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    values = []
    for key in recipe:
        if key not in ingredients or ingredients[key] < recipe[key]:
            return 0
        else:
            values.append(ingredients[key] // recipe[key])
    return min(values)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 500, 'butter': 518, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
