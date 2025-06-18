def on_button_pressed():
    global projectile_vx, projectile_vy
    if controller.left.is_pressed() or controller.right.is_pressed() or (controller.up.is_pressed() or controller.down.is_pressed()):
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . f f f f . . . . . .
                    . . . . f f f 2 2 f f f . . . .
                    . . . f f f 2 2 2 2 f f f . . .
                    . . f f f e e e e e e f f f . .
                    . . f f e 2 2 2 2 2 2 e e f . .
                    . . f e 2 f f f f f f 2 e f . .
                    . . f f f f e e e e f f f f . .
                    . f f e f b f 4 4 f b f e f f .
                    . f e e 4 1 f d d f 1 4 e e f .
                    . . f e e d d d d d d e e f . .
                    . . . f e e 4 4 4 4 e e f . . .
                    . . e 4 f 2 2 2 2 2 2 f 4 e . .
                    . . 4 d f 2 2 2 2 2 2 f d 4 . .
                    . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                    . . . . . f f f f f f . . . . .
                    . . . . . f f . . f f . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f f f . . . . . .
                    . . . . f f f 2 2 f f f . . . .
                    . . . f f f 2 2 2 2 f f f . . .
                    . . f f f e e e e e e f f f . .
                    . . f f e 2 2 2 2 2 2 e e f . .
                    . f f e 2 f f f f f f 2 e f f .
                    . f f f f f e e e e f f f f f .
                    . . f e f b f 4 4 f b f e f . .
                    . . f e 4 1 f d d f 1 4 e f . .
                    . . . f e 4 d d d d 4 e f e . .
                    . . f e f 2 2 2 2 e d d 4 e . .
                    . . e 4 f 2 2 2 2 e d d e . . .
                    . . . . f 4 4 5 5 f e e . . . .
                    . . . . f f f f f f f . . . . .
                    . . . . f f f . . . . . . . . .
                    """),
                img("""
                    . . . . . . f f f f . . . . . .
                    . . . . f f f 2 2 f f f . . . .
                    . . . f f f 2 2 2 2 f f f . . .
                    . . f f f e e e e e e f f f . .
                    . . f f e 2 2 2 2 2 2 e e f . .
                    . . f e 2 f f f f f f 2 e f . .
                    . . f f f f e e e e f f f f . .
                    . f f e f b f 4 4 f b f e f f .
                    . f e e 4 1 f d d f 1 4 e e f .
                    . . f e e d d d d d d e e f . .
                    . . . f e e 4 4 4 4 e e f . . .
                    . . e 4 f 2 2 2 2 2 2 f 4 e . .
                    . . 4 d f 2 2 2 2 2 2 f d 4 . .
                    . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
                    . . . . . f f f f f f . . . . .
                    . . . . . f f . . f f . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . f f f f . . . . . .
                    . . . . f f f 2 2 f f f . . . .
                    . . . f f f 2 2 2 2 f f f . . .
                    . . f f f e e e e e e f f f . .
                    . . f e e 2 2 2 2 2 2 e f f . .
                    . f f e 2 f f f f f f 2 e f f .
                    . f f f f f e e e e f f f f f .
                    . . f e f b f 4 4 f b f e f . .
                    . . f e 4 1 f d d f 1 4 e f . .
                    . . e f e 4 d d d d 4 e f . . .
                    . . e 4 d d e 2 2 2 2 f e f . .
                    . . . e d d e 2 2 2 2 f 4 e . .
                    . . . . e e f 5 5 4 4 f . . . .
                    . . . . . f f f f f f f . . . .
                    . . . . . . . . . f f f . . . .
                    """)],
            100,
            False)
        projectile_vx = 0
        projectile_vy = 0
        if controller.left.is_pressed():
            projectile_vx = 0 - projectile_speed
        if controller.right.is_pressed():
            projectile_vx = projectile_speed
        if controller.up.is_pressed():
            projectile_vy = 0 - projectile_speed
        if controller.down.is_pressed():
            projectile_vy = projectile_speed
controller.any_button.on_event(ControllerButtonEvent.PRESSED, on_button_pressed)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . 4 4 . . . . . . .
            . . . . . . 4 5 5 4 . . . . . .
            . . . . . . 2 5 5 2 . . . . . .
            . . . . . . . 2 2 . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        mySprite,
        projectile_vx,
        projectile_vy)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(otherSprite, effects.ashes, 200)
    sprites.destroy(sprite)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

projectile: Sprite = None
baddy: Sprite = None
projectile_vx = 0
projectile_vy = 0
projectile_speed = 0
mySprite: Sprite = None
sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
tiles.set_current_tilemap(tilemap("""
    level
    """))
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . .
        . . . . f f f 2 2 f f f . . . .
        . . . f f f 2 2 2 2 f f f . . .
        . . f f f e e e e e e f f f . .
        . . f f e 2 2 2 2 2 2 e e f . .
        . . f e 2 f f f f f f 2 e f . .
        . . f f f f e e e e f f f f . .
        . f f e f b f 4 4 f b f e f f .
        . f e e 4 1 f d d f 1 4 e e f .
        . . f e e d d d d d d e e f . .
        . . . f e e 4 4 4 4 e e f . . .
        . . e 4 f 2 2 2 2 2 2 f 4 e . .
        . . 4 d f 2 2 2 2 2 2 f d 4 . .
        . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
        . . . . . f f f f f f . . . . .
        . . . . . f f . . f f . . . . .
        """),
    SpriteKind.player)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
