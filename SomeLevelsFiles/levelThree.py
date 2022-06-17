from SomeLevelsFiles.levelBase import LevelBase
from arcade import csscolor

class LevelThree(LevelBase):

    def setup(game):
        LevelBase.setup(game)
        game.levelHint.createHint("Button & Coins")
        LevelBase.levelColor(csscolor.GOLD)

    def update(game):
        LevelBase.update(game)

        # The win condition for the level is to press the button atleast once and to collect all the coins
        if game.buttonPressCount > 0:
            if len(game.scene["Coins"]) == 0:
                game.doorOpen = True
                game.scene["DoorOpened"].visible = True
                game.scene["DoorClosed"].visible = False