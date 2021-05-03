import matplotlib.pyplot as plt
import seaborn as sns
import os
class figure:
    def __init__(self):
        if 'figures' not in os.listdir(os.getcwd()+'/static'):
            os.mkdir(os.getcwd()+'/static'+'figures')
    def lineplot(self,x,y,legend,title,hue=None,color=None):
        plt.figure(figsize=(16,9))
        sns.lineplot(x,y, hue=hue,marker = "o", linestyle= "--", linewidth = 2,markersize = 10,color=color)
        if legend:
            plt.legend([legend],loc='upper left',fontsize='x-large')
        plt.title(title+'\n'+'(Vicky AI Production.)',loc='center',fontdict={'fontsize':16})
        plt.savefig(os.getcwd()+'/static'+f'figures/{title}.png')
    def pie_plot(self,lst,title,df1):
        plt.figure(figsize=(16,9))
        explode = [0.02,0.1,0.07,0.01,0.1,0.3,0.6] # To slice the perticuler section
        colors = ["c", 'b','g','y','g','r','b'] # Color of each section
        textprops = {"fontsize":17} # Font size of text in pie chart

        plt.pie(lst, # Values
                labels = df1['Province_State'].unique(), # Labels for each sections
                labeldistance = 1,
                explode = explode, # To slice the perticuler section
                colors =colors, # Color of each section
                autopct = "%0.2f%%", # Show data in persentage for with 2 decimal point
                shadow = True, # Showing shadow of pie chart
                radius = 0.8, # Radius to increase or decrease the size of pie chart 
            startangle = 270, # Start angle of first section
                # rotatelabels=True,
                pctdistance=0.5,
        #         frame=True,
                textprops =textprops) 
        plt.title(title+'\n'+'(Vicky AI Production.)',loc='center',fontdict={'fontsize':16})
        plt.savefig(os.getcwd()+'/static'+f'figures/{title}.png')
