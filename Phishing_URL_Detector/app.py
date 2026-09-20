from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    url = request.form.get("url", "")

    score = 0
    reasons = []

    if not url.startswith("https://"):
        score += 1
        reasons.append("URL does not use HTTPS")

    if len(url) > 75:
        score += 1
        reasons.append("URL is unusually long")

    if score >= 2:
        risk = "SUSPICIOUS"
    elif score == 1:
        risk = "MEDIUM RISK"
    else:
        risk = "SAFE"

    return render_template(
        "index.html",
        risk=risk,
        score=score,
        reasons=reasons,
        url=url
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)