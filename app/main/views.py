from flask import render_template,request,redirect,url_for
from . import main
from ..models import MealPlan
from ..requests import get_mealplan,get_joke
@main.route('/')
def index():
    """
    """

    title="RECIPE4U"
    
    return render_template('index.html',title=title)

@main.route('/mealplan',)

def mealplan():
    mealplan = get_mealplan("day")
    joke = get_joke()
    return render_template('mealplan.html', title= "Mealplans", mealplan= mealplan,joke=joke)
