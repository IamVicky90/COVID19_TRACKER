from flask import Flask,request,render_template
import pandas as pd
from COVID19_TRACKER import COVID19_TRACKER
import os
import smtplib


def create_logs_folder_if_not_exist():
    if 'logs' not in os.listdir(os.getcwd()):
        os.mkdir('logs')
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
def get_file_lst():
    file_lst=['']
    if 'csv_files.txt' in os.listdir(os.getcwd()):
        with open('csv_files.txt','r') as r:
            file_lst=r.read().split(' ')
    return file_lst

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
            
            file_lst=get_file_lst()
            

            return render_template('index.html',df_date='You are seeing the COVID19 situation in Pakistan till date: '+file_lst[-2])
    except Exception as e:
        raise e
        return 'Sorry we cannot proceed '+str(e)
@app.route('/on_submit', methods=['GET', 'POST'])
def on_submit():
    try:
        if request.method=='POST':
            try:
                email=request.form['email']
                message=request.form['message']
                
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                
                server.login('vickyaiproduction@gmail.com', '25mar2001')
                server.sendmail('vickyaiproduction@gmail.com', 'waqasbilal02@gmail.com', email+'(email ID)\nMessage: '+message)
                server.sendmail('vickyaiproduction@gmail.com', email, 'Thank You! for your response we will definately look into this!\nStay Home Stay Safe!')
                server.close()
            except Exception as e:
                raise e
                pass

            file_lst=get_file_lst()
            return render_template('index.html',df_date='You are seeing the COVID19 situation in Pakistan till date: '+file_lst[-2])
        else:
            return 'Sorry we cannot proceed '
    except Exception as e:
        raise e
        return 'Sorry we cannot proceed '+str(e)
    
    



if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000")
