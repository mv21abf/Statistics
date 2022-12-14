# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 23:27:54 2022

@author: manuv
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns

def read_data(fn):
    """ 
    This function read data 
    """
    df = pd.read_csv(fn)
    return df;

    
def bargraph():
    """
    This function plots cereal yield of different countries
    in the year 2010,2012 and 2014
    """
    cereal_df = read_data("C:\\ads 2\\CY.csv")
    cereal_df_Transpose = cereal_df.transpose()
    plt.figure(figsize=(10, 4))
    val = cereal_df[['Country Name', '2010', '2012', '2014']]
    t = val.iloc[0:5]
    y = t['Country Name']
    x = np.arange(len(y))
    plt.bar(x-0.1, t['2010'], width=0.2, label="2010")
    plt.bar(x+0.1, t['2012'], width=0.2, label="2012")
    plt.bar(x+0.3, t['2014'], width=0.2, label="2014")
    plt.xticks(x, y, rotation=90, horizontalalignment='center',fontsize=15)
    plt.yticks(fontsize=15)
    plt.title("CEREAL YIELD",fontsize=15)
    plt.legend(fontsize=15)
    plt.xlabel("Country",fontsize=15)
    plt.ylabel("Cereal Yield",fontsize=15)
    plt.savefig("Cereal.png", bbox_inches="tight")
    plt.show()
    _mean =val.mean()
    _median =val.median()
    _mode = stats.mode(val)
    print("Mean of Cereal yield :\n",_mean)
    print("\n")
    print("Median of Cereal yield:\n",_median)  
    print("Mode of Cereal yield:\n",_mode)

def bargraph1():
    """
    This function plots total population of five different 
    countries in the given year 2010,2012 and 2014
    """
    pop_df = read_data("C:/ads 2/PT.csv")
    plt.figure(figsize=(10, 4))
    val = pop_df[['Country Name', '2010', '2012', '2014']]
    t = val.iloc[0:5]
    y = t['Country Name']
    x = np.arange(len(y))
    plt.bar(x-0.1, t['2010'], width=0.2, label="2010")
    plt.bar(x+0.1, t['2012'], width=0.2, label="2012")
    plt.bar(x+0.3, t['2014'], width=0.2, label="2014")
    plt.xticks(x, y, rotation=90, horizontalalignment='center',fontsize=15)
    plt.yticks(fontsize=15)
    plt.title("POPULATION, TOTAL",fontsize=15)
    plt.legend(fontsize=15)
    plt.xlabel("Country",fontsize=15)
    plt.ylabel("Population",fontsize=15)
    plt.savefig("Population.png", bbox_inches="tight")
    plt.show()
    _mean =val.mean()
    _median =val.median()
    _mode = stats.mode(val)
    print("Mean of Total Population :\n",_mean)
    print("\n")
    print("Median of Total Population:\n",_median)    
    print("Mode of Cereal yield:\n",_mode)



    
    
if __name__=="__main__":    
    
    #calling function to visualise bar plot
    bargraph()  
    
    #calling function to visualise bar plot
    bargraph1()
   