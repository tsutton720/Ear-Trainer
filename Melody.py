import pygame
import NoteInfo as n
import Button as b
import EarApp


def run(notefiles, display):

    font = pygame.font.SysFont("genevattf", 100)
    diff = 3
    melody = n.getNote(diff, notefiles)

    mainM = b.button((0, 162, 199), 50, 100, 90, 40, "Main Menu")
    playMel = b.button((0, 162, 199), 50, 300, 90, 40, "Play Mel")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                running = False
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if playMel.isOver(pos):
                    n.playNotes(melody, notefiles)

                if(mainM.isOver(pos)):
                    EarApp.main()

        display.fill((255, 255, 255))
        text = font.render("Melody Matcher", 1, (0, 0, 0))
        display.blit(text, (80, 30))
        mainM.draw(display)
        playMel.draw(display)
        pygame.display.update()
