const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

// POST endpoint to handle orders
app.post('/order', (req, res) => {
    const { order } = req.body; // Extract selected order

    const orderConfirmation = `
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Order Confirmation</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                padding: 20px;
                background-color: #f9f9f9;
            }
            h1 {
                color: #4CAF50;
            }
            .confirmation {
                padding: 15px;
                border: 1px solid #ddd;
                background-color: #fff;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <h1>Order Confirmation</h1>
        <div class="confirmation">
            <p>Your selected order is: <strong>${order}</strong>.</p>
            <a href="/">Go back to Menu</a>
        </div>
    </body>
    </html>
    `;
    res.send(orderConfirmation);
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
