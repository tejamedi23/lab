const fs = require('fs');
const filepath = "sample_file.txt";

fs.open(filepath, 'r+', (err, fd) => {
    if (err) return console.error('Error opening file:', err);

    fs.fstat(fd, (err, stats) => {
        if (err) {
            console.error('Error getting file stats:', err);
            return fs.close(fd, () => { });
        }

        const buffer = Buffer.alloc(stats.size);
        // READ FILE
        fs.read(fd, buffer, 0, stats.size, 0, (err, bytesRead) => {
            if (err) {
                console.error('Error reading file:', err);
                return fs.close(fd, () => { });
            } else {
                console.log('File content:\n', buffer.toString());
            }

            // NOW WRITE AFTER READING FINISHES
            const new_text = "\n This is the text you have written to the file";
            fs.write(fd, new_text, (err, data) => {
                if (err) {
                    console.error('Error writing to file:', err);
                    return fs.close(fd, () => { });
                } else {
                    console.log("The text written to the file is:", new_text);
                }

                // CLOSE FILE AFTER WRITING
                fs.close(fd, (err) => {
                    if (err) console.error('Error closing file:', err);
                    else console.log('File closed successfully.');
                });
            });
        });
    });
});
