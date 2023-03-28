from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super(). __init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


width = 600
height = 500
window = display.set_mode((width, height))
display.set_caption('Пинг-Понг')

background = GameSprite('back.jpg', 0, 0, 0, width, height)

game = True
finish = False
clock = time.Clock()
FPS = 120

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        background.reset()


    display.update()
    clock.tick(FPS)


