import urllib.request,json
from .models import Recipe,MealPlan, Joke, SearchIngredients
import requests


# Getting api key
api_key= None
base_url = 'https://api.spoonacular.com/recipes/search?query={}&apiKey=e7ba7ecc9faf4e32a68df8753b188959'    

SEARCH_MEALPLAN_URL = 'https://api.spoonacular.com/mealplanner/generate?timeFrame=day&apiKey=e7ba7ecc9faf4e32a68df8753b188959&includeNutrition=false'
JOKE_URL = "https://api.spoonacular.com/food/jokes/random?apiKey=75c25110646a42c7a2d8abe6acb16386"
SEARCH_RECIPES_BY_INGREDIENTS_url='https://api.spoonacular.com/recipes/findByIngredients?ingredients={}&number=50&apiKey=75c25110646a42c7a2d8abe6acb16386&includeNutrition=false'

GET_RECIPE_INFORMATION_url='https://api.spoonacular.com/recipes/{}/information?apiKey=75c25110646a42c7a2d8abe6acb16386&includeNutrition=false'

def configure_request(app):
    global api_key,base_url, SEARCH_RECIPES_BY_INGREDIENTS_url,GET_RECIPE_INFORMATION_url,SEARCH_MEALPLAN_URL,JOKE_URL
    # api_key = app.config['API_KEY']
    base_url = app.config['RECIPE_API_BASE_URL']
    api_key=app.config['API_KEY']
    SEARCH_RECIPES_BY_INGREDIENTS_url=app.config['SEARCH_RECIPES_BY_INGREDIENTS']
    GET_RECIPE_INFORMATION_url=app.config['GET_RECIPE_INFORMATION']
    SEARCH_MEALPLAN_URL=app.config['SEARCH_MEALPLAN']
    JOKE_URL=app.config['JOKE_URL']
    
def get_search_by_recipe(recipe):
     """
     Function that gets the json response to our url request
     """
     print(recipe)
     get_search_by_base_url=base_url.format(recipe)
     print(get_search_by_base_url)
     fetch=requests.get(get_search_by_base_url)
     get_search_by_base_response=fetch.json()
    #  print(get_search_by_base_response)
    #  print([obj.get('id') for obj in get_search_by_base_response]) 

     return get_search_by_base_response


def process_search(recipes_list):
    '''
    Function tha processes the recipe result and convert them into a list of object
    Args:
        recipes_list: Alist of dictionaries that contain searching recipe details
    Returrns :
    recipes_results: A list of searching recipe objects  
    '''
    recipes_results = []
    for recipes_item in recipes_list:
        id = recipes_item.get('id')
        title = recipes_item.get('title')
        readyInMinutes = recipes_item.get('readyInMinutes')
        servings = recipes_item.get('servings')
        sourceUrl = recipes_item.get('sourceUrl')
        image = recipes_item.get('image')

        if  image:
            recipes_object = Recipe(id,title,readyInMinutes,servings,sourceUrl,image)
            recipes_results.append(recipes_object)

    return recipes_results   


    

    
# SEARCHBY API CALL
def get_search_by_ingredients(ingredient_name):
    """
     Function that gets the json response to our url request
    """
    get_search_by_ingredients_url=SEARCH_RECIPES_BY_INGREDIENTS_url.format(ingredient_name)
    print(get_search_by_ingredients_url)
    fetch=requests.get(get_search_by_ingredients_url)
    get_search_by_ingredients_response=fetch.json()

    # results=
    # print([obj.get('id') for obj in get_search_by_ingredients_response])
   
    
    # for recipe in get_search_by_ingredients_response:
    #     id =recipe.get("id",'default value')
    #     # print(recipe)

    return get_search_by_ingredients_response

def get_recipe_information(id):
    """
    Function that gets the json response to our url request
    """
    get_recipe_information_url=GET_RECIPE_INFORMATION_url.format(id,api_key)
    print(get_recipe_information_url)
    fetch=requests.get(get_recipe_information_url)
    get_recipe_information_response=fetch.json()
    print(get_recipe_information_response)

    return get_recipe_information_response
 
def get_mealplan(mealplan):
    """
    Function to consume http request and return a Mealplan class instance
    """
    get_mealplan_url= SEARCH_MEALPLAN_URL.format(mealplan,api_key)
    fetch=requests.get(get_mealplan_url)
    get_mealplan_response=fetch.json()
    
    return get_mealplan_response

def get_joke():
    """
    Function to consume http request and return a Mealplan class instance
    """
    response = requests.get(JOKE_URL).json()

    random_joke = Joke(response.get("text"))
    return random_joke


