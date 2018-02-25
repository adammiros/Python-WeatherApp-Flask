import weatherFunctions


def runWeatherAppLogic(city):
    weatherFunctions.setupCity(city)
    response = weatherFunctions.getWeather()
    return response


def getImage():
    readyImage = weatherFunctions.imageData[0]
    return readyImage
    readyImage = []
