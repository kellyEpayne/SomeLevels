from SomeLevelsFiles.levelBase import LevelBase
from arcade import csscolor

class LevelFive(LevelBase):

    def setup(game):
        LevelBase.setup(game)
        game.levelHint.createHint("Hold the door")
        LevelBase.levelColor(csscolor.DARK_BLUE)
        

    def update(game):
        LevelBase.update(game)

        if game.scene["Button"].buttonPressed:
            game.doorOpen = True
            game.scene["DoorOpened"].visible = True
            game.scene["DoorClosed"].visible = False
        else:
            game.doorOpen = False
            game.scene["DoorOpened"].visible = False
            game.scene["DoorClosed"].visible = True