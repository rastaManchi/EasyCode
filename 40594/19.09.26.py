class BallController():
    def __init__(self):
        self.__owner = None

    def getOwner(self):
        print(self.__owner)

    def setOwner(self):
        self.__owner = 'Булат'

ball = BallController()
ball.setOwner()
ball.getOwner()