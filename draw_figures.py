import matplotlib.pyplot as plt
import seaborn as sns
import os
import random
import numpy as np
import matplotlib.pyplot as plt


class figure:
    def __init__(self):
        if 'figures' not in os.listdir(os.getcwd()+'/static'):
            os.mkdir(os.getcwd()+'/static'+'/figures')
    def lineplot(self,x,y,legend,title,hue=None,color=None):
        plt.figure(figsize=(12,6))
        sns.lineplot(x,y, hue=hue,marker = "o", linestyle= "--", linewidth = 2,markersize = 10,color=color)
        if not 'None' in legend:
            plt.legend(legend,loc='upper left',fontsize='x-large')
        plt.title(title+'\n'+'(Vicky AI Production.)',loc='center',fontdict={'fontsize':16})
        plt.savefig(os.getcwd()+'/static'+f'/figures/{title}.png')
    def pie_plot(self,lst,title,df1):
       
        plt.figure(figsize=(16,9))
        explode = [0.0,0.0,0.0,0.0,0.0,0.2,0.0] # To slice the perticuler section
        colors = ["c", 'magenta','g','pink','y','r','b'] # Color of each section
        
        textprops = {"fontsize":22} # Font size of text in pie chart

        plt.pie(lst, # Values
                labels = ['Sindh', 'G.B', 'Punjab', 'Balochistan','K.P.K', 'Islamabad',  'A.J.K'],# Labels for each sections
                labeldistance = 1.1,
                explode = explode, # To slice the perticuler section
                colors =colors, # Color of each section
                autopct = "%0.2f%%", # Show data in persentage for with 2 decimal point
                shadow = True, # Showing shadow of pie chart
                radius = 1, # Radius to increase or decrease the size of pie chart 
            startangle = 270, # Start angle of first section
                # rotatelabels=True,
                pctdistance=0.6,
                
        #         frame=True,

                textprops =textprops)
        # plt.tight_layout() 
        plt.title(title+'\n'+'(Vicky AI Production.)',loc='center',fontdict={'fontsize':22})
        plt.savefig(os.getcwd()+'/static'+f'/figures/{title}.png')
    def ratio_between_deaths_and_recoveries(self,deaths,recoveries):
        plt.figure(figsize=(16,9))
        explode = [0.0,0.1] # To slice the perticuler section
        colors = ["magenta",'r'] # Color of each section
        
        textprops = {"fontsize":22} # Font size of text in pie chart

        plt.pie([recoveries,deaths], # Values
                labels = ['Total Recoveries','Total Deaths'],# Labels for each sections
                labeldistance = 0.8,
                explode = explode, # To slice the perticuler section
                colors =colors, # Color of each section
                autopct = "%0.2f%%", # Show data in persentage for with 2 decimal point
                shadow = True, # Showing shadow of pie chart
                radius = 1, # Radius to increase or decrease the size of pie chart 
            startangle = 270, # Start angle of first section
                # rotatelabels=True,
                pctdistance=0.6,
                
        #         frame=True,

                textprops =textprops)
        # plt.tight_layout() 
        plt.title('Deaths Vs Recoveries in 2021'+'\n'+'(Vicky AI Production.)',loc='center',fontdict={'fontsize':22})
        plt.savefig(os.getcwd()+'/static'+'/figures/ratio_between_deaths_and_recoveries.png')

