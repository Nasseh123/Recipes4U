from flask import render_template,request,redirect,url_for,flash
from . import main
from ..requests import get_search_by_ingredients,get_recipe_information

@main.route('/')
def index():
    """
    """
    
    # ingredients=get_search_by_ingredients('chicken')
    title="RECIPE4U"
    search_by_ingredients=request.args.get('ingredient_query')

    if search_by_ingredients:
        return redirect(url_for('.search_by_ingredients',ingredient_name=search_by_ingredients))
    else:
        # flash('OOPS!Sorry No recipe matched with your inputed ingredients')
        return render_template('index.html',title=title)

@main.route('/search/<ingredient_name>')
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