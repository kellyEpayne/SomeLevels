from SomeLevelsFiles.levelBase import LevelBase
from SomeLevelsFiles.levelOne import LevelOne
from SomeLevelsFiles.levelTwo import LevelTwo
from SomeLevelsFiles.levelThree import LevelThree
from SomeLevelsFiles.levelFour import LevelFour
from SomeLevelsFiles.levelFive import LevelFive
from SomeLevelsFiles.levelSix import LevelSix

class LevelsHolder():
    # Holds on to all the levels
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
                # If game.level doesn't match one of these cases then the level will be set to one and called again
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
            # The is no end case for this one because this point shouldn't be reached outside of the range
                
    def addFriend(game):

        # This function is call addFriend from LevelBase        
        LevelBase.addFriend(game)