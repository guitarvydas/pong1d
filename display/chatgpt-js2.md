```
How do I fix this error?
node control.js start 
/Users/paultarvydas/projects/pong1d/display/control.js:1
const fetch = require('node-fetch');
              ^

Error [ERR_REQUIRE_ESM]: require() of ES Module /Users/paultarvydas/projects/pong1d/display/node_modules/node-fetch/src/index.js from /Users/paultarvydas/projects/pong1d/display/control.js not supported.
Instead change the require of index.js in /Users/paultarvydas/projects/pong1d/display/control.js to a dynamic import() which is available in all CommonJS modules.
    at Object.<anonymous> (/Users/paultarvydas/projects/pong1d/display/control.js:1:15) {
  code: 'ERR_REQUIRE_ESM'
}

Node.js v21.7.3

```

The error indicates that `node-fetch` is now an ES module and should be imported using the `import` statement instead of `require`. To fix this, you can either convert your `control.js` file to an ES module or use a different HTTP client like `axios` that still supports CommonJS.

Here's how to fix it using the `import` statement:

1. **Convert `control.js` to an ES module:**

First, change the file extension of `control.js` to `.mjs` so Node.js recognizes it as an ES module. Rename `control.js` to `control.mjs`.

2. **Modify `control.mjs` to use `import` instead of `require`:**

```javascript
import fetch from 'node-fetch';

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

3. **Run `control.mjs` using Node.js:**

```sh
node control.mjs start
```

Alternatively, you can use `axios` to keep using CommonJS syntax:

1. **Install `axios`:**

```sh
npm install axios
```

2. **Modify `control.js` to use `axios` instead of `node-fetch`:**

```javascript
const axios = require('axios');

const command = process.argv[2];
const param = process.argv[3];

const baseUrl = 'http://localhost:3000';

const sendCommand = async (endpoint) => {
    try {
        const response = await axios.post(`${baseUrl}${endpoint}`);
        if (response.status === 200) {
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

3. **Run `control.js` using Node.js:**

```sh
node control.js start
```

Choose either method based on your preference and the structure of your project.
