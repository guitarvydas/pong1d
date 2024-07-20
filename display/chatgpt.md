Here's a solution using Python with Flask for the server and JavaScript for the front-end. The server will handle the commands via HTTP endpoints, and the front-end will update the display accordingly.

First, install Flask if you haven't already:
```sh
pip install flask
```

### Python (Flask) Server Code

Create a file named `server.py`:

```python
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

if __name__ == '__main__':
    app.run(debug=True)
```

### HTML/JavaScript (Front-End) Code

Create a folder named `templates` in the same directory as `server.py`, and inside it, create a file named `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dot Display</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        #container {
            display: grid;
            grid-template-columns: repeat(16, 1fr);
            gap: 5px;
        }
        .dot, .bam {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background-color: black;
            display: none;
        }
        .bam {
            background-color: red;
            width: auto;
            height: auto;
            border-radius: 0;
            font-size: 1.5em;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        #winner {
            display: none;
            font-size: 2em;
        }
    </style>
</head>
<body>
    <div id="container">
        <!-- 16 positions -->
        <div class="dot" id="dot-0"></div>
        <div class="dot" id="dot-1"></div>
        <div class="dot" id="dot-2"></div>
        <div class="dot" id="dot-3"></div>
        <div class="dot" id="dot-4"></div>
        <div class="dot" id="dot-5"></div>
        <div class="dot" id="dot-6"></div>
        <div class="dot" id="dot-7"></div>
        <div class="dot" id="dot-8"></div>
        <div class="dot" id="dot-9"></div>
        <div class="dot" id="dot-10"></div>
        <div class="dot" id="dot-11"></div>
        <div class="dot" id="dot-12"></div>
        <div class="dot" id="dot-13"></div>
        <div class="dot" id="dot-14"></div>
        <div class="dot" id="dot-15"></div>
        <!-- BAM positions -->
        <div class="bam" id="bam-0">BAM!</div>
        <div class="bam" id="bam-15">BAM!</div>
    </div>
    <div id="winner"></div>
    <script>
        async function updateDisplay() {
            const response = await fetch('/status');
            const data = await response.json();

            // Clear previous state
            document.querySelectorAll('.dot').forEach(dot => dot.style.display = 'none');
            document.querySelectorAll('.bam').forEach(bam => bam.style.display = 'none');
            document.getElementById('winner').style.display = 'none';

            if (data.winner) {
                document.getElementById('winner').innerText = data.winner === 'left' ? 'Player on the Left won!' : 'Player on the Right won!';
                document.getElementById('winner').style.display = 'block';
                return;
            }

            if (data.bam_active) {
                document.getElementById(`bam-${data.bam_position}`).style.display = 'flex';
            } else if (data.current_position !== null) {
                document.getElementById(`dot-${data.current_position}`).style.display = 'block';
            }
        }

        setInterval(updateDisplay, 100);
    </script>
</body>
</html>
```

### Flask Status Endpoint

Add the following route to `server.py` to provide status information to the front-end:

```python
@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        'current_position': current_position,
        'bam_active': bam_active,
        'bam_position': 0 if bam_active and current_position == 0 else 15,
        'winner': winner
    })
```

### Command Line Interface

To control the server from the command line, you can use `requests` to make HTTP POST requests. Create a script named `control.py`:

```python
import requests
import sys

def send_command(endpoint):
    response = requests.post(f'http://127.0.0.1:5000/{endpoint}')
    if response.status_code == 200:
        print("Command sent successfully")
    else:
        print("Failed to send command")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python control.py <command>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "start":
        send_command('pos/0')
    elif command.startswith("pos"):
        _, pos = command.split()
        send_command(f'pos/{pos}')
    elif command == "leftBAM":
        send_command('leftBAM')
    elif command == "rightBAM":
        send_command('rightBAM')
    elif command == "winnerL":
        send_command('winnerL')
    elif command == "winnerR":
        send_command('winnerR')
    else:
        print("Unknown command")
```

### Running the Server and Sending Commands

1. Start the server by running:
```sh
python server.py
```

2. Open a browser window and navigate to `http://127.0.0.1:5000`.

3. Use the control script to send commands. For example:
```sh
python control.py start
python control.py pos 5
python control.py leftBAM
python control.py winnerL
```

This setup should provide a local browser-based server that can display a dot at one of 16 positions and respond to various commands.
