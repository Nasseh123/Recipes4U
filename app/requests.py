import requests
import urllib.request, json
from .models import  MealPlan, Joke
# Getting api key
api_key = "6f8461162ff54814bf4501e258fa7a48"

base_url = None
SEARCH_MEALPLAN_URL = 'https://api.spoonacular.com/mealplanner/generate?timeFrame=day?apiKey{}'

def configure_request(app):
    global SEARCH_MEALPLAN_URL,api_key
    api_key=app.config['API_KEY']
    SEARCH_MEALPLAN_URL=app.config['SEARCH_MEALPLAN']

def get_mealplan(mealplan):
    """
    Function to consume http request and return a Mealplan class instance
    """
    get_mealplan_url= SEARCH_MEALPLAN_URL.format(mealplan,api_key)
    fetch=requests.get(get_mealplan_url)
    get_mealplan_response=fetch.json()

    return get_mealplan_response

