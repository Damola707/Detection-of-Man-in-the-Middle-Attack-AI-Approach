from flask import Flask, render_template
from datetime import datetime
import threading

app = Flask(__name__)

# This will be populated with alert data from the packet sniffing script
alert_data = []

# Basic route to display alerts
@app.route('/')
def index():
    return render_template('index.html', alerts=alert_data)

def start_flask():
    app.run(debug=True, use_reloader=False)  # Avoid double-running in threading

# Run Flask in a separate thread
flask_thread = threading.Thread(target=start_flask)
flask_thread.start()
