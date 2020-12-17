import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
import pandas as pd 
import json
from plot_utils.plt import *
from plot_utils.sns import *

def lineplot(cfg):
    if  cfg['new_figure']:
        fig = plt.figure(figsize=cfg['figsize'])
        cfg['fig'] = fig
    sns.lineplot(x=cfg['x'], y=cfg['y'], data=cfg['data'])

    custom_plt_plot(cfg['fig'], **cfg['plt_info'])
    custom_sns_plot(**cfg['sns_info'])

if __name__=="__main__":
    with open("config.json")  as jsonfile:
        cfg = json.load(jsonfile)



    