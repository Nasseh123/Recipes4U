import os

class Config:

    SECRET_KEY=os.environ.get('SECRET_KEY')
    API_KEY=os.environ.get('API_KEY')
    RECIPE_API_BASE_URL ='https://api.spoonacular.com/recipes/search?query={}&apiKey={}'
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options = {
'development':DevConfig,
'production':ProdConfig
}