from flask import Flask, render_template, jsonify
from threading import Thread
import time
from eksi import Eksi  # Eksi sınıfını içe aktarın

app = Flask(__name__)
eksi_instance = Eksi()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    def run_eksi():
        eksi_instance.setup()
        eksi_instance.login()
        while True:
            try:
                eksi_instance.send_post()
                eksi_instance.surf()
                eksi_instance.fav()
            except Exception as e:
                print(f'Error: {e}')
                eksi_instance.close_browser()
                eksi_instance.setup()
                eksi_instance.login()
                time.sleep(1)

    thread = Thread(target=run_eksi)
    thread.start()
    return jsonify({"status": "Eksi bot started!"})

if __name__ == '__main__':
    app.run(debug=True)