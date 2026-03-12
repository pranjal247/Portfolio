from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    profile = {
        "name": "Pranjal Tiwari",
        "title": "Electrical & Computer Engineer | Digital Marketing | IoT Enthusiast",
        "about": "B.Tech graduate from SRM Institute of Science and Technology with interests in IoT, Embedded Systems and Digital Marketing.",
    }

    return render_template("index.html", profile=profile)


if __name__ == "__main__":
    app.run(debug=True)