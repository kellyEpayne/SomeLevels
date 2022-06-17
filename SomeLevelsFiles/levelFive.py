from SomeLevelsFiles.levelBase import LevelBase
from arcade import csscolor

class LevelFive(LevelBase):

    def setup(game):
        LevelBase.setup(game)
        game.levelHint.createHint("Hold the door")
        LevelBase.levelColor(csscolor.DARK_BLUE)
        

    def update(game):
        LevelBase.update(game)

        # The win condition for the level is holding the button down
        # The friend cannot enter the door so they must hold the button down to let the player win
        if game.scene["Button"].buttonPressed:
            game.doorOpen = True
            game.scene["DoorOpened"].visible = True
            game.scene["DoorClosed"].visible = False
        else:
            # Closes the door if the player or friend step off the button
            game.doorOpen = False
            game.scene["DoorOpened"].visible = False
            game.scene["DoorClosed"].visible = True