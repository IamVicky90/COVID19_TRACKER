import pandas as pd
import datetime
from webscrapper import scrap_data
from load_data_to_csv_file import data_loader
from data_preprocessing import process_data
import draw_figures
import time
import os
import warnings
warnings.filterwarnings('ignore')
class COVID19_TRACKER:
    def __init__(self):
        
        self.data_loader_obj=data_loader()
        self.scrap_data_obj=scrap_data()
        self.process_data_obj=process_data()
        self.draw_figures_obj=draw_figures.figure()
    def tracker(self):
        csv_files=self.scrap_data_obj.start_scrap()
        self.data_loader_obj.create_csv(csv_files)
        df1=self.data_loader_obj.convert_csv_to_pandas_dataframe()
        df1=self.process_data_obj.date_processing(df1)
        self.process_data_obj.derive_colum('Cases in a day','Confirmed',df1)
        self.process_data_obj.derive_colum('Deaths in a day','Deaths',df1)
        self.process_data_obj.derive_colum('Recovered in a day','Recovered',df1)
        self.process_data_obj.remove_null_columns(df1)
        df1=self.process_data_obj.remove_latest_date_in_Last_Update_Column_if_found_zero(df1)
        
        total_cases_by_province_lst,sum=self.process_data_obj.province_info('Cases in a day',df1)
        total_deaths_by_province_lst,death_sum=self.process_data_obj.province_info('Deaths in a day',df1)
        total_recoveries_by_province_lst,recovered_sum=self.process_data_obj.province_info('Recovered in a day',df1)
        
        self.draw_figures_obj.lineplot(df1['Last_Update'],df1['Cases in a day'],title='COVID19 Cases IN PAKISTAN FROM 2021',legend=['Total Cases since 2021: '+str(int(sum)),f"Today's cases are {self.process_data_obj.return_sum(df1,'Cases in a day')}"],color='g')
        self.draw_figures_obj.lineplot(df1['Last_Update'],df1['Deaths in a day'],title='COVID19 Deaths IN PAKISTAN FROM 2021',legend=['Total Deaths since 2021: '+str(int(death_sum))+f"\nToday's deaths are {self.process_data_obj.return_sum(df1,'Deaths in a day')}"],color='r')
        self.draw_figures_obj.lineplot(df1['Last_Update'],df1['Recovered in a day'],title='COVID19 Recoveries IN PAKISTAN FROM 2021',legend=['Total Recoveries since 2021: '+str(int(recovered_sum))+f"\nToday's recoveries are {self.process_data_obj.return_sum(df1,'Recovered in a day')}"],color='b')
        self.draw_figures_obj.lineplot(df1['Last_Update'],df1['Cases in a day'],hue=df1['Province_State'],title='COVID19 Cases BY PROVOINCE FROM 2021',legend=['None'],color=None)
        self.draw_figures_obj.lineplot(df1['Last_Update'],df1['Deaths in a day'],hue=df1['Province_State'],title='COVID19 DEATHS BY PROVOINCE FROM 2021',legend=['None'],color=None)
        self.draw_figures_obj.lineplot(df1['Last_Update'],df1['Recovered in a day'],hue=df1['Province_State'],title='COVID19 Recoveries BY PROVOINCE FROM 2021',legend=['None'],color=None)
        self.draw_figures_obj.pie_plot(total_cases_by_province_lst,'Total Corronavirus Cases by Province',df1)
        self.draw_figures_obj.pie_plot(total_deaths_by_province_lst,'Total Corronavirus Deaths by Province',df1)
        self.draw_figures_obj.pie_plot(total_recoveries_by_province_lst,'Total Corronavirus Recoveries by Province',df1)
        self.draw_figures_obj.ratio_between_deaths_and_recoveries(int(death_sum),int(recovered_sum))
        return df1
    
    

