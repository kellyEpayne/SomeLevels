import arcade
import SomeLevelsFiles.constants as constants
from SomeLevelsFiles.player import Player
from SomeLevelsFiles.friend import Friend

class LevelBase():

    def setup(game):

        mapName = "SomeLevelsFiles/Resources/TheOnlyLevel.json"

        
        tileScaling = constants.scale

        game.tile_map = arcade.load_tilemap(mapName, tileScaling, use_spatial_hash=True)
        game.scene = arcade.Scene.from_tilemap(game.tile_map)


                
        game.playerSprite = Player()
        game.playerSprite.center_x = constants.screenWidth / 2
        game.playerSprite.center_y = constants.screenHeight / 2
        game.scene.add_sprite("Player", game.playerSprite)

        game.playerscore = 0
        game.friend = 0
        game.scene["Button"].buttonPressed = False
        game.buttonPressCount = 0
        game.doorOpen = False
        game.leverstate = False

        walls = [game.scene["Walls"], game.scene["ButtonBase"]]

        game.physics_engine = arcade.PhysicsEnginePlatformer(
            game.playerSprite, walls=walls
        )

    def levelColor(color):
        arcade.set_background_color(color)

    def addFriend(game):

        if game.friend == 0:
            game.friendSprite = Friend()
            game.friendSprite.center_x = constants.screenWidth / 2
            game.friendSprite.center_y = constants.screenHeight / 2
            game.scene.add_sprite("Friend", game.friendSprite)

            game.friendPhysics = arcade.PhysicsEnginePlatformer(
            game.friendSprite, walls=game.physics_engine.walls)

            #game.physics_engine.platforms.append(game.scene["Friend"])

            #game.friendPhysics.walls.append(game.playerSprite)
            #game.physics_engine.walls.append(game.friendSprite)

            game.friend += 1       


    def update(game):

        game.physics_engine.update()
        game.playerSprite.update()
        
        coin_collect = arcade.check_for_collision_with_list(
            game.playerSprite, game.scene["Coins"]
        )

        for coin in coin_collect:
            coin.remove_from_sprite_lists()
            game.playerscore +=1

        lava_touch = arcade.check_for_collision_with_list(
            game.playerSprite, game.scene["Lava"]
        )

        if lava_touch:
            game.setup()

        if game.doorOpen:
            door_collision = arcade.check_for_collision(
                game.playerSprite, game.scene["DoorOpened"][0]
            )

            if door_collision:
                game.level += 1
                game.setup()

        if game.friend == 1:
            game.friendPhysics.update()
            game.friendSprite.update()
            LevelBase.updateFriend(game)

        LevelBase.buttonLogic(game)
        LevelBase.leverLogic(game)



    def updateFriend(game):
        coin_collect = arcade.check_for_collision_with_list(
            game.friendSprite, game.scene["Coins"]
        )

        for coin in coin_collect:
            coin.remove_from_sprite_lists()
            game.playerscore +=1

        lava_touch = arcade.check_for_collision_with_list(
            game.friendSprite, game.scene["Lava"]
        )

        if lava_touch:
            game.scene.remove_sprite_list_by_name("Friend")
            game.friend -= 1


    def leverLogic(game):
        
        if game.friend > 0:

            leverFlip = arcade.check_for_collision(
                game.playerSprite, game.scene["LeverOff"][0]
            )

            friendLeverFlip = arcade.check_for_collision(
            game.friendSprite, game.scene["LeverOff"][0]
            )

            if leverFlip or friendLeverFlip:

                if game.leverFlipable:
                    game.scene["LeverOff"].visible = not game.scene["LeverOff"].visible
                    game.scene["LeverOn"].visible = not game.scene["LeverOn"].visible

                    game.leverstate = not game.leverstate
                    game.leverFlipable = False
                    game.scene["Glass"].visible = not game.scene["Glass"].visible

                    if game.scene["Glass"].visible:
                        game.physics_engine.walls.append(game.scene["Glass"])
                        game.friendPhysics.walls.append(game.scene["Glass"])
                    else:
                        game.physics_engine.walls.remove(game.scene["Glass"])
                        game.friendPhysics.walls.remove(game.scene["Glass"])
            else:
                game.leverFlipable = True

        else:

            leverFlip = arcade.check_for_collision(
                game.playerSprite, game.scene["LeverOff"][0]
            )

            if leverFlip:

                if game.leverFlipable:
                    game.scene["LeverOff"].visible = not game.scene["LeverOff"].visible
                    game.scene["LeverOn"].visible = not game.scene["LeverOn"].visible

                    game.leverstate = not game.leverstate
                    game.leverFlipable = False
                    game.scene["Glass"].visible = not game.scene["Glass"].visible

                    if game.scene["Glass"].visible:
                        game.physics_engine.walls.append(game.scene["Glass"])
                    else:
                        game.physics_engine.walls.remove(game.scene["Glass"])
            else:
                game.leverFlipable = True

    def buttonLogic(game):

        if game.friend > 0:
            buttonPressFriend = arcade.check_for_collision(
            game.friendSprite, game.scene["Button"][0])

            buttonPressPlayer = arcade.check_for_collision(
            game.playerSprite, game.scene["Button"][0])        

            buttonPress = buttonPressPlayer or buttonPressFriend

        else:
            buttonPress = arcade.check_for_collision(
            game.playerSprite, game.scene["Button"][0]
            )        

        if buttonPress:
            game.scene["Button"].visible = False
            game.scene["Button"].buttonPressed = True
            game.buttonPressCount += 1
        else:
            game.scene["Button"].buttonPressed = False
            game.scene["Button"].visible = True