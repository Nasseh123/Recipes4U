import unittest
from app.models import Recipe

class RecipeTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the recipe class
    '''

    def setUp(self):
        '''
        set up method that tests every time
        '''
        self.new_recipe = Recipe('','','','','','')

    def test_instance(self):
        self.assertTrue((isinstance(self.new_recipe,Recipe))    