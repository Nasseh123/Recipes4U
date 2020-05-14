import unittest
from app.models import SearchIngredients


class searchIngredientsTest(unittest.TestCase):
    """
    Test class to test behaviour of searchingredients class
    """
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_searchingredient=SearchIngredients(124,'Fried Chicken','https://spoonacular.com/recipeImages/78752-312x231.jpg')

    def test_instance(self):
        self.assertTrue (isinstance(self.new_searchingredient,SearchIngredients))