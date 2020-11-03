import os
import random
import pygame


def getNote(num, noteList):
    notes = []

    for i in range(num):
        x = random.randint(0, len(noteList)-1)
        notes.append(x)

    return notes


def playNotes(noteIndexs, fullList):
    pygame.mixer.init()
    for i in noteIndexs:
        sound = pygame.mixer.Sound(fullList[i])
        sound.play()
        pygame.time.delay(700)


def nameNote(noteNum):
    switch = {
        0: "A",
        1: "A#",
        2: "B",
        3: "C",
        4: "C#",
        5: "D",
        6: "D#",
        7: "E",
        8: "F",
        9: "F#",
        10: "G",
        11: "G#"
    }
    return switch.get(noteNum % 12)


def nameInterval(diff):
    switch = {
        0: "Octave",
        1: "Minor Second",
        2: "Major Second",
        3: "Minor Third",
        4: "Major Third",
        5: "Perfect Fourth",
        6: "Tritone",
        7: "Perfect Fifth",
        8: "Minor Sixth",
        9: "Major Sixth",
        10: "Minor Seventh",
        11: "Major Seventh"
    }
