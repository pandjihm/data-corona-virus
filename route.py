from flask import Flask, render_template
import requests, schedule

app = Flask (__name__)

def covid():
    api_url = "https://api.kawalcorona.com/indonesia/"
    total = requests.get(api_url).json()
    return total

refresh = schedule.every(5).seconds.do(covid)

data_covid = covid()

@app.route("/")
def index():
    return render_template("index.html", data_covid = data_covid)

@app.route("/index.html")
def beranda():
    return render_template("index.html", data_covid = data_covid)

@app.route("/tentang-kami.html")
def tentang():
    return render_template("tentang-kami.html")

if __name__ == "__main__":
    app.run(debug=True)