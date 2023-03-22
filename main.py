from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<station>/<date>')
def api(station, date):
    #df = pd.read_csv("")
    temperature = 23
    return {'station': station,
            'date': date,
            'temperature': temperature}


if __name__ == '__main__':
    app.run(debug=True)
