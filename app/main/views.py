from flask import render_template
from . import main
from ..requests import get_search_by_ingredients

@main.route('/')
def index():
    """
    """
    ingredients=get_search_by_ingredients('chicken')
    title="RECIPE4U"
    
    return render_template('index.html',title=title,ingredients=ingredients)