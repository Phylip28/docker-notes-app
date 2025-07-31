from flask import Flask, request, render_template
import os

app = Flask(__name__)

NOTES_FILE = "data/notes.txt"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            with open(NOTES_FILE, "a") as f:
                f.write(note + "\n")
    notes = []
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            notes = f.readlines()
    return render_template("index.html", notes=notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
