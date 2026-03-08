//Variables declaration
const http = require('http');
const fs = require('fs');
const url = require('url');
const querystring = require('querystring');
const usersFile = 'users.txt';

//Creating the server
const server = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url, true);

    if (req.method === 'GET' && req.url === '/') {
        // Serve the login form
        fs.readFile('login.html', 'utf8', (err, data) => {
            if (err) {
                res.writeHead(500, { 'Content-Type': 'text/plain' });
                res.end('Error loading login page');
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(data);
            }
        });
    }
    // Reading password from file, user and validating it.
    else if (req.method === 'POST' && parsedUrl.pathname === '/login') {
        let body = '';
        // Keeping the request reading on to ensure the complete request is received.
        req.on('data', chunk => {
            body += chunk.toString();
        });

        req.on('end', () => {
            //Parsing the body object to get the query parameters
            const postData = querystring.parse(body);
            const { username, password } = postData;

            fs.readFile(usersFile, 'utf8', (err, data) => {
                if (err) {
                    res.writeHead(500, { 'Content-Type': 'text/plain' });
                    res.end('Error reading user data');
                    return;
                }
                const storedPassword = data.trim();

                if (password === storedPassword) {
                    res.writeHead(200, { 'Content-Type': 'text/plain' });
                    res.end('Welcome, ' + username + '!');
                } else {
                    // Reload login page with error message
                    fs.readFile('login.html', 'utf8', (err, pageData) => {
                        if (err) {
                            res.writeHead(500, { 'Content-Type': 'text/plain' });
                            res.end('Error loading login page');
                        } else {
                            res.writeHead(200, { 'Content-Type': 'text/html' });
                            const modifiedPage = pageData.replace('<p id="message"></p>',
                                '<p id="message" style="color:red;">Incorrect password. Please try again.</p>');
                            res.end(modifiedPage);
                        }
                    });
                }
            });
        });
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
    }
});

const port = 3001
server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
