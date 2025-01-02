from flask import Flask, render_template, jsonify, Response
import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


def run_eksi_bot():
    process = subprocess.Popen(
        ['python', 'eksi.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    for line in process.stdout:
        yield f"data: {line}\n\n"

    for line in process.stderr:
        yield f"data: {line}\n\n"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start_eksi():
    try:
        logger.info("Eksi bot starting...")
        return jsonify({"status": "Eksi Bot started successfully."})
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return jsonify({"status": f"An error occurred: {str(e)}"}), 500


@app.route('/stream')
def stream():
    return Response(run_eksi_bot(), content_type='text/event-stream')


@app.route('/logs', methods=['GET'])
def get_logs():
    try:
        with open('eksi.log', 'r') as log_file:
            logs = log_file.read()
        return jsonify({"logs": logs})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
