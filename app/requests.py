import urllib.request,json
from .models import  MealPlan
# Getting api key
api_key = "6f8461162ff54814bf4501e258fa7a48"

url = "https://api.spoonacular.com/mealplanner/generate?apiKey={}"

def get_mealplan():
    """
    Function to consume http request and return a Mealplan class instance
    """
    response = requests.get(url).json()

    meal_result = MealPlan(response.get("title"),response.get("readyInMinutes"),response.get("servings"),response.get("sourceUrl"))
    return meal_result