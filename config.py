import os

class Config:

    SECRET_KEY=os.environ.get('SECRET_KEY')
    API_KEY=os.environ.get('API_KEY')
    FOOD_VIDEOS_URL=os.environ.get('FOOD_VIDEOS_URL')
    MY_API_KEY=os.environ.get('MY_API_KEY')
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options = {
'development':DevConfig,
'production':ProdConfig
}