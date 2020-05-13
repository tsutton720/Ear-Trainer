from tkinter import Label, Button, Tk
import driver


class BottomTextEarTrainingScreen:
    def __init__(self, master):
        self.master = master

        master.title("Bottom Text Ear Trainer GUI")

        self.label = Label(master, font=('Helvetica', 30),
                           text="Bottom Text Ear Trainer").place(x=275, y=0)

        self.interval_buttonList = []

        self.interval_buttonList.append(Button(master, text="Octave", font=(
            'Helvetica', 15), command=lambda: driver.main2(0)).place(x=275, y=400))
        self.interval_buttonList.append(Button(master, text="Minor 2", font=(
            'Helvetica', 15), command=lambda: driver.main2(1)).place(x=275, y=500))
        self.interval_buttonList.append(Button(master, text="Major 2", font=(
            'Helvetica', 15), command=lambda: driver.main2(2)).place(x=275, y=600))
        self.interval_buttonList.append(Button(master, text="Minor 3", font=(
            'Helvetica', 15), command=lambda: driver.main2(3)).place(x=525, y=400))
        self.interval_buttonList.append(Button(master, text="Major 3", font=(
            'Helvetica', 15), command=lambda: driver.main2(4)).place(x=525, y=500))
        self.interval_buttonList.append(Button(master, text="Perfect 4", font=(
            'Helvetica', 15), command=lambda: driver.main2(5)).place(x=525, y=600))
        self.interval_buttonList.append(Button(master, text="Tritone", font=(
            'Helvetica', 15), command=lambda: driver.main2(6)).place(x=825, y=400))
        self.interval_buttonList.append(Button(master, text="Perfect 5", font=(
            'Helvetica', 15), command=lambda: driver.main2(7)).place(x=825, y=500))
        self.interval_buttonList.append(Button(master, text="Minor 6", font=(
            'Helvetica', 15), command=lambda: driver.main2(8)).place(x=825, y=600))
        self.interval_buttonList.append(Button(master, text="Major 6", font=(
            'Helvetica', 15), command=lambda: driver.main2(9)).place(x=1125, y=400))
        self.interval_buttonList.append(Button(master, text="Minor 7", font=(
            'Helvetica', 15), command=lambda: driver.main2(10)).place(x=1125, y=500))
        self.interval_buttonList.append(Button(master, text="Major 7", font=(
            'Helvetica', 15), command=lambda: driver.main2(11)).place(x=1125, y=600))

        self.replay_Button = Button(master, text="Replay Note", font=(
            'Helvetica', 15), command=driver.replaySound).place(x=825, y=800)

        self.tooLowLabel = Label(master, font=(
            'Helvetica', 20), text="Too Low", fg="red").place(x=350, y=150)
        self.tooHighLabel = Label(master, font=(
            'Helvetica', 20), text="Too High", fg="red").place(x=1000, y=150)
        self.correctLabel = Label(master, font=(
            'Helvetica', 20), text="Correct", fg="green").place(x=695, y=150)

        self.greet_button = Button(text="Begin", font=(
            'Helvetica', 15), command=driver.main)
        self.greet_button.place(x=525, y=800)

        # self.greet_button.config(bg="red")

        self.close_button = Button(text="Close", command=master.quit)
        # self.close_button.place()

    def greet(self):
        print("Greetings!")


root = Tk()

root.geometry("1600x900")
root.resizable(0, 0)
my_gui = BottomTextEarTrainingScreen(root)

root.mainloop()
