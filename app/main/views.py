from flask import render_template
from . import main

@main.route('/')
def index():
    """
    """

    title="RECIPE4U"
    
    return render_template('index.html',title=title)