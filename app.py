from flask import Flask, render_template, jsonify
from main import main  # Import the main function from main.py

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script')
def run_script():
    TWITTER_USERNAME = ""
    TWITTER_PASSWORD = ""
    result = main(TWITTER_USERNAME, TWITTER_PASSWORD)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
