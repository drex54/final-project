mySprite3: Sprite = None
scene.set_background_color(11)
mySprite = sprites.create(img("""
        . . 4 4 4 . . . . 4 4 4 . . . . 
            . 4 5 5 5 e . . e 5 5 5 4 . . . 
            4 5 5 5 5 5 e e 5 5 5 5 5 4 . . 
            4 5 5 4 4 5 5 5 5 4 4 5 5 4 . . 
            e 5 4 4 5 5 5 5 5 5 4 4 5 e . . 
            . e e 5 5 5 5 5 5 5 5 e e . . . 
            . . e 5 f 5 5 5 5 f 5 e . . . . 
            . . f 5 5 5 4 4 5 5 5 f . . f f 
            . . f 4 5 5 f f 5 5 6 f . f 5 f 
            . . . f 6 6 6 6 6 6 4 4 f 5 5 f 
            . . . f 4 5 5 5 5 5 5 4 4 5 f . 
            . . . f 5 5 5 5 5 4 5 5 f f . . 
            . . . f 5 f f f 5 f f 5 f . . . 
            . . . f f . . f f . . f f . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
mySprite2 = sprites.create(img("""
        ..........bbbbbb................
            .......bbb444444bb..............
            .....2244444ddd444b.............
            ....244444444dddd44e............
            ...244444444444ddd4be...........
            ..244444444444444d44be..........
            .2b444444444444444d4be..........
            .2b44444444444444444bbe.........
            2bbb4444444444444444bbe.........
            2bbb4444444444444444bbe.........
            2bb4b4444444444444444bbe........
            2bb4444444444444444444be........
            2bb44444444444444444444e........
            2bbb444bbb4444444444444e........
            22bbb444bb4bb444444444be........
            .2bbbbb44bbbb44444444bbe........
            .22bbbbbbbb44bbb444444bbe.......
            ..eeebbbbbbb44bbb444444be.......
            ...eeeeebbbbbbbb44b4444be.......
            .....eeeeee222bb44bbb4bbe.......
            .......eeeee222bb44bbbbee.......
            ............e222bbbbbbbec.......
            ..............ee2bbbbeebdb......
            .................eeeeecdddb.....
            .......................cd11bbbb.
            ........................cd111dbb
            .........................b11111c
            .........................c11dd1c
            .........................cd1dbc.
            .........................cb11c..
            ..........................ccc...
            ................................
    """),
    SpriteKind.food)
if True:
    mySprite3 = sprites.create(img("""
            . . . . . . . . . . b 5 b . . . 
                    . . . . . . . . . b 5 b . . . . 
                    . . . . . . b b b b b b . . . . 
                    . . . . . b b 5 5 5 5 5 b . . . 
                    . . . . b b 5 d 1 f 5 5 d f . . 
                    . . . . b 5 5 1 f f 5 d 4 c . . 
                    . . . . b 5 5 d f b d d 4 4 . . 
                    . b b b d 5 5 5 5 5 4 4 4 4 4 b 
                    b d d d b b d 5 5 4 4 4 4 4 b . 
                    b b d 5 5 5 b 5 5 5 5 5 5 b . . 
                    c d c 5 5 5 5 d 5 5 8 5 5 5 b . 
                    c b d c d 5 5 b 5 5 8 5 5 5 b . 
                    . c d d c c b d 5 5 5 5 5 d b . 
                    . . c b d d d d d 5 5 5 b b . . 
                    . . . c c c c c c c c b b . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    mySprite3.set_position(57, 63)
    controller.move_sprite(mySprite3, 70, 50)
else:
    mySprite3.follow(mySprite)

def on_forever():
    if mySprite.overlaps_with(mySprite2):
        info.change_score_by(1)
        info.start_countdown(1.4)
        mySprite2.set_position(randint(10, 160), randint(10, 120))
forever(on_forever)

def on_forever2():
    if mySprite.overlaps_with(mySprite3):
        mySprite.destroy()
        game.over(False, effects.dissolve)
forever(on_forever2)
