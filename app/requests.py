import urllib.request,json
import requests

# Getting api key
my_api_key = None
# Getting the movie base url
base_url = None

FOOD_VIDEOS_URL=None

def configure_request(app):
    global FOOD_VIDEOS_URL, my_api_key

    my_api_key=app.config['MY_API_KEY']
    FOOD_VIDEOS_URL=app.config['FOOD_VIDEOS_URL']


def search_food_videos(food):
    # search_food_videos_url = FOOD_VIDEOS_URL.format(food, my_api_key)
    search_food_videos_url = f'https://api.spoonacular.com/food/videos/search?query={food}&number=10&apiKey=b3e0e6046d7b44848276665bf840228f'

    fetch = requests.get(search_food_videos_url)
    get_food_videos = fetch.json()


     

    return get_food_videos
    

def get_random_videos():

    random_food_videos_url = 'https://api.spoonacular.com/recipes/random?number=10&tags=vegetarian,dessert&apiKey=b3e0e6046d7b44848276665bf840228f'

    fetch = requests.get(random_food_videos_url)
    get_random_videos = fetch.json()

    return get_random_videos

