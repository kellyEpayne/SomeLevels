from SomeLevelsFiles.levelBase import LevelBase
from arcade import csscolor

class LevelFour(LevelBase):

    def setup(game):
        LevelBase.setup(game)
        game.levelHint.createHint("FriendS are nice")
        LevelBase.levelColor(csscolor.DARK_GREEN)
        

    def update(game):
        LevelBase.update(game)

        if game.friend > 0:
            game.doorOpen = True
            game.scene["DoorOpened"].visible = True
            game.scene["DoorClosed"].visible = False