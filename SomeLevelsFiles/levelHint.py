import arcade

class LevelHint():

    def createHint(self, text):
        # Creates the level name/hint to win
        start_x = 0
        start_y = 0
        self.hint = arcade.Text(
            text,
            start_x,
            start_y,
            arcade.csscolor.BLACK,
            32,
            128
        )