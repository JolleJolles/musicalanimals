import pandas as pd
import numpy as np
from midiutil import MIDIFile

class Manimals:

    def __init__(self, time = 0, duration = 1, tempo = 60, volume = 100):

        self.time = def create_midi(file, datacols = [], musicvars = []):

    # 1) Checks
    # Check dat length datacols == length musicvars
    # etc

    # 2) Load data file
    datafile = pd.read_csv(file)

    # 3) Set up midifile
    track = 0
    channel = 0
    time = 0 # In beats
    duration = 1 # In beats
    tempo = 60 # In BPM
    volume = 100 # 0-127, as per the MIDI standard

    for i, col in enumerate(datacols):
        datacol <- datafile.loc[,col]

        musicconversion(data = datacol, transformation = musicvar[i])



def musicconversion(data, transformation):






create_midi(file = "~/Desktop/jolles-stickles-pairs.csv",
            datacols = ["x","y"],
            musicvars = ["amplitude","frequency"])
