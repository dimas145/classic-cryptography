from flask import Flask, render_template, request, send_from_directory
import os
import re

import algorithms

STATIC_DIR = os.path.abspath("static")

vigenere_vipher = algorithms.VigenereCipher()

app = Flask(__name__, static_folder=STATIC_DIR)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"),
                               "img/favicon.ico",
                               mimetype="image/vnd.microsoft.icon")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form", methods=["POST"])
def form():
    if request.method == "POST":
        cipher_id = request.form["cipher_id"]
        return render_template("form/form" + str(cipher_id) + ".html")


@app.route("/update", methods=["POST"])
def update():
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["key"]
        command = request.form["command"]
        type = request.form["type"]
        alphabets = re.sub(r'[^a-zA-Z]', '', text).upper()
        if (type == "1"):
            result = ""
            if (command == "encrypt"):
                result = vigenere_vipher.encrypt(text, key)
            else:
                result = vigenere_vipher.decrypt(text, key)
            return result
        else:
            return key + " " + command + " " + type + " " + alphabets


@app.route("/action", methods=["POST"])
def action():
    if request.method == "POST":
        state = request.form["state"]
        return "State : " + state


if __name__ == "__main__":
    app.run()
