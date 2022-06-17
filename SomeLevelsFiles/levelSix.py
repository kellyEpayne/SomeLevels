from SomeLevelsFiles.levelBase import LevelBase
from arcade import csscolor

class LevelSix(LevelBase):

    def setup(game):
        LevelBase.setup(game)
        game.levelHint.createHint("snioC & nottuB")
        LevelBase.levelColor(csscolor.PURPLE)
        if game.movementSpeedReversed == False:
            game.movementSpeed = game.movementSpeed * -1
            game.movementSpeedReversed = True

    def update(game):
        LevelBase.update(game)

        if game.buttonPressCount > 0:
            if len(game.scene["Coins"]) == 0:
                game.doorOpen = True
                game.scene["DoorOpened"].visible = True
                game.scene["DoorClosed"].visible = False
                if game.movementSpeedReversed:
                    game.levelHint.createHint("Button & Coins")
                    game.movementSpeed = game.movementSpeed * -1
                    game.movementSpeedReversed = False
