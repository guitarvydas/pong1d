import open from 'open';

const baseUrl = 'http://localhost:3000/index.html';
const dotIndex = process.argv[2];

if (dotIndex === undefined || isNaN(dotIndex) || dotIndex < 0 || dotIndex > 15) {
    console.error('Please provide a valid dot index (0-15)');
    process.exit(1);
}

const url = `${baseUrl}?dot=${dotIndex}`;

(async () => {
    // Opens the URL in the default browser
    await open(url);
    console.log(`Opened ${url}`);
})();
