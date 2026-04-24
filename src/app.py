from flask import Flask, render_template, request
from src.services.weather_service import fetch_weather

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        try:
            weather = fetch_weather(city)
        except Exception as e:
            error = str(e)

    return render_template("index.html", weather=weather, error=error)


if __name__ == "__main__":
    app.run(debug=True)