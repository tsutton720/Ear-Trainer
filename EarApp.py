import pygame
from natsort import natsorted
import Button as b
import Interval
import Melody
import os


pygame.init()
display = pygame.display.set_mode(
    (500, 500))


def main():

    files = natsorted(populateFiles())

    font = pygame.font.SysFont("genevattf", 100)
    # display = pygame.display.set_mode(
    #     (500, 500))
    text = font.render("Ear Trainer", 1, (0, 0, 0))
    II = b.button((0, 162, 199), 200, 200, 150, 40, "Interval Identifier")
    MM = b.button((0, 162, 199), 200, 300, 150, 40, "Melody Matcher")

    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                exit()
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if II.isOver(pos):

                    Interval.run(files, display)

                if MM.isOver(pos):
                    Melody.run(files, display)

        display.fill((255, 255, 255))
        text = font.render("Ear Trainer", 1, (0, 0, 0))
        display.blit(text, (80, 30))
        II.draw(display)
        MM.draw(display)
        pygame.display.update()


def populateFiles():
    fileList = []
    cwd = os.getcwd()

    for fileName in os.listdir(cwd + "/notes"):
        fileList.append("notes/" + fileName)

    return fileList


if __name__ == '__main__':
    main()
