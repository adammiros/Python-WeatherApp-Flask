from flask import Flask, render_template, request
import weatherFunctions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        city = request.form["city"]
        weatherFunctions.setupCity(city)
        response = weatherFunctions.getWeather()
        image = weatherFunctions.imageData[0]
        return render_template("response.html", weatherResponse=response, image = image)

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, host="159.65.230.87", port=80)
