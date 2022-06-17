import arcade
import SomeLevelsFiles.constants as constants
from SomeLevelsFiles.player import Player
from SomeLevelsFiles.friend import Friend

class LevelBase():

    def setup(game):

        # Lines 11 to 17 create the map the game is using
        mapName = "SomeLevelsFiles/Resources/TheOnlyLevel.json"

        
        tileScaling = constants.scale

        game.tile_map = arcade.load_tilemap(mapName, tileScaling, use_spatial_hash=True)
        game.scene = arcade.Scene.from_tilemap(game.tile_map)


        # Spawns in the player                
        game.playerSprite = Player()
        game.playerSprite.center_x = constants.screenWidth / 2
        game.playerSprite.center_y = constants.screenHeight / 2 - 32 * constants.scale
        game.scene.add_sprite("Player", game.playerSprite)

        # Sets and resets the level to the default state
        game.friend = 0
        game.scene["Button"].buttonPressed = False
        game.buttonPressCount = 0
        game.doorOpen = False
        game.leverstate = False

        # Lines 34 to 38 sets up the physics_engine for the game
        walls = [game.scene["Walls"], game.scene["ButtonBase"]]

        game.physics_engine = arcade.PhysicsEnginePlatformer(
            game.playerSprite, walls=walls
        )

    def levelColor(color):
        # This function is used to set the color of the background
        arcade.set_background_color(color)

    def addFriend(game):

        # Creates the second Player
        if game.friend == 0:
            game.friendSprite = Friend()
            game.friendSprite.center_x = constants.screenWidth / 2
            game.friendSprite.center_y = constants.screenHeight / 2 - 32 * constants.scale
            game.scene.add_sprite("Friend", game.friendSprite)

            # Creates a physics engine for the Friend based on the players current physics engine
            game.friendPhysics = arcade.PhysicsEnginePlatformer(
            game.friendSprite, walls=game.physics_engine.walls)

            # Prevents the player from spawning more friends
            game.friend += 1       


    def update(game):

        # Update the physics for the player and switches the player sprite based on input
        game.physics_engine.update()
        game.playerSprite.update()
        
        # Lines 68 to 73 Players interactions with coins - they collect them
        coin_collect = arcade.check_for_collision_with_list(
            game.playerSprite, game.scene["Coins"]
        )

        for coin in coin_collect:
            coin.remove_from_sprite_lists()

        # Line 76 to 81 - If the player touches lava they are died. Reset the level
        lava_touch = arcade.check_for_collision_with_list(
            game.playerSprite, game.scene["Lava"]
        )

        if lava_touch:
            game.setup()

        # Lines 84 to 91 - If the door is open check to see if the player has entered the door. If they have move on to the next level
        if game.doorOpen:
            door_collision = arcade.check_for_collision(
                game.playerSprite, game.scene["DoorOpened"][0]
            )

            if door_collision:
                game.level += 1
                game.setup()

        # If their is a second player do the friends physics and checks
        if game.friend == 1:
            game.friendPhysics.update()
            game.friendSprite.update()
            LevelBase.updateFriend(game)

        LevelBase.buttonLogic(game)
        LevelBase.leverLogic(game)



    def updateFriend(game):
        # Lines 106 to 111 - Friend can collect coins like the player
        coin_collect = arcade.check_for_collision_with_list(
            game.friendSprite, game.scene["Coins"]
        )

        for coin in coin_collect:
            coin.remove_from_sprite_lists()

        # Lines 114 to 120 - If the friend dies remove them from the game
        lava_touch = arcade.check_for_collision_with_list(
            game.friendSprite, game.scene["Lava"]
        )

        if lava_touch:
            game.scene.remove_sprite_list_by_name("Friend")
            game.friend -= 1


    def leverLogic(game):
        # Levers got weird when the friend was added sperated leverLogic to make debugging easier

        if game.friend > 0:
            # When there is a friend
            leverFlip = arcade.check_for_collision(
                game.playerSprite, game.scene["LeverOff"][0]
            )

            friendLeverFlip = arcade.check_for_collision(
            game.friendSprite, game.scene["LeverOff"][0]
            )

            # Check to see if either is touching the lever
            if leverFlip or friendLeverFlip:

                if game.leverFlipable:
                    game.scene["LeverOff"].visible = not game.scene["LeverOff"].visible
                    game.scene["LeverOn"].visible = not game.scene["LeverOn"].visible

                    game.leverstate = not game.leverstate
                    # If someone has flipped the lever do not let them flip it again till they have moved away
                    game.leverFlipable = False
                    game.scene["Glass"].visible = not game.scene["Glass"].visible

                    # Enabling and disabling the glass barrier
                    if game.scene["Glass"].visible:
                        game.physics_engine.walls.append(game.scene["Glass"])
                        game.friendPhysics.walls.append(game.scene["Glass"])
                    else:
                        game.physics_engine.walls.remove(game.scene["Glass"])
                        game.friendPhysics.walls.remove(game.scene["Glass"])
            else:
                # If no one is touching the lever it is flipable
                game.leverFlipable = True

        else:
            # Without friend
            leverFlip = arcade.check_for_collision(
                game.playerSprite, game.scene["LeverOff"][0]
            )

            # If touching the lever
            if leverFlip:

                if game.leverFlipable:
                    game.scene["LeverOff"].visible = not game.scene["LeverOff"].visible
                    game.scene["LeverOn"].visible = not game.scene["LeverOn"].visible

                    game.leverstate = not game.leverstate
                    # Prevents the player from activating the lever again till they move away
                    game.leverFlipable = False
                    game.scene["Glass"].visible = not game.scene["Glass"].visible

                    # Enabling and disabling the glass barrier
                    if game.scene["Glass"].visible:
                        game.physics_engine.walls.append(game.scene["Glass"])
                    else:
                        game.physics_engine.walls.remove(game.scene["Glass"])
            else:
                # If the player is not touching the lever it is flipable
                game.leverFlipable = True

    def buttonLogic(game):
        # Same deal as leverLogic

        if game.friend > 0:
            # Checks for the friend or player touching the button
            buttonPressFriend = arcade.check_for_collision(
            game.friendSprite, game.scene["Button"][0])

            buttonPressPlayer = arcade.check_for_collision(
            game.playerSprite, game.scene["Button"][0])        

            buttonPress = buttonPressPlayer or buttonPressFriend

        else:
            # Check for the player touching the button
            buttonPress = arcade.check_for_collision(
            game.playerSprite, game.scene["Button"][0]
            )        

        # buttonPressed and buttonPressCount are used to control different logic in the actual levers
        # buttonPressed keeps track of if the button is being held down
        # buttonPressCount keeps track of how many times the button has be pressed
        if buttonPress:
            game.scene["Button"].visible = False
            game.scene["Button"].buttonPressed = True
            game.buttonPressCount += 1
        else:
            game.scene["Button"].buttonPressed = False
            game.scene["Button"].visible = True