from flask import render_template
from . import main
from .models import MealPlan
from ..requests import get_mealplan
@main.route('/')
def index():
    """
    """

    title="RECIPE4U"
    
    return render_template('index.html',title=title)

@main.route('/mealplan')
def mealplan():
    mealplan = get_mealplan()
    return render_template('mealplan.html', title= "Mealplans", mealplan= mealplan)