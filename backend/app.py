from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    url = data["url"]

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    paragraphs = soup.find_all("p")

    clean_text = "\n".join(p.get_text() for p in paragraphs)

    return jsonify({"text": clean_text[:1000]})

app.run(host="0.0.0.0", port=5000, debug=True)

