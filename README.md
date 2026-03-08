# Full Stack Development Lab Programs

This repository contains all 8 lab programs listed exactly in the order of the questions. Unnecessary programs have been removed to avoid confusion.

## Execution Guide & Expected Outputs

### 1. A simple Calculator using HTML, CSS and JavaScript
- **File:** `1_calculator.html`
- **How to run:** Just double-click `1_calculator.html` to open it in any web browser (Chrome, Edge, Firefox).
- **Expected Output:** You will see a styled calculator with a coral border and rounded buttons. You can click the numbers and operators to perform basic math (e.g., `5 + 5 = 10` or `10 / 2 = 5`). The result appears inside the display box and next to "Result:".

### 2. Demonstration of events (onmouseover, onmouseout) on html page
- **File:** `2_events.html`
- **How to run:** Double-click `2_events.html` to open it in a browser.
- **Expected Output:** The page displays a paragraph saying "This is working great !". Initially, the text is blue. When you hover your mouse over it (`onmouseover`), the text changes to **red** and *italic*. When you move the mouse away (`onmouseout`), it reverts to blue.

### 3. HTML and JavaScript program to remove html elements with clicks
- **File:** `3_remove_elements.html`
- **How to run:** Double-click `3_remove_elements.html` to open it in a browser.
- **Expected Output:** You will see three colored boxes (grey, lightgreen, and lightpink) containing text. When you click *anywhere* inside a box, that entire box will instantly disappear from the page.

### 4. Create a Node JS application for User login system
- **Folder:** `4_user_login`
- **How to run:** 
  1. Open terminal and go into the folder: `cd 4_user_login`
  2. Start the server: `node server.js`
  3. Open your browser and go to: `http://localhost:3001`
- **Expected Output:**
  - You will see a Login form asking for a Username and Password.
  - The correct password (stored in `users.txt`) is `p@ssw0rd`.
  - **Success:** Entering any username with the password `p@ssw0rd` shows: "Welcome, [Username]!"
  - **Failure:** Entering a wrong password shows: "Incorrect password. Please try again." in red text.

### 5. Write a Node JS program to perform read, write and other operations on a file
- **Folder:** `5_fs_operations`
- **How to run:** 
  1. Open terminal and go into the folder: `cd 5_fs_operations`
  2. Run the script: `node fs_module_operations.js`
- **Expected Output:**
  - The script will read `sample_file.txt` and print its contents to the terminal ("This is the text to read from file.").
  - It will then write new text ("This is the text you have written to the file") to the file and log "File closed successfully." in the terminal.

### 6. Program to demonstrate Node JS File(fs) module by opening, writing and closing the file
- **Folder:** `6_fs_write`
- **How to run:**
  1. Open terminal and go into the folder: `cd 6_fs_write`
  2. Run the script: `node fs_write.js`
- **Expected Output:**
  - The script will silently write "Hello, this is a sample text..." into `output.txt`.
  - The terminal will display: "File written successfully." followed by "File closed successfully."
  - If you open `output.txt`, you will see the inserted text.

### 7. Write a Node JS program to read form data from query string and generate response using Node JS
- **Folder:** `7_form_query`
- **How to run:**
  1. Open terminal and go into the folder: `cd 7_form_query`
  2. Start the server: `node server.js`
  3. Open your browser and go to: `http://localhost:3000`
- **Expected Output:**
  - The browser shows a "User Registration Form" with Username, Password, check boxes for Skills (C, C++, Java, Python), radio buttons for Gender, and a Location dropdown.
  - After filling it out and clicking Submit, you are redirected to `/submit?username=...`. 
  - The page will display the extracted form data nicely formatted, e.g., "Username: bob", "Skills: Java, Python", etc.

### 8. MONGODB Commands
- **Folder:** `8_mongodb`
- **Requirements:** You must have a MongoDB server running locally (e.g., `mongod`) on port `27017`. Do `npm install mongodb` if you haven't already.
- **How to run:**
  1. Open terminal and go into the folder: `cd 8_mongodb`
  2. Run any of the three scripts:
     - `node basic_commands.js`
     - `node crud_operations.js`
     - `node count_limit_sort.js`
- **Expected Output:**
  - The terminal will connect to the `nodejspracticedb` database, perform the operations (Insert, Find, Update, Delete, Count, Sort), and log the retrieved documents and success messages directly to the terminal.
