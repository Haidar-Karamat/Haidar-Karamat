#Number guessing game
#logic
#from random import randint #Throw randint importing random number
#
#
#
#computer_guess = randint(1, 100)
#wins = 0
#losses = 0
#while True:
#    guess_number = int(input("Enter your guess number-"))
#    if guess_number == computer_guess:
#        wins += 1
#        print("Congratulation you won!")
#        break
#    elif guess_number > computer_guess:
#        losses += 1
#        print("To high,please guess again!")
#    elif guess_number < computer_guess:
#        losses += 1
#        print("To low,please guess again! ")
#
#print("Total attempts occurs-", wins+losses)


import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game")

font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 28)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

computer_guess = random.randint(1, 100)
input_box = pygame.Rect(200, 150, 140, 32)
user_text = ""
message = "Guess a number between 1 and 100:"
wins = 0
losses = 0
clock = pygame.time.Clock()

def draw():
    screen.fill(WHITE)
    prompt_surface = font.render(message, True, BLACK)
    screen.blit(prompt_surface, (50, 50))

    input_surface = font.render(user_text, True, BLACK)
    screen.blit(input_surface, (input_box.x + 5, input_box.y + 5))

    pygame.draw.rect(screen, BLACK, input_box, 2)

    attempts_text = small_font.render(f"Attempts: {wins + losses}", True, BLACK)
    screen.blit(attempts_text, (50, 300))
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if user_text.isdigit():
                    guess_number = int(user_text)
                    if guess_number == computer_guess:
                        wins += 1
                        message = "🎉 Correct! You win!"
                    elif guess_number > computer_guess:
                        losses += 1
                        message = "Too high! Try again."
                    elif guess_number < computer_guess:
                        losses += 1
                        message = "Too low! Try again."
                else:
                    message = "Invalid input. Enter a number!"
                user_text = ""  # Reset text after enter

            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    draw()
    clock.tick(30)

pygame.quit()
sys.exit()