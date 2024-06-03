from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)
data = pd.read_csv('./data/bicycleRoutesAnalysis.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/routes')
def routes():
    routes_data = data.to_dict(orient='records')
    return jsonify(routes_data)