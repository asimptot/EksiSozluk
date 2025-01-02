from flask import Flask, render_template, jsonify, Response
import subprocess
import threading

app = Flask(__name__)


def run_eksi_bot():
    process = subprocess.Popen(
        ['python', 'eksi.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Stream output to the front-end
    for line in process.stdout:
        # Here we yield the output line to send it to the client in real time
        yield f"data: {line}\n\n"

    # Check for errors
    for line in process.stderr:
        yield f"data: {line}\n\n"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start_eksi():
    try:
        # Start the bot in a separate thread so it doesn't block the main process
        threading.Thread(target=run_eksi_bot).start()
        return jsonify({"status": "Eksi Bot started successfully."})
    except Exception as e:
        return jsonify({"status": f"An error occurred: {str(e)}"}), 500


@app.route('/stream')
def stream():
    # Return a streaming response for SSE
    return Response(run_eksi_bot(), content_type='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)
