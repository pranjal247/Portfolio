from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    profile = {
        "name": "Pranjal Tiwari",
        "title": "Electrical & Computer Engineer | IoT Enthusiast",
        "about": "B.Tech graduate from SRM Institute of Science and Technology with interests in IoT, Embedded Systems and Cloud Engineering.",
    }

    return render_template("index.html", profile=profile)


if __name__ == "__main__":
    app.run(debug=True)