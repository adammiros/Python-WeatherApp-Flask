from flask import Flask, render_template, request
import weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        city = request.form["city"]
        response = weather.runWeatherAppLogic(city)
        imageData = weather.getImage()
        return render_template("response.html", weatherResponse=response, image = imageData)

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
