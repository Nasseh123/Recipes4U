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