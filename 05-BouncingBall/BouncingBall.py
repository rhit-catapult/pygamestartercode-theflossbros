import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(100, 500)
        self.y = random.randint(100,500)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.radius = random.randint(10,40)
        self.speed_x = random.randint(-7,7)
        self.speed_y = random.randint(-7,7)


    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        if self.x + self.radius > self.screen.get_width():
            self.speed_x = -self.speed_x
        if self.y + self.radius > self.screen.get_height():
            self.speed_y = -self.speed_y
        if self.x - self.radius < 0:
            self.speed_x = -self.speed_x
        if self.y - self.radius < 0:
            self.speed_y = -self.speed_y




# DONE: Create a Ball class.
# DONE: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# DONE: Methods: __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class called ball1
    ball1 = Ball(screen)
    balls = []
    balls.append(ball1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    balls.append(Ball(screen))
                if event.key == pygame.K_BACKSPACE:
                    if len(balls) > 0:
                        balls.pop(0)





        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # DONE: Move the ball
        for ball in balls:
            ball.move()


        # DONE: Draw the ball
        for ball in balls:
            ball.draw()

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
