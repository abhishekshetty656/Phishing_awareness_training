suspicious_words = [
    "login",
    "verify",
    "secure",
    "bank",
    "update",
    "bonus",
    "free"
]

url = input("Enter a URL: ")

found = False

for word in suspicious_words:
    if word in url.lower():
        found = True

if found:
    print("\n Suspicious URL Detected!")
else:
    print("\n URL looks safe.")