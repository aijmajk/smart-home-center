import requests
import pygame
import io

try:
    # Python2
    from urllib2 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen

CITY = "Lutynia"
LAT = "51.13519"
LON = "16.78271"
LANG = "PL"
UNITS = "metric"
API_KEY = "92f9fc86bfa069bd0671f4bd412eceb8"


def update_weather(screen_w, screen_h, font, fontcolor, font_height):
    screen = pygame.Surface((screen_w, screen_h))
    screen.fill((0, 0, 0))

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "lat=" + LAT + "&lon=" + LON + "&units=" + UNITS + "&appid=" + API_KEY + "&lang=" + LANG

    response = requests.get(URL)

    # checking the status code of the request
    if response.status_code == 200:
        data = response.json()
        main = data['main']

        # WEATHER IMAGE
        img_id = data['weather'][0]['icon']
        img_url = "http://openweathermap.org/img/wn/" + str(img_id) + "@2x.png"
        img_str = urlopen(img_url).read()
        img_file = io.BytesIO(img_str)
        img = pygame.image.load(img_file)
        img = pygame.transform.scale(img, (int(screen_w / 2), int(screen_h / 2)))
        # img = img.convert()
        screen.blit(img, (screen_w / 4, 0))

        # CURRENT WEATHER
        weatherScreen = pygame.Surface((screen_w, int(screen_h / 2)))
        weatherScreen.fill((0, 0, 0))
        description = font.render(f"{data['weather'][0]['description']}", True, fontcolor)
        temperature = font.render(f"temperatura: {main['temp']} °C", True, fontcolor)
        feels_like = font.render(f"odczuwalna: {main['feels_like']} °C", True, fontcolor)
        humidity = font.render(f"wilgotność: {main['humidity']}%", True, fontcolor)
        pressure = font.render(f"ciśnienie: {main['pressure']} hPa", True, fontcolor)
        visibility = font.render(f"widzialność: {data['visibility'] / 1000}km", True, fontcolor)

        # blit on weather screen
        weatherScreen.blit(description, (130, 0))
        weatherScreen.blit(temperature, (130, font_height))
        weatherScreen.blit(feels_like, (130, 2 * font_height))
        weatherScreen.blit(humidity, (130, 3 * font_height))
        weatherScreen.blit(pressure, (130, 4 * font_height))
        weatherScreen.blit(visibility, (130, 5 * font_height))
        screen.blit(weatherScreen, (0, int(screen_h / 2)))
    else:
        print("Error in the HTTP request")

    return screen
