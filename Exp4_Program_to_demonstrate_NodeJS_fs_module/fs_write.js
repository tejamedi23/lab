const fs = require("fs");
const filePath = "output.txt";
const fileContent = "Hello, this is a sample text, written explicitly using open, write and close functions.";

// Open the file for writing
fs.open(filePath, "w", (err, fd) => {
    if (err) {
        console.error("Error opening file:", err);
        return;
    }

    // Write to the file
    fs.write(fd, fileContent, (err, written, string) => {
        if (err) {
            console.error("Error writing to file:", err);
        } else {
            console.log("File written successfully.");
            console.log("The content is: \n", written, string);
        }
    });

    //Close the file after writing
    fs.close(fd, (err) => {
        if (err) {
            console.error("Error closing file:", err);
        } else {
            console.log("File closed successfully");
        }
    });
});
