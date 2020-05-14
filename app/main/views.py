from flask import render_template, request
from . import main

from ..requests import search_food_videos, get_random_videos

@main.route('/food/videos/search')
def search_food_video():
    """
    """

    search_videos = request.args.get('video_query')
    videos = search_food_videos(search_videos)
    
    return render_template('food_videos.html',videos=videos)


