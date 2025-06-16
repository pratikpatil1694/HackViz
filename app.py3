from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    scenario = None
    if request.method == "POST":
        scenario = request.form.get("scenario")
    return render_template("index.html", scenario=scenario)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

