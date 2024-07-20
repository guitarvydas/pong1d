To achieve this using JavaScript, you can use Node.js along with the Express framework for the server-side logic, and plain HTML/CSS/JavaScript for the client-side.

First, ensure you have Node.js installed. You can download it from [nodejs.org](https://nodejs.org/).

### Step 1: Setup the Node.js Server

Create a new directory for your project and navigate into it. Then initialize a new Node.js project and install Express:

```sh
mkdir dot-display
cd dot-display
npm init -y
npm install express
```

### Step 2: Create the Server

Create a file named `server.js` and add the following code:

```javascript
const express = require('express');
const app = express();
const port = 3000;

let currentPosition = null;
let bamActive = false;
let bamPosition = null;
let winner = null;

app.use(express.static('public'));

app.get('/status', (req, res) => {
    res.json({ currentPosition, bamActive, bamPosition, winner });
});

app.post('/pos/:position', (req, res) => {
    currentPosition = parseInt(req.params.position, 10);
    bamActive = false;
    bamPosition = null;
    winner = null;
    res.sendStatus(200);
});

app.post('/leftBAM', (req, res) => {
    bamActive = true;
    bamPosition = 0;
    setTimeout(() => {
        bamActive = false;
        bamPosition = null;
    }, 500);
    res.sendStatus(200);
});

app.post('/rightBAM', (req, res) => {
    bamActive = true;
    bamPosition = 15;
    setTimeout(() => {
        bamActive = false;
        bamPosition = null;
    }, 500);
    res.sendStatus(200);
});

app.post('/winnerL', (req, res) => {
    winner = 'Left player wins!';
    res.sendStatus(200);
});

app.post('/winnerR', (req, res) => {
    winner = 'Right player wins!';
    res.sendStatus(200);
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
```

### Step 3: Create the Front-End

Create a directory named `public` and inside it, create an `index.html` file:

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
            background-color: #f0f0f0;
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
            padding: 5px;
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
                document.getElementById('winner').innerText = data.winner;
                document.getElementById('winner').style.display = 'block';
                return;
            }

            if (data.bamActive) {
                document.getElementById(`bam-${data.bamPosition}`).style.display = 'flex';
            } else if (data.currentPosition !== null) {
                document.getElementById(`dot-${data.currentPosition}`).style.display = 'block';
            }
        }

        setInterval(updateDisplay, 100);
    </script>
</body>
</html>
```

### Step 4: Command Line Control

Create a control script named `control.js` to send commands to the server:

```javascript
const fetch = require('node-fetch');
const command = process.argv[2];
const param = process.argv[3];

const baseUrl = 'http://localhost:3000';

const sendCommand = async (endpoint) => {
    try {
        const response = await fetch(`${baseUrl}${endpoint}`, { method: 'POST' });
        if (response.ok) {
            console.log('Command sent successfully');
        } else {
            console.log('Failed to send command');
        }
    } catch (error) {
        console.error('Error:', error);
    }
};

(async () => {
    switch (command) {
        case 'start':
            await sendCommand('/pos/0');
            break;
        case 'pos':
            await sendCommand(`/pos/${param}`);
            break;
        case 'leftBAM':
            await sendCommand('/leftBAM');
            break;
        case 'rightBAM':
            await sendCommand('/rightBAM');
            break;
        case 'winnerL':
            await sendCommand('/winnerL');
            break;
        case 'winnerR':
            await sendCommand('/winnerR');
            break;
        default:
            console.log('Unknown command');
    }
})();
```

To run this, you will need to install the `node-fetch` package:

```sh
npm install node-fetch
```

### Step 5: Running the Server and Sending Commands

1. Start the server by running:
```sh
node server.js
```

2. Open a browser window and navigate to `http://localhost:3000`.

3. Use the control script to send commands. For example:
```sh
node control.js start
node control.js pos 5
node control.js leftBAM
node control.js winnerL
```

This setup will create a local browser-based server that can display a dot at one of 16 positions and respond to various commands.

----

the dots display in the same spot, how to fix this?

To fix the issue of the dots displaying in the same spot, you need to ensure that the dots are positioned correctly in a horizontal line. This can be done by using CSS to create a grid layout with 16 columns and placing each dot in its respective column.

Here's the corrected `index.html` and `server.js` files to ensure that the dots display in the correct positions:

### Corrected `index.html`

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
            background-color: #f0f0f0;
        }
        #container {
            display: grid;
            grid-template-columns: repeat(16, 40px);
            gap: 5px;
        }
        .dot, .bam {
            width: 40px;
            height: 40px;
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
            padding: 5px;
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
                document.getElementById('winner').innerText = data.winner;
                document.getElementById('winner').style.display = 'block';
                return;
            }

            if (data.bamActive) {
                document.getElementById(`bam-${data.bamPosition}`).style.display = 'flex';
            } else if (data.currentPosition !== null) {
                document.getElementById(`dot-${data.currentPosition}`).style.display = 'block';
            }
        }

        setInterval(updateDisplay, 100);
    </script>
</body>
</html>
```

### Corrected `server.js`

Make sure this file has no errors as shown previously.

```javascript
const express = require('express');
const app = express();
const port = 3000;

let currentPosition = null;
let bamActive = false;
let bamPosition = null;
let winner = null;

app.use(express.static('public'));

app.get('/status', (req, res) => {
    res.json({ currentPosition, bamActive, bamPosition, winner });
});

app.post('/pos/:position', (req, res) => {
    currentPosition = parseInt(req.params.position, 10);
    bamActive = false;
    bamPosition = null;
    winner = null;
    res.sendStatus(200);
});

app.post('/leftBAM', (req, res) => {
    bamActive = true;
    bamPosition = 0;
    setTimeout(() => {
        bamActive = false;
        bamPosition = null;
    }, 500);
    res.sendStatus(200);
});

app.post('/rightBAM', (req, res) => {
    bamActive = true;
    bamPosition = 15;
    setTimeout(() => {
        bamActive = false;
        bamPosition = null;
    }, 500);
    res.sendStatus(200);
});

app.post('/winnerL', (req, res) => {
    winner = 'Left player wins!';
    res.sendStatus(200);
});

app.post('/winnerR', (req, res) => {
    winner = 'Right player wins!';
    res.sendStatus(200);
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
```

### Running the Server and Sending Commands

1. **Start the server** by running:
    ```sh
    node server.js
    ```

2. **Open a browser window** and navigate to `http://localhost:3000`.

3. **Use the control script** to send commands. For example:
    ```sh
    node control.mjs start
    node control.mjs pos 5
    node control.mjs leftBAM
    node control.mjs winnerL
    ```

By ensuring that each dot is correctly placed in a grid layout and updating the display correctly based on the server's status, the dots should display at the correct positions.
