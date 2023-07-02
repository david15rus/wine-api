from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<country>/<points>')
def country(country, points):
    df = pd.read_json('wine_date.json')
    df = df.loc[df['points'] >= int(points)]
    data = df.loc[df['country'] == country].to_dict(orient='records')
    return data


@app.route('/api/v1/<points>')
def points(points):
    df = pd.read_json('wine_date.json')
    data = df.loc[df['points'] >= int(points)].to_dict(orient='records')
    return data


if __name__ == '__main__':
    app.run(debug=True, port=5001)
