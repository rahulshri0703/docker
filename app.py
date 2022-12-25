from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home", methods=["POST", "GET"])
def home():
    p = ""
    if request.method == "POST":
        x = float(request.form["summer"])
        p = x
        p = x * 10000
    return render_template("home.html", new=p)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

# default port is 5000
# to run : docker run -d -p 8000:5000 image_name
