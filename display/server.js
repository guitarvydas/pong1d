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
