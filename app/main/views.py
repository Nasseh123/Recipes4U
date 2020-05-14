

from flask import render_template,request,redirect,url_for,flash
from . import main
from ..models import MealPlan
from ..requests import get_search_by_ingredients,get_recipe_information,get_mealplan,get_joke,get_search_by_recipe

from ..requests import search_food_videos, get_random_videos

@main.route('/food/videos/search')
def search_food_video():
    """
    """

    search_videos = request.args.get('video_query')
    videos = search_food_videos(search_videos)
    
    return render_template('food_videos.html',videos=videos)


@main.route('/recipes/random')
def random_videos():

    recipes = get_random_videos()

    return render_template('random_recipes.html',recipes=recipes)

@main.route('/')
def index():
    title="RECIPE4U"
    search_by_recipe=request.args.get('general_query')
    search_by_ingredients=request.args.get('ingredient_query')
    if search_by_recipe:
        return redirect(url_for('.search_by_recipe',recipe_name=search_by_recipe))
    elif search_by_ingredients:
        return redirect(url_for('.search_by_ingredients',ingredient_name=search_by_ingredients))
    else:
        # flash('OOPS!Sorry No recipe matched with your inputed ingredients')
        return render_template('index.html',title=title)
    
    return render_template('index.html',title=title)
@main.route('/search/<recipe_name>')
def search_by_recipe(recipe_name):
    """
    view function to display recipes by ingredients
    """
    # recipe_name_list=ingredient_name.split(" ")
    # recipe_name_format="+".join(recipe_name_list)
    
    searched_recipes=get_search_by_recipe(recipe_name)
    
    return render_template('searches.html',recipes=searched_recipes) 
    
    

   
@main.route('/search/ingredients/<ingredient_name>')
def search_by_ingredients(ingredient_name):
    """
    view function to display recipes by ingredients
    """
    # recipe_name_list=ingredient_name.split(" ")
    # recipe_name_format="+".join(recipe_name_list)
    searched_recipes=get_search_by_ingredients(ingredient_name)
    return render_template('search.html',recipes=searched_recipes)

@main.route('/recipe/information/<id>')
def get_information(id):
    """
    """

    moreinfo=get_recipe_information(id)
    return render_template ('more_recipe_information.html',moreinfo=moreinfo)


@main.route('/mealplan',)

def mealplan():
    mealplan = get_mealplan("day")
    joke = get_joke()
    return render_template('mealplan.html', title= "Mealplans", mealplan= mealplan,joke=joke)
    

