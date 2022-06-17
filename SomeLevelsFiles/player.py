import arcade
from SomeLevelsFiles.constants import scale

class Player(arcade.Sprite):
    
    def __init__(self):
        super().__init__()

        self.scale = scale
        self.textures = []

        texture = arcade.load_texture("SomeLevelsFiles/Resources/Player.png")
        self.textures.append(texture)
        texture = arcade.load_texture("SomeLevelsFiles/Resources/Player.png", flipped_horizontally=True)
        self.textures.append(texture)

        self.texture = texture

    def update(self):
        # Updates the players sprite to face the correct direction

        if self.change_x > 0:
            self.texture = self.textures[0]
        elif self.change_x < 0:
            self.texture = self.textures[1]