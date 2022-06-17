from SomeLevelsFiles.levelBase import LevelBase
from arcade import csscolor

class LevelOne(LevelBase):

    def setup(game):
        LevelBase.setup(game)
        game.levelHint.createHint("Button")
        LevelBase.levelColor(csscolor.DARK_RED)
        

    def update(game):
        LevelBase.update(game)

        # The win condition for the level is to press the button atleast one time
        if game.buttonPressCount > 0:
            game.doorOpen = True
            game.scene["DoorOpened"].visible = True
            game.scene["DoorClosed"].visible = False
