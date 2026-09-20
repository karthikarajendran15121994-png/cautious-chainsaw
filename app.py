from flask import Flask, render_template, request
from urllib.parse import urlparse
import re

app = Flask(__name__)


def detect_phishing(url):
    score = 0
    reasons = []

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed = urlparse(url)
    hostname = parsed.hostname

    if not hostname:
        return 10, "DANGEROUS", ["Invalid URL"]

    # HTTPS
    if parsed.scheme != "https":
        score += 1
        reasons.append("URL does not use HTTPS")

    # URL length
    if len(url) > 75:
        score += 1
        reasons.append("URL is unusually long")

    # @ symbol
    if "@" in url:
        score += 2
        reasons.append("URL contains @ symbol")

    # IP address
    ip_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"

    if re.match(ip_pattern, hostname):
        score += 3
        reasons.append("URL uses an IP address instead of a domain")

    # Suspicious words
    suspicious_words = [
        "login",
        "verify",
        "account",
        "password",
        "bank",
        "confirm",
        "signin",
        "update",
        "secure"
    ]

    found = []

    for word in suspicious_words:
        if word in url.lower():
            found.append(word)

    if found:
        score += 1
        reasons.append(
            "Suspicious keywords: " + ", ".join(found)
        )

    # Many subdomains
    if hostname.count(".") >= 3:
        score += 1
        reasons.append("Many subdomains detected")

    # Risk level
    if score >= 6:
        risk = "DANGEROUS"
    elif score >= 3:
        risk = "SUSPICIOUS"
    else:
        risk = "LOW RISK"

    return score, risk, reasons


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":
        url = request.form.get("url", "").strip()

        if url:
            score, risk, reasons = detect_phishing(url)

            result = {
                "url": url,
                "score": score,
                "risk": risk,
                "reasons": reasons
            }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

