import os
import pygame

def main():

    try:
        pygame.mixer.init()

    except pygame.error as e:
        print("Audio initialization failed!", e)
        return

if __name__ == "__main__":
    main()