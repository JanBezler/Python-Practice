import requests
from flask import Flask, render_template


url = "https://www.metaweather.com/api/location/523920"
api_output = None
weather_list = []

r = requests.get(url)
page_source = r.text
exec(f"api_output = {page_source}")
weather = api_output.get("consolidated_weather")

for item in weather:
    weather_list.append(
        {"date": item.get("applicable_date"),
         "state": item.get("weather_state_name"),
         "temp": round(item.get("the_temp"), 2),
         "temp_max": round(item.get("max_temp"), 2),
         "temp_min": round(item.get("min_temp"), 2),
         "wind_direction": item.get("wind_direction_compass")})

# FLASK
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', weather=weather_list)


if __name__ == "__main__":
    app.run()
