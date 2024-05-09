from flask import Flask, render_template, request
from datetime import datetime
import requests

# Initialize Flask application
app = Flask(__name__)

# Define route for the home page
@app.route('/')


def home():
    # API key for accessing OpenWeatherMap API
    api_key = "4ccc7cabc4bac53437084c5a6f2e1781"
    # City for which weather forecast is requested
    city = 'Adelaide'
    # Construct the API URL with city and API key
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={api_key}&units=metric"
    print(url)
    # Send GET request to OpenWeatherMap API
    response = requests.get(url)
    #JSON response
    data = response.json()
    # Extract forecast list from API response
    forecast_list = data['list']
    index = 0
    forecast_data = []
    # Iterate through forecast list
    while index < len(forecast_list):
        # Extract relevant data for each forecast
        dt_txt = forecast_list[index]["dt_txt"]
        temp = forecast_list[index]["main"]["temp"]
        icon = forecast_list[index]["weather"][0]["icon"]
        description = forecast_list[index]["weather"][0]["description"]

        # Convert the string to a datetime object
        date_object = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
        # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
        day_of_week = date_object.weekday()
        print(day_of_week)
        # You can also get the day name
        day_name = date_object.strftime('%A')
        print(day_name)

        index +=8

        # Create dictionary for forecast data
        thisdict = {
                "dt_txt": dt_txt,
                "day_of_week": day_name,
                "temp": temp,
                "icon": "http://openweathermap.org/img/w/" + icon + ".png",
                "description": description
            }
        # Append forecast data to list
        forecast_data.append(thisdict)
    print(forecast_data)

    # Render HTML template with forecast data
    return render_template('home.html',forecast_data=forecast_data)

# def get_day_of_week(dt_txt):
#     date_object = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
#     day_of_week = date_object.weekday()
#     day_name = date_object.strftime('%A')
#     return day_name



if __name__ == '__main__':
    app.run(debug=True)