projectile_speed = 200
projectile_vy = 0 - projectile_speed
projectile_vx = 0
mySprite.set_position(80, 990)
for index in range(10):
    baddy = sprites.create(img("""
            . . . . . . c c c c c c . . . .
            . . . . . c 6 7 7 7 7 6 c . . .
            . . . . c 7 7 7 7 7 7 7 7 c . .
            . . . c 6 7 7 7 7 7 7 7 7 6 c .
            . . . c 7 7 7 c 6 6 6 6 c 7 c .
            . . . f 7 7 7 6 f 6 6 f 6 7 f .
            . . . f 7 7 7 7 7 7 7 7 7 7 f .
            . . c f 6 7 7 c 6 7 7 7 7 f . .
            . c 7 7 f 6 7 7 c c c c f . . .
            c 7 7 7 7 f c 6 7 7 7 2 7 c . .
            c c 6 7 7 6 c f c 7 7 2 7 7 c .
            . . c 6 6 6 c c f 6 7 1 1 1 1 c
            . . f 6 6 6 6 c 6 6 1 1 1 1 1 f
            . . f c 6 6 6 6 6 1 1 1 1 1 6 f
            . . . f 6 6 6 1 1 1 1 1 1 6 f .
            . . . . f c c c c c c c c c . .
            """),
        SpriteKind.enemy)
    baddy.set_position(randint(0, 160), randint(60, 850))
    baddy.follow(mySprite, 5)
    animation.run_image_animation(baddy,
        [img("""
                . . . . . . c c c c c c . . . .
                . . . . . c 6 7 7 7 7 6 c . . .
                . . . . c 7 7 7 7 7 7 7 7 c . .
                . . . c 6 7 7 7 7 7 7 7 7 6 c .
                . . . c 7 7 7 c 6 6 6 6 c 7 c .
                . . . f 7 7 7 6 f 6 6 f 6 7 f .
                . . . f 7 7 7 7 7 7 7 7 7 7 f .
                . . c f 6 7 7 c 6 7 7 7 7 f . .
                . c 7 7 f 6 7 7 c c c c f . . .
                c 7 7 7 7 f c 6 7 7 7 2 7 c . .
                c c 6 7 7 6 c f c 7 7 2 7 7 c .
                . . c 6 6 6 c c f 6 7 1 1 1 1 c
                . . f 6 6 6 6 c 6 6 1 1 1 1 1 f
                . . f c 6 6 6 6 6 1 1 1 1 1 6 f
                . . . f 6 6 6 1 1 1 1 1 1 6 f .
                . . . . f c c c c c c c c c . .
                """),
            img("""
                . . . . . . . c c c c c c . . .
                . . . . . . c 6 7 7 7 7 6 c . .
                . . . . . c 7 7 7 7 7 7 7 7 c .
                . . . . c 6 7 7 7 7 7 7 7 7 6 c
                . . . . c 7 7 7 c 6 6 6 6 c 7 c
                . . . . f 7 7 7 6 f 6 6 f 6 7 f
                . . . . f 7 7 7 7 7 7 7 7 7 7 f
                . . . . f 6 7 7 c 6 7 7 7 7 f .
                . . c c c f 6 7 7 c c c c f . .
                . c 7 7 7 c c f 7 7 7 2 6 c . .
                c 7 7 7 7 6 f c 7 7 2 7 7 6 c .
                c c c 6 6 6 c 6 6 7 1 1 1 1 c .
                . . c 6 6 6 6 6 6 1 1 1 1 1 c .
                . . c 6 6 6 6 6 1 1 1 1 1 6 c .
                . . c c 6 6 7 1 1 1 1 1 6 c . .
                . . . c c c c c c c c c c . . .
                """)],
        200,
        True)
