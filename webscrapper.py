import os
from autoscraper import AutoScraper
class scrap_data:
    def __init__(self):
        pass
    def start_scrap(self):
        url='https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports'
        wanted_list=['01-01-2021.csv','Patch OH deaths from 2020-05-12 to 2021-04-26']
        scrapper=AutoScraper()
        result=scrapper.build(url,wanted_list)
        csv_files=[]
        file_lst=[]
        if 'csv_files.txt' in os.listdir(os.getcwd()):
            with open('csv_files.txt','r') as r:
                file_lst=r.read().split(' ')

        for item in result:
            if ('.csv' in item and '2021' in item) and (item not in file_lst):
                csv_files.append(item)
                with open('csv_files.txt','a+') as f:
                    f.write(item+' ')
        return csv_files