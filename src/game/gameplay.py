import pygame
from time import sleep

from rl_env import Environment


# Make an environment object
env = Environment()
# Change wall speed to 3 (one step every 3 frames)
env.WALL_SPEED = 3

# Initialize some variables
WINDOW = pygame.display.set_mode((env.WINDOW_WIDTH, env.WINDOW_HEIGHT))
clock = pygame.time.Clock()
win = False
winning_score = 100

# Repeaat the game untill the player win
# (got a score of winning_score) or quits the game.
while not win:
    score_increased = False
    game_over = False
    _ = env.reset()
    pygame.display.set_caption("Game")
    while not game_over:
        clock.tick(27)
        env.render(WINDOW=WINDOW, human=True)
        game_over = env.game_over
    #####################################################
    sleep(0.5)
    WINDOW.fill(env.WHITE)
    if env.score >= winning_score:
        win = True
        env.print_text(WINDOW=WINDOW,
                       text_cords=(env.WINDOW_WIDTH // 2,
                                   env.WINDOW_HEIGHT // 2),
                       text=f"You Win - Score : {env.score}",
                       color=env.RED, center=True)
    else:
        env.print_text(WINDOW=WINDOW, text_cords=(env.WINDOW_WIDTH // 2,
                                                  env.WINDOW_HEIGHT // 2),
                       text=f"Game Over - Score : {env.score}",
                       color=env.RED, center=True)
    pygame.display.update()
