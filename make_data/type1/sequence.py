import numpy as np
import pandas as pd 

class Sequence():

    def make(self):
        FREQ = 200
        taus = []
        R = 0.99
        for update_num in range(500):
            tau = (update_num%FREQ)/FREQ
            beta = (tau/R)**5/4 if tau<=R else 1/4
            taus.append(beta)
        df = pd.DataFrame(taus, columns=["x"])
        df.to_csv("data/sequence.csv", index=False)   
        print("*--Check data folder--*")


if __name__=="__main__":
    an = Sequence()
    an.make()

