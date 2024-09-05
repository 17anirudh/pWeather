import requests
import json
import time
import sys

class Network:
    
    def verify(self, a, RED, RESET):
        url = f'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID={a}'
        b = requests.get(url)
        if b.status_code == 200:
            print('Valid API key')
        else:
            sys.exit(f'{RED}Invalid API key{RESET}')

    def Coord(self, alpha, user_input, api_key, RED, RESET):
        if isinstance(user_input, int):
            #Zip code
            url = f'https://api.openweathermap.org/data/2.5/weather?zip={user_input},{alpha}&appid={api_key}'
            response = requests.get(url)
            if response.status_code == 200:
                return response.content
            else: 
                print('fail')
        else:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={user_input},{alpha}&appid={api_key}'
            response = requests.get(url)
            if response.status_code == 200:
                return response.content
            else: 
                sys.exit(f"{RED} Something abnormal happened, couldn't find....{RESET}")

    def Display(self, response, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, RESET):
        jsonn = json.loads(response)

        temp = jsonn["main"]["temp"]
        temp -= 273.15
        temp = round(temp, 2)
        temp = str(temp)
        temp += '°C'

        temp_max = jsonn["main"]["temp_max"]
        temp_max -= 273.15
        temp_max = round(temp_max, 2)
        temp_max = str(temp_max)
        temp_max += '°C'

        temp_min = jsonn["main"]["temp_min"]
        temp_min -= 273.15
        temp_min = round(temp_min, 2)
        temp_min = str(temp_min)
        temp_min += '°C'

        feels_like = jsonn["main"]["feels_like"]
        feels_like -= 273.15
        feels_like = round(feels_like, 2)
        feels_like = str(feels_like)
        feels_like += '°C'

        pressure = jsonn["main"]["pressure"]
        pressure = str(pressure)
        pressure += 'hPa'

        humidity = jsonn["main"]["humidity"]
        humidity = str(humidity)
        humidity += '%'

        visibility = int(jsonn["visibility"])
        visibility /= 1000
        visibility = str(visibility)
        visibility = str(visibility) + 'm'

        wind_speed = jsonn["wind"]["speed"]
        wind_speed = str(wind_speed)
        wind_speed += 'm/s'

        cloud = jsonn["clouds"]["all"]
        cloud = str(cloud)
        cloud += '%'

        sunrise = jsonn["sys"]["sunrise"]
        sunrise += jsonn["timezone"]
        te = time.gmtime(int(sunrise))
        sunrise = time.strftime('%I:%M %p', te)

        sunset = jsonn["sys"]["sunset"]
        sunset += jsonn["timezone"]
        te = time.gmtime(int(sunset))
        sunset = time.strftime('%I:%M %p', te)

        #temp, min, max, feels, pressure, humidity, visibility, wind, cloud, sunrise and sunset
        print(f"Temperature: {GREEN}{temp}{RESET}\nMax Temperature: {RED}{temp_max}{RESET}\nMin Temperature: {BLUE}{temp_min}{RESET}\nFeels like: {YELLOW}{feels_like}{RESET}\nPressure: {CYAN}{pressure}{RESET}\nHumidity: {GREEN}{humidity}{RESET}\nWind: {MAGENTA}{wind_speed}{RESET}\nCloud: {BLUE}{cloud}{RESET}\nSunrise: {sunrise}\nSunset: {sunset}")

        snow = jsonn.get("snow", {}).get("1h", None)
        if snow is not None:
            snow = str(snow) + 'mm'
            print(f'Snow: {RED}{snow}{RESET}')

        # Check for rain
        rain = jsonn.get("rain", {}).get("1h", None)
        if rain is not None:
            rain = str(rain) + 'mm'
            print(f'Rain: {RED}{rain}{RESET}')
        