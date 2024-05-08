from flask import Flask, request,render_template
from weather import weather_status
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['citys']
    try:
       status,temperature = weather_status(city)
       temperature = int(temperature)
       notice = city
    except:
        status,temperature ='',''
        notice  = weather_status(city)
    
    return render_template('index.html',status=status, temperature=temperature ,notice= notice, symbol = "C")