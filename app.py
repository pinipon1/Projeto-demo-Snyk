import requests
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    r = requests.get("https://httpbin.org/get")
    return f"Hello, Flask! Response status: {r.status_code}"
if __name__ == "__main__":
    app.run(debug=True)
