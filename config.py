import os

class Config:

    SECRET_KEY=os.environ.get('SECRET_KEY')
    API_KEY=os.environ.get('API_KEY')
    SEARCH_MEALPLAN = 'https://api.spoonacular.com/mealplanner/generate?timeFrame=day&apiKey=e7ba7ecc9faf4e32a68df8753b188959&includeNutrition=false'
    JOKE_URL = "https://api.spoonacular.com/food/jokes/random?apiKey=e7ba7ecc9faf4e32a68df8753b188959"
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options = {
'development':DevConfig,
'production':ProdConfig
}