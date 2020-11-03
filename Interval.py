import pygame
from natsort import natsorted
import os
import NoteInfo as h
import Button as b
import NoteInfo
import EarApp


def resetButton(Buttons, texts):
    for i in Buttons:
        i.color = (0, 162, 199)

    texts[1] = None


def checkAnswer(diff, input):
    print("diff", diff)
    print("input", input)
    return diff == int(input)


def drawScreen(display, buttons, text):
    white = (255, 255, 255)
    font = pygame.font.SysFont("genevattf", 100)
    display.fill(white)

    display.blit(text[0], (80, 30))

    if text[1] != None:
        display.blit(text[1], (80, 200))

    for i in buttons:
        i.draw(display)


def getText():
    font = pygame.font.SysFont("genevattf", 50)
    text = [
        font.render("Interval Identifier", 1, (0, 0, 0)),
        None
    ]

    return text


def getButtons(width, height, diff):

    if diff <= 6:
        gridx = (width / (diff + 1)) - 5
        gridx2 = gridx

    else:
        gridx = (width / (6 + 1)) - 5
        gridx2 = (width / (diff - 5)) - 5

    buttons = [
        b.button((0, 162, 199), 210, 100, 90, 40, "Play Notes"),
        b.button((0, 162, 199), 210, 30, 90, 40, "Next"),
        b.button((0, 162, 199), 50, 100, 90, 40, "Main Menu"),
        b.button((0, 162, 199), gridx*1, 200, 30, 30, "0"),
        b.button((0, 162, 199), gridx*2, 200, 30, 30, "1"),
        b.button((0, 162, 199), gridx*3, 200, 30, 30, "2"),
        b.button((0, 162, 199), gridx*4, 200, 30, 30, "3"),
        b.button((0, 162, 199), gridx*5, 200, 30, 30, "4"),
        b.button((0, 162, 199), gridx*6, 200, 30, 30, "5"),
        b.button((0, 162, 199), gridx2*1, 300, 30, 30, "6"),
        b.button((0, 162, 199), gridx2*2, 300, 30, 30, "7"),
        b.button((0, 162, 199), gridx2*3, 300, 30, 30, "8"),
        b.button((0, 162, 199), gridx2*4, 300, 30, 30, "9"),
        b.button((0, 162, 199), gridx2*5, 300, 30, 30, "10"),
        b.button((0, 162, 199), gridx2*6, 300, 30, 30, "11"),

    ]
    # going to have to add number of static buttons
    buttons = buttons[:diff+3]

    return buttons


def run(noteList, display):

    font = pygame.font.SysFont("genevattf", 50)
    noteIndex = NoteInfo.getNote(2, noteList)
    noteIndex.sort()
    interval = noteIndex[1] - noteIndex[0]

    buttons = getButtons(500, 500, 12)
    texts = getText()

    input = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                exit()
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if buttons[0].isOver(pos):
                    NoteInfo.playNotes(noteIndex, noteList)

                if buttons[1].isOver(pos):
                    noteIndex = NoteInfo.getNote(2, noteList)
                    noteIndex.sort()
                    interval = noteIndex[1] - noteIndex[0]
                    resetButton(buttons, texts)

                if buttons[2].isOver(pos):
                    EarApp.main()
                # answer buttons
                for i in range(3, len(buttons)):
                    if buttons[i].isOver(pos):
                        input = buttons[i].text
                        if checkAnswer(interval, input):
                            buttons[i].color = (0, 255, 0)
                            texts[1] = font.render(
                                "Correct", 1, (0, 255, 0))

                            # output correct
                        else:
                            buttons[i].color = (255, 0, 0)
                            texts[1] = font.render(
                                "Incorrect", 1, (255, 0, 0))

                            # output incorrect

        drawScreen(display, buttons, texts)

        pygame.display.update()
