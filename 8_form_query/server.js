const http = require('http');
const fs = require('fs');
const url = require('url');

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        //Serve the HTML file
        fs.readFile('index.html', (err, data) => {
            if (err) {
                res.writeHead(500, { 'Content-Type': 'text/plain' });
                res.end('Error loading index.html');
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(data);
            }
        });
    } else if (req.url.startsWith('/submit')) {
        //Process form submission
        const queryParams = url.parse(req.url, true).query;
        const username = queryParams.username || 'N/A';
        const password = queryParams.password || 'N/A'; // In real cases, never print passwords
        const skills = queryParams.skills ? Array.isArray(queryParams.skills) ?
            queryParams.skills.join(', ') : queryParams.skills : 'None';
        const gender = queryParams.gender || 'Not specified';
        const location = queryParams.location || 'Not specified';

        const responseHTML = `
        <html>
        <head><title>Form Submission</title></head>
        <body>
            <h2>Submitted Data</h2>
            <p><strong>Username:</strong> ${username}</p>
            <p><strong>Password:</strong> ${password}</p>
            <p><strong>Skills:</strong> ${skills}</p>
            <p><strong>Gender:</strong> ${gender}</p>
            <p><strong>Location:</strong> ${location}</p>
            <a href="/">Go Back</a>
        </body>
        </html>
        `;
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(responseHTML);
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 Not Found');
    }
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});
