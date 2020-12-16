import numpy as np
import pandas as pd 

class Annealing():

    def make(self):
        T = 14700*2
        M = 2 
        R = 0.5
        t = np.arange(0,T)
        tau = np.clip(t%np.ceil(T/M)/(T/M),0,1)
        beta = [t/R if t<=R else 1 for t in tau]
        beta = np.array(beta)
        df = pd.DataFrame(beta, columns=["beta"])
        df.to_csv("data/annealing.csv", index=False)   
        print("*--Check data folder--*")


if __name__=="__main__":
    an = Annealing()
    an.make()

