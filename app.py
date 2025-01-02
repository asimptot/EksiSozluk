from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

# Route to serve the index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to start the Eksi bot
@app.route('/start', methods=['POST'])
def start_eksi():
    try:
        # Run eksi.py as a subprocess
        subprocess.Popen(['python', 'eksi.py'])
        return jsonify({"status": "Eksi Bot started successfully."})
    except Exception as e:
        return jsonify({"status": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
