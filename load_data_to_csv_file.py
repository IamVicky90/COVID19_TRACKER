import pandas as pd
import os
class data_loader:
    def __init__(self):
        pass
    def create_csv(self,csv_files):
        if len(csv_files)>0:
            dfs=[]
            for file in csv_files:
                url=f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{file}'
                temp = pd.read_csv(url)
                dfs.append(temp[temp.Country_Region=='Pakistan'])
            
            if ('COVID19 Updated.csv') in os.listdir(os.getcwd()):
                df=pd.read_csv('COVID19 Updated.csv')
                dfs.append(df)
                df = pd.concat(dfs, ignore_index=True)
                df.to_csv('COVID19 Updated.csv')
            else:
                df = pd.concat(dfs, ignore_index=True)
                df.to_csv('COVID19 Updated.csv')
    def convert_csv_to_pandas_dataframe(self):
        df=pd.read_csv('COVID19 Updated.csv',usecols=['Province_State','Country_Region','Last_Update','Confirmed','Deaths','Recovered','Active','Case_Fatality_Ratio'])
        return df
        