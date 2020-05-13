import urllib.request,json
import requests
from .models import SearchIngredients

# Getting api key
api_key = None
# Getting the movie base url
base_url = None
SEARCH_RECIPES_BY_INGREDIENTS_url=None

def configure_request(app):
    global SEARCH_RECIPES_BY_INGREDIENTS_url,api_key

    api_key=app.config['API_KEY']
    SEARCH_RECIPES_BY_INGREDIENTS_url=app.config['SEARCH_RECIPES_BY_INGREDIENTS']

# SEARCHBY API CALL
def get_search_by_ingredients(ingredients):
    """
     Function that gets the json response to our url request
    """
    get_search_by_ingredients_url=SEARCH_RECIPES_BY_INGREDIENTS_url.format(ingredients,api_key)

    fetch=requests.get(get_search_by_ingredients_url)
    get_search_by_ingredients_response=fetch.json()

    # results=
    # print([obj.get('id') for obj in get_search_by_ingredients_response])
    # for recipe in get_search_by_ingredients_response:
    #     id =recipe.get("id",'default value')
    #     print(recipe)

    return get_search_by_ingredients_response
