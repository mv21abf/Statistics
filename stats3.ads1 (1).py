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
    This function reads csv file data 
    """
    df = pd.read_csv(fn)
    return df

def get_transpose(str):
    """This Function returns transpose of dataframe given
    """
    df=str.transpose()
    return df

def bargraph():
    """
    This function plots cereal yield of different countries
    in the year 2010,2012 and 2014
    """
    cereal_df = read_data("C:\\ads 2\\CY.csv")
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


def lineplot_1(): 
    """
    This function plots CO2 emissions from solid fuel consumption
    of eight different countries in the given year 2010,2012 and 2014
    """
    solid = read_data("co2 s.csv")
    plt.figure()
    year=["2010","2012","2014"]
    for i in range(len(year)):
        plt.plot(solid['Country Name'],solid[year[i]],label = year[i])
    plt.title("CO2 emissions from solid fuel consumption (kt)",fontsize=15)
    plt.xlabel("Country Name",fontsize=15)
    plt.ylabel("CO2 Emissions(solid fuel)",fontsize=15)
    plt.legend(fontsize=15)
    plt.xticks(rotation=90,horizontalalignment='center',fontsize=15)
    plt.yticks(fontsize=15)
    plt.savefig("solid_fuel_consumption.png", bbox_inches = "tight")
    plt.show()

    
   
def lineplot_2(): 
    """
    This function plots CO2 emissions from liquid fuel consumption
    of eight different countries in the given year 2010,2012 and 2014
    """
    
    liquid = read_data("co2 l.csv")
    plt.figure()
    year=["2010","2012","2014"]
    for i in range(len(year)):
        plt.plot(liquid['Country Name'],liquid[year[i]],label = year[i])
    plt.title("CO2 emissions from liquid fuel consumption (kt)",fontsize=15)
    plt.xlabel("Country Name",fontsize=15)
    plt.ylabel("CO2 Emissions(liquid fuel)",fontsize=15)
    plt.legend(fontsize=15)
    plt.xticks(rotation=90,horizontalalignment="center",fontsize=15)
    plt.yticks(fontsize=15)
    plt.savefig("liquid_fuel_consumption.png", bbox_inches = "tight")
    plt.show()


def heatmap():
    """
    This function visualize correlation between different indicators
    """
    df = pd.read_csv("swi.csv")
    df_drop = df.drop("Country Name",axis=1)
    df_set_ind = df_drop.set_index("Indicator")
    df_set_ind.index.name = None
    df_trans = get_transpose(df_set_ind)
    cor=df_trans.corr()
    sns.heatmap(data=cor,annot=True)
    plt.title("Switzerland",fontsize=15)
    plt.xticks(rotation=90,horizontalalignment="center",fontsize=15)
    plt.yticks(fontsize=15)
    plt.savefig("Heatmap.png", bbox_inches = "tight")
    plt.show()
    
    
    
if __name__=="__main__":    
    
    #calling function to visualise bar plot
    bargraph()  
    
    #calling function to visualise bar plot
    bargraph1()
    
    #calling function to visualise line plot
    lineplot_1()
    
    #calling function to visualise line plot
    lineplot_2()
    
    #calling function to visualise heatmap
    heatmap()
   
