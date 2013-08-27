import sys
import pygame
from ball import Ball
from box import Box

def main():
    # Initialisation
    pygame.init()
    fps_clock = pygame.time.Clock()

    width, height = size = 700, 700
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)

    ball = Ball()

    boxes = []
    rows = 5
    row = 0
    columns = 17
    column = 0
    while row < rows:
        row = row + 1
        while column < columns:
            column = column + 1
            boxes.append(Box(column,row))
        column = 0

    # Game Loop Start
    while 1:

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Logic
        ball.move()
        broken_box = ball.check_collision(size, boxes)
        if broken_box is not None:
            i = 0
            new_boxes = []
            for each in boxes:
                if broken_box != i:
                    new_boxes.append(each)
                i = i + 1
            boxes = new_boxes

        #Render
        for each in boxes:
            screen.blit(each.image, each.rect)
        screen.blit(ball.image, ball.rect)

        pygame.display.flip()
        screen.fill(black)
        fps_clock.tick(60)


if __name__ == '__main__':
    main()
