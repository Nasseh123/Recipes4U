import os

class Config:

    SECRET_KEY=os.environ.get('SECRET_KEY')
    API_KEY=os.environ.get('API_KEY')
    GET_MEALPLAN = "https://api.spoonacular.com/mealplanner/generate?timeFrame={}?apiKey={}"
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options = {
'development':DevConfig,
'production':ProdConfig
}