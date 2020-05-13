from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_search_by_recipe

@main.route('/')
def index():
    """
    """
    search = get_search_by_recipe('chicken')
    title="RECIPE4U"
    search_by_recipe=request.args.get('general_query')

    if search_by_recipe:
        return redirect(url_for('.search_by_recipe',recipe_name=search_by_recipe))
    else: 
        return render_template('index.html',title=title,search = search)

@main.route('/search/<recipe_name>')
def search_by_recipe(recipe_name):
    """
    view function to display recipes by ingredients
    """
    # recipe_name_list=ingredient_name.split(" ")
    # recipe_name_format="+".join(recipe_name_list)
    
    searched_recipes=get_search_by_recipe(recipe_name)
    
    return render_template('search.html',recipes=searched_recipes) 