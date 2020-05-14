
class MealPlan:

    """
    Adds mealplan class derived from the Api
    """


    def __init__(self,id,title,readyInMinutes,servings,sourceUrl):
        self.id = id
        self.title = title
        self.readyInMinutes = readyInMinutes
        self.servings = servings
        self.sourceUrl = sourceUrl

class Joke:

    """
    Adds joke class derived from Api
    """

    def __init__(self,text):
        self.text = text
        
class SearchIngredients:
    """
    """

    def __init__(self,id,title,image):
        self.id=id
        self.title=title
        self.image=image

