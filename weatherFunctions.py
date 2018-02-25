import json
import requests

def setupCity(city):
    global data
    global cityName
    cityName = city
    url = "http://api.openweathermap.org/data/2.5/weather?q=%s&units=imperial&APPID=a08bf51b1569b6dff62559275a68f019" % (city)
    response = requests.get(url)
    response.raise_for_status()
    weatherData = json.loads(response.text)
    data = weatherData
    return data



def temperature():
        temp = data["main"]["temp"]
        return temp


def TypeOfWeatherAndImages():
        typeOfCondition = data["weather"][0]["main"]
        global imageData
        imageData = []


        if typeOfCondition == "Clear":
            imageData.append("clear")
            return "It's clear"


        elif typeOfCondition == "Clouds":
            imageData.append("cloudy")
            return "There are some scattered clouds"


        elif typeOfCondition == "Snow":
            imageData.append("snowy")
            return "It's snowy"


        elif typeOfCondition == "Sun":
            imageData.append("sunny")
            return "It's sunny"


        elif typeOfCondition == "light snow":
            imageData.append("snowy")
            return "Its snowy"


        elif typeOfCondition == "Haze":
            imageData.append("cloudy")
            return "Its hazy"


        elif typeOfCondition == "Light Rain":
            imageData.append("cloudy")
            return "It's raining lightly"


        elif typeOfCondition == "Mist":
            imageData.append("cloudy")
            return "It's misty"


        else:
            return "ERROR Getting Specific Type Of Weather!"



def getHighTemp():
        highTemp = data["main"]["temp_max"]
        return highTemp


def getLowTemp():
        lowTemp = data["main"]["temp_min"]
        return lowTemp


def getWeather():
    extraConditions = TypeOfWeatherAndImages()
    temp = temperature()
    highTemp = getHighTemp()
    lowTemp = getLowTemp()
    highTemp = str(highTemp)
    lowTemp = str(lowTemp)
    response = ("The weather in %s is %s degrees fahrenheit. \n %s. Also, today, there will be a high of %s degrees and a low of %s degrees. " % (cityName, temp, extraConditions, highTemp, lowTemp))
    return response
