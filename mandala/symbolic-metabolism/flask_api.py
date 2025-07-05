from flask import Flask, request, jsonify, render_template
import csv
from agents import GlyphAgent

app = Flask(__name__)

# Load glyphs
def load_glyphs():
    with open("static/glyphs.csv", encoding="utf-8") as f:
        return list(csv.DictReader(f))

@app.route("/")
def index():
    return render_template("glyphs.jinja2", glyphs=load_glyphs())

@app.route("/dialogue", methods=["POST"])
def dialogue():
    data = request.json
    agent = GlyphAgent(data["glyph"], data["domain"], 5, 5)
    return jsonify({"response": agent.respond(data["input"])})

if __name__ == "__main__":
    app.run(debug=True)
