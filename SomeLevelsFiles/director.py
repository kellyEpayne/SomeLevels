import arcade
import SomeLevelsFiles.constants as constants
from SomeLevelsFiles.textButtons import TextButtons
from SomeLevelsFiles.levelHint import LevelHint
from SomeLevelsFiles.levelsHolder import LevelsHolder

class Director(arcade.Window):
    def __init__(self):

        super().__init__(constants.screenWidth, constants.screenHeight, constants.screenTitle)

        self.movementSpeed = 4 * constants.scale
        self.jumpSpeed = 9 * constants.scale
        
        self.level = 1
        self.levelHint = LevelHint()
        # later levels will flip the movement directions. This is here so that reseting the level won't break the movement
        self.movementSpeedReversed = False
        # remove this. It made me angy
        #self.textButtons = TextButtons(self)
        

    def setup(self):

        LevelsHolder.setup(self)

    
    def on_draw(self):
        
        self.clear()
        self.scene.draw()
        #self.textButtons.manager.draw()
        self.levelHint.hint.draw()

    def on_key_press(self, key, modifiers):
        
        if key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.playerSprite.change_y = self.jumpSpeed
        elif key == arcade.key.A:
            self.playerSprite.change_x = -self.movementSpeed
        elif key == arcade.key.D:
            self.playerSprite.change_x = self.movementSpeed
        elif key == arcade.key.S:
            LevelsHolder.addFriend(self)

        if self.friend > 0:
            if key == arcade.key.UP:
                if self.friendSprite.change_y == 0:
                    self.friendSprite.change_y = self.jumpSpeed
            elif key == arcade.key.LEFT:
                self.friendSprite.change_x = -self.movementSpeed
            elif key == arcade.key.RIGHT:
                self.friendSprite.change_x = self.movementSpeed

    def on_key_release(self, key, modifiers):
    
        if key == arcade.key.W:
            self.playerSprite.change_y = 0
        elif key == arcade.key.A:
            self.playerSprite.change_x = 0
        elif key == arcade.key.D:
            self.playerSprite.change_x = 0

        if self.friend > 0:
            if key == arcade.key.UP:
                self.friendSprite.change_y = 0
            elif key == arcade.key.LEFT:
                self.friendSprite.change_x = 0
            elif key == arcade.key.RIGHT:
                self.friendSprite.change_x = 0

    def on_update(self, delta_time):
        
        LevelsHolder.update(self)

#def testMain():
#    #for testing
#    window = Director()
#    window.setup()
#    arcade.run()
#
#testMain()