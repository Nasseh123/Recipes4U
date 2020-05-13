import requests
import urllib.request, json
from .models import  MealPlan, Joke
# Getting api key
api_key= "e7ba7ecc9faf4e32a68df8753b188959"
base_url = None
SEARCH_MEALPLAN_URL = 'https://api.spoonacular.com/mealplanner/generate?timeFrame=day&apiKey=e7ba7ecc9faf4e32a68df8753b188959&includeNutrition=false'
JOKE_URL = "https://api.spoonacular.com/food/jokes/random?apiKey=e7ba7ecc9faf4e32a68df8753b188959"
def configure_request(app):
    global SEARCH_MEALPLAN_URL,api_key,JOKE_URL
    api_key=app.config['API_KEY']
    SEARCH_MEALPLAN_URL=app.config['SEARCH_MEALPLAN']
    JOKE_URL=app.config['JOKE_URL']
    
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