from flask import Flask, render_template, jsonify, Response
import subprocess
import threading
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

    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            logger.info(output.strip())
            # Burada çıktıyı bir dosyaya veya veritabanına yazabilirsiniz
            # Örneğin: write_to_file(output.strip())

    # Hata kontrolü
    stderr_output = process.stderr.read()
    if stderr_output:
        logger.error(stderr_output.strip())


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start_eksi():
    try:
        logger.info("Eksi bot starting...")
        threading.Thread(target=run_eksi_bot).start()
        return jsonify({"status": "Eksi Bot started successfully."})
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return jsonify({"status": f"An error occurred: {str(e)}"}), 500


@app.route('/stream')
def stream():
    # Return a streaming response for SSE
    return Response(run_eksi_bot(), content_type='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)