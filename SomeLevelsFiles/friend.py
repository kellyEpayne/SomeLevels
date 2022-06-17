import arcade
from SomeLevelsFiles.constants import scale

class Friend(arcade.Sprite):
    
    def __init__(self):
        # The only difference between player and friend is the image used
        super().__init__()

        self.scale = scale
        self.textures = []

        texture = arcade.load_texture("SomeLevelsFiles/Resources/Friend.png")
        self.textures.append(texture)
        texture = arcade.load_texture("SomeLevelsFiles/Resources/Friend.png", flipped_horizontally=True)
        self.textures.append(texture)

        self.texture = texture

    def update(self):
        # Updates the friend sprite to face the correct direction

        if self.change_x > 0:
            self.texture = self.textures[0]
        elif self.change_x < 0:
            self.texture = self.textures[1]
