import weatherFunctions

cityInput = input("What city would you like to get the weather for? \n")

weatherFunctions.setupCity(cityInput)
response = weatherFunctions.getWeather()
print(response)
