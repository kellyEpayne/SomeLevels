import arcade
import SomeLevelsFiles.constants as constants
from SomeLevelsFiles.levelHint import LevelHint
from SomeLevelsFiles.levelsHolder import LevelsHolder

class Director(arcade.Window):

    def __init__(self):

        super().__init__(constants.screenWidth, constants.screenHeight, constants.screenTitle)

        self.movementSpeed = 4 * constants.scale
        self.jumpSpeed = 9 * constants.scale
        
        # The game starts counting from level 1
        self.level = 1
        self.levelHint = LevelHint()

        # later levels will flip the movement directions. This is here so that reseting the level won't break the movement
        self.movementSpeedReversed = False
        

    def setup(self):
        # LevelsHolder keeps track of whcih levelNumbers setup we are using
        LevelsHolder.setup(self)

    
    def on_draw(self):

        #Draws everthing to the screen
        self.clear()
        self.scene.draw()
        self.levelHint.hint.draw()

    def on_key_press(self, key, modifiers):
        
        # Players controls
        if key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.playerSprite.change_y = self.jumpSpeed
        elif key == arcade.key.A:
            self.playerSprite.change_x = -self.movementSpeed
        elif key == arcade.key.D:
            self.playerSprite.change_x = self.movementSpeed
        elif key == arcade.key.S:
            LevelsHolder.addFriend(self)

        # Player twos controls - Player two might not exist
        # the friend variable keeps track if player two exists
        if self.friend > 0:
            if key == arcade.key.UP:
                if self.friendSprite.change_y == 0:
                    self.friendSprite.change_y = self.jumpSpeed
            elif key == arcade.key.LEFT:
                self.friendSprite.change_x = -self.movementSpeed
            elif key == arcade.key.RIGHT:
                self.friendSprite.change_x = self.movementSpeed

    def on_key_release(self, key, modifiers):
    
        # Similar to on key press
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
        # just like setup but for the update function
        LevelsHolder.update(self)

#def testMain():
#    #for testing
#    window = Director()
#    window.setup()
#    arcade.run()
#
#testMain()