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


def temperature():
        temp = data["main"]["temp"]
        return temp


def extraTypeOfConditions():
        typeOfCondition = data["weather"][0]["main"]

        if typeOfCondition == "Clear":
            return "It's clear"

        elif typeOfCondition == "Clouds":
            return "There are some scattered clouds"

        elif typeOfCondition == "Snow":
            return "It's snowy"

        elif typeOfCondition == "Sun":
            return "It's sunny"

        elif typeOfCondition == "light snow":
            return "Its snowy"

        elif typeOfCondition == "Haze":
            return "Its hazy"

        else:
            return "ERROR Getting Specific Type Of Weather!"


def getHighTemp():
        highTemp = data["main"]["temp_max"]
        return highTemp


def getLowTemp():
        lowTemp = data["main"]["temp_min"]
        return lowTemp


def getWeather():
    extraConditions = extraTypeOfConditions()
    temp = temperature()
    highTemp = getHighTemp()
    lowTemp = getLowTemp()
    highTemp = str(highTemp)
    lowTemp = str(lowTemp)
    return("The weather in %s is %s degrees fahrenheit \n %s \n. Also, today, there will be a high of %s degrees and a low of %s degrees. " % (cityName, temp, extraConditions, highTemp, lowTemp))
