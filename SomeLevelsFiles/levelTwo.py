from SomeLevelsFiles.levelBase import LevelBase
from arcade import csscolor

class LevelTwo(LevelBase):

    def setup(game):
        LevelBase.setup(game)
        game.levelHint.createHint("Coins")
        LevelBase.levelColor(csscolor.DARK_ORANGE)

    def update(game):
        LevelBase.update(game)

        if len(game.scene["Coins"]) == 0:
            game.doorOpen = True
            game.scene["DoorOpened"].visible = True
            game.scene["DoorClosed"].visible = False

