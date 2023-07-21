from flask import Flask, render_template
import pandas as pd

app = Flask('website')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/v1/<station>/<date>')
def about(station, date):
    file_name = 'data_small/TG_STAID' + str(station).zfill(6) +'.txt'
    df = pd.read_csv(file_name, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10

    return {'station': station,
            'data': date,
            'temperature': temperature}

app.run(debug=True)