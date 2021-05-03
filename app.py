from flask import Flask,request,render_template
import pandas as pd
from COVID19_TRACKER import COVID19_TRACKER

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    COVID19_TRACKERobj=COVID19_TRACKER()
    COVID19_TRACKERobj.tracker()
    return render_template('index.html')


@app.route('/refresh', methods=['GET', 'POST'])
def refresh():
    return 'Hellow'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000")