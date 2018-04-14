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
        setupCity(city)
        typeOfCondition = data["weather"][0]["main"]
        weatherSeverity = 0
        global imageData
        imageData = []


        if typeOfCondition == "Clear":
            imageData.append("clear")
            return "It's clear"
            weatherSeverity = 0
            determinSeverity()


        elif typeOfCondition == "Clouds":
            imageData.append("cloudy")
            return "There are some scattered clouds"
            weatherSeverity = weatherSeverity = 1
            determinSeverity()


        elif typeOfCondition == "Snow":
            imageData.append("snowy")
            return "It's snowy"
            weatherSeverity = weatherSeverity = 5 
            determinSeverity()


        elif typeOfCondition == "Sun":
            imageData.append("sunny")
            return "It's sunny"
            weatherSeverity = 0
            determinSeverity()


        elif typeOfCondition == "light snow":
            imageData.append("snowy")
            return "Its snowy"
            weatherSeverity = weatherSeverity = 2
            determinSeverity()


        elif typeOfCondition == "Haze":
            imageData.append("cloudy")
            return "Its hazy"
            weatherSeverity = weatherSeverity = 1
            determinSeverity()


        elif typeOfCondition == "Light Rain":
            imageData.append("cloudy")
            return "It's raining lightly"
            weatherSeverity = weatherSeverity = 1
            determinSeverity()


        elif typeOfCondition == "Mist":
            imageData.append("cloudy")
            return "It's misty"
            weatherSeverity = weatherSeverity = 1
            determinSeverity()

        
        else:
            return "ERROR Getting Specific Type Of Weather!"


def determinSeverity():
    if weatherSeverity = 0:
        return "It will be calm since weather severity is very low"

    elif weatherSeverity = 1:
        return "Weather severity is low. You should be fine"

    elif weatherSeverity = 2:
        return "Weather severity is picking up. You should have a little bit of caution."

    elif weatherSeverity = 3:
        return "Weather severity is at a medium level. Please be careful"
        
    elif weatherSeverity > 3: 
        return "Ok now its dangerous please try to avoid the roads if possible!"



def getHighTemp():
        highTemp = data["main"]["temp_max"]
        return highTemp


def getLowTemp():
        lowTemp = data["main"]["temp_min"]
        return lowTemp


def getWeather():
    extraConditions = TypeOfWeatherAndImages()
    temperature = temperature()
    highTemp = str(getHighTemp())
    lowTemp = str(getlowTemp)

    return extraConditions
    return temperature
    return highTemp
    return lowTemp
    

def Return Response():
    getWeather()
    response = ("The weather in %s is %s degrees fahrenheit. \n %s. Also, today, there will be a high of %s degrees and a low of %s degrees. " % (cityName, temp, extraConditions, highTemp, lowTemp))
    return response