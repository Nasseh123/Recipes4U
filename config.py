import os

class Config:

    SECRET_KEY=os.environ.get('SECRET_KEY')
    API_KEY=os.environ.get('API_KEY')

    FOOD_VIDEOS_URL=os.environ.get('FOOD_VIDEOS_URL')
    MY_API_KEY=os.environ.get('MY_API_KEY')
    

    RECIPE_API_BASE_URL ='https://api.spoonacular.com/recipes/search?query={}&apiKey={}'
    

    SEARCH_MEALPLAN = 'https://api.spoonacular.com/mealplanner/generate?timeFrame=day&apiKey=e7ba7ecc9faf4e32a68df8753b188959&includeNutrition=false'
    JOKE_URL = "https://api.spoonacular.com/food/jokes/random?apiKey=e7ba7ecc9faf4e32a68df8753b188959"
    SEARCH_RECIPES_BY_INGREDIENTS='https://api.spoonacular.com/recipes/findByIngredients?ingredients={}&number=50&apiKey={}&includeNutrition=false'
    GET_RECIPE_INFORMATION='https://api.spoonacular.com/recipes/{}/information?apiKey={}&includeNutrition=false'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options = {
'development':DevConfig,
'production':ProdConfig
}