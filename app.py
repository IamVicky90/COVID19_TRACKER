from flask import Flask,request,render_template
import pandas as pd
from COVID19_TRACKER import COVID19_TRACKER
import os

def create_logs_folder_if_not_exist():
    if 'logs' not in os.listdir(os.getcwd()):
        os.mkdir('logs')
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.route("/", methods=['GET', 'POST'])
def home():
    create_logs_folder_if_not_exist()
    str_date=''
    try:
        with open('logs/date.cache','r') as f:
                str_date=f.read()
    except FileNotFoundError:
        print('No, date.cache file is here')
    except Exception as e:
        print('Error occured: '+str(e))
    return render_template('index.html',df_date='You are seeing the COVID19 situation in Pakistan till date: '+str_date)


@app.route('/refresh', methods=['GET', 'POST'])
def refresh():
    try:
        if request.method=='POST':
            COVID19_TRACKERobj=COVID19_TRACKER()
            df=COVID19_TRACKERobj.tracker()
            # str_date=str(df['Last_Update'][0])[0:10]
            # with open('logs/date.cache','w') as f:
            #     f.write(str_date)
            file_lst=['']
            if 'csv_files.txt' in os.listdir(os.getcwd()):
                with open('csv_files.txt','r') as r:
                    file_lst=r.read().split(' ')

            return render_template('index.html',df_date='You are seeing the COVID19 situation in Pakistan till date: '+file_lst[-2])
    except Exception as e:
        raise e
        return 'Unknown Error occured: '+str(e)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000")