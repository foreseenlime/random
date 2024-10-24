## This code uses the Microsoft version of microbit Python
## That means it is different from normal python and uses different things

def on_button_pressed_a():
    player.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global shoot, score
    shoot = game.create_sprite(player.get(LedSpriteProperty.X),
        player.get(LedSpriteProperty.Y))
    for index in range(4):
        shoot.change(LedSpriteProperty.Y, -1)
        basic.pause(20)
        if shoot.is_touching(enemy):
            enemy.delete()
            score += 1
    shoot.delete()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    player.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

score = 0
enemy: game.LedSprite = None
shoot: game.LedSprite = None
player: game.LedSprite = None
player = game.create_sprite(2, 4)

def on_forever():
    global enemy
    enemy = game.create_sprite(randint(0, 4), 0)
    for index2 in range(4):
        enemy.change(LedSpriteProperty.Y, 1)
        basic.pause(500)
        if enemy.is_touching(player):
            game.game_over()
    enemy.delete()
basic.forever(on_forever)
