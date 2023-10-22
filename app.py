from flask import Flask, request, render_template, jsonify
import requests
app = Flask(__name__)

@app.route('/')
def get_page():
    return render_template('index.html')

@app.route('/weatherapp', methods = ['POST'])
def get_data():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    city = request.form['city']
    # city = request.form.get('city') --> can be written like this too.
    units = request.form['units']
    appid = request.form['appid']
    params = {'q':city, 'units':units, 'appid':appid}
    data = requests.get(url, params)
    return data.json()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5003)
