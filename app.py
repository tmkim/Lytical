# app.py

# import required libraries
# remember to add in libraries to requirements.txt
import os
import requests
from flask import Flask, render_template, request, json
import data_analysis

# initialize Flask
app = Flask(__name__)

# return main page if no parameters passed
# INCOMPLETE
@app.route('/')
def main_page():
    return render_template('index.html')
	
# return charts
@app.route('/viewData')
def viewData():
    # app logic goes here
    # needs to return arrays like [ [time, tps], [time, tps], [time, tps] ] --> web
    # example -> formattedresult = [[1, 50], [2, 100], [5,500]]
    return render_template('chart.html',tps=formattedresult)

# NOT SURE IF NEEDED
# @app.route('/process')
def dataMagic():
	data = 'test_data'
	formattedresult = data_analysis.getprocessedTPM(data)
    	
# run app
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)