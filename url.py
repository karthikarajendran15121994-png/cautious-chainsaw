<<<<<<< HEAD
from urllib.parse import urlparse

def check_url(url):
    score = 0
    reasons = []

    # Check HTTPS
    if not url.startswith("https://"):
        score += 1
        reasons.append("URL does not use HTTPS")

    # Parse URL
    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    # Check for @ symbol
    if "@" in url:
        score += 2
        reasons.append("URL contains @ symbol")

    # Check for IP address instead of domain name
    parts = domain.split(".")
    if len(parts) == 4 and all(part.isdigit() for part in parts):
        score += 2
        reasons.append("URL uses an IP address")

    # Check suspicious words
    suspicious_words = [
        "login", "verify", "verification",
        "secure", "account", "update",
        "password", "bank", "confirm"
    ]

    for word in suspicious_words:
        if word in url.lower():
            score += 1
            reasons.append(f"Contains suspicious word: {word}")

    # Check URL length
    if len(url) > 100:
        score += 1
        reasons.append("URL is unusually long")

    # Final result
    if score >= 4:
        result = "PHISHING / HIGH RISK"
    elif score >= 2:
        result = "SUSPICIOUS"
    else:
        result = "LOW RISK"

    return result, score, reasons


# Main program
url = input("Enter a URL: ")

result, score, reasons = check_url(url)

print("\n--- Phishing URL Detector ---")
print("URL:", url)
print("Risk Level:", result)
print("Risk Score:", score)

if reasons:
    print("\nReasons:")
    for reason in reasons:
        print("-", reason)
else:
=======
from urllib.parse import urlparse

def check_url(url):
    score = 0
    reasons = []

    # Check HTTPS
    if not url.startswith("https://"):
        score += 1
        reasons.append("URL does not use HTTPS")

    # Parse URL
    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    # Check for @ symbol
    if "@" in url:
        score += 2
        reasons.append("URL contains @ symbol")

    # Check for IP address instead of domain name
    parts = domain.split(".")
    if len(parts) == 4 and all(part.isdigit() for part in parts):
        score += 2
        reasons.append("URL uses an IP address")

    # Check suspicious words
    suspicious_words = [
        "login", "verify", "verification",
        "secure", "account", "update",
        "password", "bank", "confirm"
    ]

    for word in suspicious_words:
        if word in url.lower():
            score += 1
            reasons.append(f"Contains suspicious word: {word}")

    # Check URL length
    if len(url) > 100:
        score += 1
        reasons.append("URL is unusually long")

    # Final result
    if score >= 4:
        result = "PHISHING / HIGH RISK"
    elif score >= 2:
        result = "SUSPICIOUS"
    else:
        result = "LOW RISK"

    return result, score, reasons


# Main program
url = input("Enter a URL: ")

result, score, reasons = check_url(url)

print("\n--- Phishing URL Detector ---")
print("URL:", url)
print("Risk Level:", result)
print("Risk Score:", score)

if reasons:
    print("\nReasons:")
    for reason in reasons:
        print("-", reason)
else:
>>>>>>> 25c9d58ac411fff9056f03851950aa708f3efb9b
    print("\nNo obvious suspicious characteristics detected.")