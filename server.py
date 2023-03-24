import random
from flask import Flask  # platform in my computer to run my app
from settings import weather_token
from settings import giphy_token
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World! write /weather/city after the / to get a cool thing'


@app.route('/weather/<city>')
def weather(city):
    url1 = "https://api.openweathermap.org/data/2.5/weather"
    params1 = {'q': city, 'units': 'metric', 'appid': weather_token}
    response1 = requests.get(url=url1, params=params1)
    temp = response1.json()['main']['temp']
    if temp < 0:
        a = random.choice(["snow", "winter", "cold", "rain"])
    elif 0 < temp < 20:
        a = random.choice(["Coat", "sweater", "wool hat", "boots", "raincoat", "cosy"])
    else:
        a = random.choice(["hot", "warm", "beach"])
    url = "http://api.giphy.com/v1/gifs/translate"
    params = {'api_key': giphy_token, 's': a}
    response = requests.get(url=url, params=params)
    if response.status_code != 200:
        return ""
    giphy = response.json()['data']['images']['original']['url']
    # print(giphy)
    return f"<h2>Hello, today is {temp} C° </h2>" + f"<img src={giphy}>" + "<style>body{height: 300px;background-color: red; background-image: linear-gradient(to right, Red , Orange, Yellow, Green, Blue, Indigo, Violet);}</style>"


if __name__ == "__main__":
    app.run()
