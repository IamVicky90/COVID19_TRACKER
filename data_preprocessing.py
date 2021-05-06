import pandas as pd
class process_data:
    def __init__(self):
        pass
    def date_processing(self,df1):
            df1["Last_Update"]=df1["Last_Update"].str.slice(0,10)
            df1["Last_Update"] = pd.to_datetime(df1["Last_Update"])
            df1=df1.sort_values(by="Last_Update",ascending=False).reset_index()
            return df1
    def derive_colum(self,col_to_create,derive_from,df1):
        df1[col_to_create]=0

        for province in df1['Province_State'].unique():
            lst=[]
            for row in df1[df1.Province_State==province][derive_from].values:
                lst.append(row)
            current=[]
            for i in range(len(lst)):
                if i==len(lst)-1:
                    current.append(None)
                    break
                j=i+1
                diff=lst[i]-lst[j]
                if diff<0:
                    current.append(0)
                else:
                    current.append(diff)

            j=0
            for i,flag in enumerate(df1.Province_State==province):
                if flag:
                    df1[col_to_create][i]=current[j]
                    j=j+1
    def remove_null_columns(self,df1):
        df1.dropna(inplace=True)
    def province_info(self,by,df1):
        sum=0
        lst=[]
        for province in ['Sindh', 'Gilgit-Baltistan', 'Punjab', 'Balochistan','Khyber Pakhtunkhwa', 'Islamabad',  'Azad Jammu and Kashmir']:
            lst.append(df1[df1['Province_State']==province][by].sum())
            sum+=df1[df1['Province_State']==province][by].sum()
        return lst,sum
    def remove_latest_date_in_Last_Update_Column_if_found_zero(self,df1):
        if df1['Cases in a day'][0]==0.0 and df1['Deaths in a day'][0]==0.0 and df1['Recovered in a day'][0]==0.0:
            df1=df1.iloc[7:,]
        else:
            check=df1['Last_Update'][7]
            if df1[df1['Last_Update']==check]['Cases in a day'][7]==0 and df1[df1['Last_Update']==check]['Recovered in a day'][7]==0 and df1[df1['Last_Update']==check]['Deaths in a day'][7]==0:
                df1=df1.loc[df1['Last_Update']!='2021-05-05',]
        df1.to_csv('logs/df1.cache')
        df1=pd.read_csv('logs/df1.cache')
        
        return self.date_processing(df1)
    def return_sum(self,df1,col_name):
        return str(int(df1[df1['Last_Update']==df1['Last_Update'][0]][col_name].sum()))
    

