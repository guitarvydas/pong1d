from flask import Flask, render_template, jsonify
import time
import threading

app = Flask(__name__)
current_position = None
bam_active = False
winner = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pos/<int:position>', methods=['POST'])
def set_position(position):
    global current_position, bam_active, winner
    current_position = position
    bam_active = False
    winner = None
    return jsonify(success=True)

@app.route('/leftBAM', methods=['POST'])
def left_bam():
    global bam_active
    bam_active = True
    threading.Thread(target=bam_display, args=(0,)).start()
    return jsonify(success=True)

@app.route('/rightBAM', methods=['POST'])
def right_bam():
    global bam_active
    bam_active = True
    threading.Thread(target=bam_display, args=(15,)).start()
    return jsonify(success=True)

@app.route('/winnerL', methods=['POST'])
def winner_left():
    global winner
    winner = 'left'
    return jsonify(success=True)

@app.route('/winnerR', methods=['POST'])
def winner_right():
    global winner
    winner = 'right'
    return jsonify(success=True)

def bam_display(position):
    global bam_active
    time.sleep(0.5)
    bam_active = False

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        'current_position': current_position,
        'bam_active': bam_active,
        'bam_position': 0 if bam_active and current_position == 0 else 15,
        'winner': winner
    })

if __name__ == '__main__':
    app.run(debug=True)
