import urllib.request,json
from .models import Recipe
import requests

# Recipe = recipe.Recipe

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):

    global api_key,base_url
    api_key = app.config['API_KEY']
    base_url = app.config['RECIPE_API_BASE_URL']

    # pass
def get_search_by_recipe(recipe):
     """
     Function that gets the json response to our url request
     """
     get_search_by_base_url=base_url.format(recipe,api_key)
     print(get_search_by_base_url)
     fetch=requests.get(get_search_by_base_url)
     get_search_by_base_response=fetch.json()
     print(get_search_by_base_response)
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