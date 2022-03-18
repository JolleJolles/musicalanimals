import pandas as pd
import numpy as np

def create_midi(file, datacols = [], musicvars = []):

    # 1) Checks
    # Check dat length datacols == length musicvars
    # etc

    # 2) Load data file 
    datafile = pd.read_csv(file)
    for i, col in enumerate(datacols):
        datacol <- datafile.loc[,col]

        musicconversion(data = datacol, transformation = musicvar[i])



def musicconversion()


create_midi(file = "~/Desktop/jolles-stickles-pairs.csv",
            datacols = ["x","y"],
            musicvars = ["amplitude","frequency"])
