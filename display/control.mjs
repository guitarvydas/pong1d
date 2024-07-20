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
