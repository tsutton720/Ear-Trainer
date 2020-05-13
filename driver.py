import os
from natsort import natsorted
from random import randint
from playsound import playsound

userIn = -1
answer = -1
buttonPressed = False
highscore = 0
currScore = 0


def populateFile(fileList):
    cwd = os.getcwd()

    for fileName in os.listdir(cwd + "/notes"):
        fileList.append("notes/" + fileName)


def getNotes(noteList):
    length = len(noteList)
    note1 = randint(0, length - 1)
    note2 = randint(note1, length - 1)

    playsound(noteList[note1])
    playsound(noteList[note2])

    print(note1)
    print(note2)
    return [note1, note2]


def setIn(input):
    userIn = input
    buttonPressed = True


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

    return switch.get(diff)


def calcInterval(noteList):
    return (noteList[1] - noteList[0]) % 12


def main():
    global fileList
    global twoNotes
    global answer
    global userIn
    f = open("HighScores.txt", "r+")
    if os.stat("HighScores.txt").st_size == 0:
        highscore = 0
    else:
        high = f.read()
        highscore = int(high)
    f.close()
    print(highscore)
    currScore = 0
    fileList = []
    populateFile(fileList)
    fileList = natsorted(fileList)
    twoNotes = getNotes(fileList)
    answer = calcInterval(twoNotes)
    userIn = -1

    print("0: Octave\n1: Minor Second\n2: Major Second\n3: Minor Third\n4: Major Third\n5: Perfect Fourth\n6: "
          "Tritone\n7: Perfect Fifth\n8: Minor Sixth\n9: Major Sixth\n10: Minor Seventh\n11: Major Seventh\n\n\n")

    print("This is answer: ", answer)
    # userIn = input("Enter your answer: ")


currScore = 0
f = open("HighScores.txt", "r+")
highscore = 0
if os.stat("HighScores.txt").st_size == 0:
    highscore = 0
else:
    high = f.read()
    highscore = int(high)
f.close()


def main2(input):
    global fileList
    global twoNotes
    global answer
    global userIn
    global highscore
    global currScore

    print(highscore)
    print(currScore)

    # twoNotes = getNotes(fileList)
    # answer = calcInterval(twoNotes)
    # userIn = -1
    f = open("HighScores.txt", "r+")
    if os.stat("HighScores.txt").st_size == 0:
        highscore = 0
    else:
        high = f.read()
        highscore = int(high)
    f.close()

    userIn = input
    print("This is user in: ", userIn)

    while True:
        print("This is the current input: " + str(userIn))
        print("This is the current answer: " + str(answer))
        if userIn == 'r':
            playsound(fileList[twoNotes[0]])
            playsound(fileList[twoNotes[1]])
            # print("yeet")
            # userIn = input("Enter your answer: ")
            print("Enter your answer: ")
        elif userIn == 'q':
            if currScore > highscore:
                highscore = currScore
            break
        elif int(userIn) == answer:
            print("Correct")
            twoNotes = getNotes(fileList)
            answer = calcInterval(twoNotes)
            # userIn = input("Enter your answer: ")
            print("Enter your answer: ")
            currScore += 1
            if currScore > highscore:
                highscore = currScore
            break
        else:
            # userIn = input("Nice try, retard. Better luck next time: ")
            print("Nice try. Better luck next time: ")
            if currScore > highscore:
                highscore = currScore
                f = open("HighScores.txt", "w")
                f.write(str(currScore))
                f.close()
            highscore = currScore
            currScore = 0
            break


def replaySound():
    global twoNotes
    global fileList

    playsound(fileList[twoNotes[0]])
    playsound(fileList[twoNotes[1]])
    print("inside")


def updateScore(highscore):
    f = open("HighScores.txt", "w")
    f.write(str(highscore))
    f.close()


if __name__ == '__main__':
    main()
