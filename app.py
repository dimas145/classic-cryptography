from flask import Flask, render_template, request, send_from_directory
import os

STATIC_DIR = os.path.abspath("static")

app = Flask(__name__, static_folder=STATIC_DIR)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"), "img/favicon.ico", mimetype="image/vnd.microsoft.icon")
 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update", methods=["POST"])
def update():
   if request.method == "POST":
      name = request.form["name"]
      return "Hello " + name + "!"
    
if __name__ == "__main__":
   app.run()