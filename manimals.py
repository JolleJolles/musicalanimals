import os
import pandas as pd
import numpy as np
from midiutil import MIDIFile
from sklearn.preprocessing import minmax_scale

class Manimals:

    def __init__(self, file, suffix = "_midi", datacols = [], musicvars = [],
                 channel = 0, time = 0, timestep = 1, duration = 1, tempo = 1500, volume = 100):

        """
        Documentation here
        time : int, default = 0
            The time in beats
        volume : in, default = 100
            Volume level, between 0 and 127, per MIDI standardß
        etc...
        """

        self.file = file
        self.suffix = suffix
        self.time = time
        self.timestep = timestep
        self.musicvars = musicvars
        self.duration = duration
        self.channel = channel
        self.tempo = tempo
        self.volume = volume

        # Load datafile
        try:
            self.datafile = pd.read_csv(self.file)
        except:
            print("issue reading datafile")
            return
        self.datacols = datacols
        self.musicvars = musicvars

        # Set up midifile
        self.track = 0
        self.MyMIDI = MIDIFile(1)
        self.MyMIDI.addTempo(self.track, self.time, self.tempo)

        # Generate music
        self.generate_music()


    def generate_music(self):

        for i, col in enumerate(self.datacols):
            datacol = self.datafile[col]
            datacol = minmax_scale(datacol) * 127
            # for time being just start with first 20 datapoints
            datacol = datacol[0:300]

            if self.musicvars[i] == "pitch":
                for pitch in datacol:
                    if pitch == pitch:
                        channel = 1 if pitch % 2 == 0 else 3
                        note = int(pitch)
                        print(str(self.time)+" "+str(note), end=" ")
                        self.MyMIDI.addNote(self.track,
                                            channel,
                                            note,
                                            self.time,
                                            self.duration,
                                            self.volume)
                        if pitch % 2:
                            self.time = self.time + self.timestep

        self.save_midi()


    def save_midi(self):

        midifile = os.path.splitext(self.file)[0]+self.suffix+".mid"
        with open(midifile, "wb") as output_file:
            self.MyMIDI.writeFile(output_file)
        print("Midi file written..")
