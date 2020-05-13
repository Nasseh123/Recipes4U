import os

class Config:

    SECRET_KEY=os.environ.get('SECRET_KEY')
    API_KEY=os.environ.get('API_KEY')
    SEARCH_RECIPES_BY_INGREDIENTS='https://api.spoonacular.com/recipes/findByIngredients?ingredients={}&number=50&apiKey={}&includeNutrition=false'
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options = {
'development':DevConfig,
'production':ProdConfig
}