for index2 in range(10):
    baddy = sprites.create(img("""
            . . . . c c c c c c . . . . . .
            . . . c 6 7 7 7 7 6 c . . . . .
            . . c 7 7 7 7 7 7 7 7 c . . . .
            . c 6 7 7 7 7 7 7 7 7 6 c . . .
            . c 7 c 6 6 6 6 c 7 7 7 c . . .
            . f 7 6 f 6 6 f 6 7 7 7 f . . .
            . f 7 7 7 7 7 7 7 7 7 7 f . . .
            . . f 7 7 7 7 6 c 7 7 6 f c . .
            . . . f c c c c 7 7 6 f 7 7 c .
            . . c 7 2 7 7 7 6 c f 7 7 7 7 c
            . c 7 7 2 7 7 c f c 6 7 7 6 c c
            c 1 1 1 1 7 6 f c c 6 6 6 c . .
            f 1 1 1 1 1 6 6 c 6 6 6 6 f . .
            f 6 1 1 1 1 1 6 6 6 6 6 c f . .
            . f 6 1 1 1 1 1 1 6 6 6 f . . .
            . . c c c c c c c c c f . . . .
            """),
        SpriteKind.enemy)
    baddy.set_position(randint(0, 160), randint(60, 850))
    baddy.follow(mySprite, 5)
    animation.run_image_animation(baddy,
        [img("""
                . . . . c c c c c c . . . . . .
                . . . c 6 7 7 7 7 6 c . . . . .
                . . c 7 7 7 7 7 7 7 7 c . . . .
                . c 6 7 7 7 7 7 7 7 7 6 c . . .
                . c 7 c 6 6 6 6 c 7 7 7 c . . .
                . f 7 6 f 6 6 f 6 7 7 7 f . . .
                . f 7 7 7 7 7 7 7 7 7 7 f . . .
                . . f 7 7 7 7 6 c 7 7 6 f c . .
                . . . f c c c c 7 7 6 f 7 7 c .
                . . c 7 2 7 7 7 6 c f 7 7 7 7 c
                . c 7 7 2 7 7 c f c 6 7 7 6 c c
                c 1 1 1 1 7 6 f c c 6 6 6 c . .
                f 1 1 1 1 1 6 6 c 6 6 6 6 f . .
                f 6 1 1 1 1 1 6 6 6 6 6 c f . .
                . f 6 1 1 1 1 1 1 6 6 6 f . . .
                . . c c c c c c c c c f . . . .
                """),
            img("""
                . . . c c c c c c . . . . . . .
                . . c 6 7 7 7 7 6 c . . . . . .
                . c 7 7 7 7 7 7 7 7 c . . . . .
                c 6 7 7 7 7 7 7 7 7 6 c . . . .
                c 7 c 6 6 6 6 c 7 7 7 c . . . .
                f 7 6 f 6 6 f 6 7 7 7 f . . . .
                f 7 7 7 7 7 7 7 7 7 7 f . . . .
                . f 7 7 7 7 6 c 7 7 6 f . . . .
                . . f c c c c 7 7 6 f c c c . .
                . . c 6 2 7 7 7 f c c 7 7 7 c .
                . c 6 7 7 2 7 7 c f 6 7 7 7 7 c
                . c 1 1 1 1 7 6 6 c 6 6 6 c c c
                . c 1 1 1 1 1 6 6 6 6 6 6 c . .
                . c 6 1 1 1 1 1 6 6 6 6 6 c . .
                . . c 6 1 1 1 1 1 7 6 6 c c . .
                . . . c c c c c c c c c c . . .
                """)],
        200,
        True)

def on_on_update():
    scene.center_camera_at(mySprite.x, mySprite.y - 32)
    if mySprite.y < 60:
        game.game_over(True)
game.on_update(on_on_update)
