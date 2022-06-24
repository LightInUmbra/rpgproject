import os
import pygame
import player
import main_menu
import keyboard
import game_menu
import pickle

pygame.init()

# SIZE = WIDTH, HEIGHT = 720, 480
BACKGROUND_COLOR = pygame.Color('black')
FPS = 60

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()


def load_images(path):
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(path + os.sep + file_name).convert()
        images.append(image)
    return images

class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, position, images, images_updown, images_downup):
        super(AnimatedSprite, self).__init__()

        size = (48, 48)

        self.rect = pygame.Rect(position, size)
        self.images = images
        self.images_updown = images_updown
        self.images_downup = images_downup
        self.images_right = images
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]
        self.images_up = images_downup
        self.images_down = images_updown
        self.index = 0
        self.image = images[self.index]

        self.velocity = pygame.math.Vector2(0, 0)

        self.animation_time = 0.1
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

    def update_time_dependent(self, dt):
        if self.velocity.x > 0:
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left
        elif self.velocity.y > 0:
            self.images = self.images_down
        elif self.velocity.y < 0:
            self.images = self.images_up

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def update_frame_dependent(self):
        if self.velocity.x > 0:
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left
        elif self.velocity.y > 0:
            self.images = self.images_down
        elif self.velocity.y < 0:
            self.images = self.images_up

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def update(self, dt):
        self.update_time_dependent(dt)
        # self.update_frame_dependent()

def main():
    main_menu.MainMenu()

def start_game():
    images = load_images(path='assets/players/test/right')
    images_updown = load_images(path='assets/players/test/down')
    images_downup = load_images(path='assets/players/test/up')
    player = AnimatedSprite(
        position=(100, 100),
        images=images,
        images_updown=images_updown,
        images_downup=images_downup
    )
    all_sprites = pygame.sprite.Group(player)

    running = True
    while running:

        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.velocity.x = 4
                elif event.key == pygame.K_a:
                    player.velocity.x = -4
                elif event.key == pygame.K_s:
                    player.velocity.y = 4
                elif event.key == pygame.K_w:
                    player.velocity.y = -4
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    player.velocity.x = 0
                elif event.key == pygame.K_s or event.key == pygame.K_w:
                    player.velocity.y = 0
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    game_menu.GameMenu()

        all_sprites.update(dt)
        screen.fill(BACKGROUND_COLOR)
        all_sprites.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
