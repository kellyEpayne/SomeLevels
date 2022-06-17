from SomeLevelsFiles.levelBase import LevelBase
from arcade import csscolor

class LevelSix(LevelBase):

    def setup(game):
        LevelBase.setup(game)
        # The text here is backwards to give the player a hint that the movements are reversed
        game.levelHint.createHint("snioC & nottuB")
        LevelBase.levelColor(csscolor.PURPLE)

        # Since setup is called when the player is killed this if statment prevents the movements being reversed on death
        if game.movementSpeedReversed == False:
            game.movementSpeed = game.movementSpeed * -1
            game.movementSpeedReversed = True

    def update(game):
        LevelBase.update(game)

        # The win condition for the level is to press the button atleast once and collect all of the coins
        if game.buttonPressCount > 0:
            if len(game.scene["Coins"]) == 0:
                game.doorOpen = True
                game.scene["DoorOpened"].visible = True
                game.scene["DoorClosed"].visible = False
                # Once the door is opened the movement is set back to the orignal movement setup
                # The text is also flipped to give the player a hint that the backwards movements are reversed
                if game.movementSpeedReversed:
                    game.levelHint.createHint("Button & Coins")
                    game.movementSpeed = game.movementSpeed * -1
                    # Got to keep track of whether the movement is reversed
                    game.movementSpeedReversed = False
