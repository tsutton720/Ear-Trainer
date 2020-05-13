from mingus.midi import fluidsynth
import time

sound_path = "GrandPiano.sf2"

fluidsynth.init(sound_path)
time.sleep(15)
fluidsynth.play_Note(80, 0, 80)
