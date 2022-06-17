from SomeLevelsFiles.levelBase import LevelBase
from SomeLevelsFiles.levelOne import LevelOne
from SomeLevelsFiles.levelTwo import LevelTwo
from SomeLevelsFiles.levelThree import LevelThree
from SomeLevelsFiles.levelFour import LevelFour
from SomeLevelsFiles.levelFive import LevelFive
from SomeLevelsFiles.levelSix import LevelSix

class LevelsHolder():
    
    def setup(game):

        match game.level:
            case 1:
                LevelOne.setup(game)
            case 2:
                LevelTwo.setup(game)
            case 3:
                LevelThree.setup(game)
            case 4:
                LevelFour.setup(game)
            case 5:
                LevelFive.setup(game)
            case 6:
                LevelSix.setup(game)
            case _:
                game.level = 1
                game.setup()
                

    def update(game):

        match game.level:
            case 1:
                LevelOne.update(game)
            case 2:
                LevelTwo.update(game)
            case 3:
                LevelThree.update(game)
            case 4:
                LevelFour.update(game)
            case 5:
                LevelFive.update(game)
            case 6:
                LevelSix.update(game)
                
    def addFriend(game):
        
        LevelBase.addFriend(game)