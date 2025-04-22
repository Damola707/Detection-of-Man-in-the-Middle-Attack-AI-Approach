from flask import Flask, render_template
import json
import os

app = Flask(__name__)
ALERTS_FILE = "alerts.json"

@app.route('/')
def index():
    if not os.path.exists(ALERTS_FILE):
        alerts = []
    else:
        with open(ALERTS_FILE, 'r') as f:
            try:
                alerts = json.load(f)
            except json.JSONDecodeError:
                alerts = []
    return render_template("dashboard.html", alerts=alerts)

if __name__ == '__main__':
    app.run(debug=True)
