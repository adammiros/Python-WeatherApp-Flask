import weatherFunctions


def runWeatherAppLogic(city):
    weatherFunctions.setupCity(city)
    response = weatherFunctions.getWeather()
    return response
