from flask import Flask, render_template, request
from datetime import datetime
import requests


app = Flask(__name__)

@app.route('/')


def home():
    api_key = "4ccc7cabc4bac53437084c5a6f2e1781"
    city = 'Adelaide'
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={api_key}&units=metric"
    print(url)
    response = requests.get(url)
    data = response.json()



        # "description": data["weather"][0]["description"],
        # "temperature": data["main"]["temp"],n
        # "humidity": data["main"]["humidity"],
        # "wind_speed": data["wind"]["speed"]}

    forecast_list = data['list']
    index = 0
    forecast_data = []
    while index < len(forecast_list):

        dt_txt = forecast_list[index]["dt_txt"]
        temp = forecast_list[index]["main"]["temp"]
        icon = forecast_list[index]["weather"][0]["icon"]
        description = forecast_list[index]["weather"][0]["description"]
        index +=8

        today = datetime(2017, 10, 20)
        today.get_weekday()

        thisdict = {
                "dt_txt": dt_txt,
                "temp": temp,
                "icon": "http://openweathermap.org/img/w/" + icon + ".png",
                "description": description
            }
        forecast_data.append(thisdict)
        print(forecast_data)


        return render_template('home.html',forecast_data=forecast_data)




if __name__ == '__main__':
    app.run(debug=True)

