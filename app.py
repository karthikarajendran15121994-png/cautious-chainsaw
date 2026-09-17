from flask import Flask, render_template, request
from urllib.parse import urlparse

app = Flask(__name__)


def check_url(url):
    score = 0
    reasons = []

    if not url.startswith("https://"):
        score += 1
        reasons.append("URL does not use HTTPS")

    parsed = urlparse(url)
    domain = parsed.netloc

    if "@" in url:
        score += 2
        reasons.append("URL contains @ symbol")

    parts = domain.split(".")

    if len(parts) == 4 and all(part.isdigit() for part in parts):
        score += 2
        reasons.append("URL uses an IP address")

    suspicious_words = [
        "login", "verify", "account",
        "password", "bank", "update",
        "confirm", "secure"
    ]

    for word in suspicious_words:
        if word in url.lower():
            score += 1
            reasons.append(f"Suspicious word found: {word}")

    if len(url) > 100:
        score += 1
        reasons.append("URL is unusually long")

    if score >= 4:
        result = "PHISHING / HIGH RISK"
        level = "danger"
    elif score >= 2:
        result = "SUSPICIOUS"
        level = "warning"
    else:
        result = "LOW RISK"
        level = "safe"

    return result, score, reasons, level


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    score = None
    reasons = []
    level = None
    url = ""

    if request.method == "POST":

        url = request.form.get("url", "").strip()

        if url:
            result, score, reasons, level = check_url(url)

    return render_template(
        "index.html",
        result=result,
        score=score,
        reasons=reasons,
        level=level,
        url=url
    )


if __name__ == "__main__":
    app.run(debug=True)