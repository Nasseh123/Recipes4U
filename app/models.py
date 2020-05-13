class Recipe:
    '''
    Recipe class to define recipe objects
    '''

    def __init__(self,id,title,readyInMinutes,servings,sourceUrl,image):
        self.id = id
        self.title= title
        self.readyInMinutes = readyInMinutes
        self.servings = servings
        self.sourceUrl = sourceUrl
        self.image = image