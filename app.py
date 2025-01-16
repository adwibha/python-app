from flask import Flask, render_template
import pyspeedtest

app = Flask(__name__)

@app.route('/')
def home():
    # Initialize SpeedTest
    speed = pyspeedtest.SpeedTest()

    # Perform download, upload, and ping tests
    download_speed = speed.download() / 1_000_000  # Convert to Mbps
    upload_speed = speed.upload() / 1_000_000      # Convert to Mbps
    ping = speed.ping()

    # Render the results in HTML
    return render_template('index.html', download_speed=download_speed, upload_speed=upload_speed, ping=ping)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
