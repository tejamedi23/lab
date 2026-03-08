// Import MongoDB driver
const { MongoClient } = require("mongodb");

// Connection string (adjust if your MongoDB runs elsewhere)
const uri = "mongodb://localhost:27017";

async function run() {
    const client = new MongoClient(uri);

    try {
        // Connect to MongoDB
        await client.connect();
        console.log("Connected to MongoDB!");

        // Create or access a database
        const db = client.db("nodejspracticedb");

        // Create or access a collection
        const students = db.collection("students");

        // Insert documents
        await students.insertMany([
            { name: "Alice", grade: "A", marks: 90 },
            { name: "Bob", grade: "B", marks: 75 },
            { name: "Charlie", grade: "C", marks: 60 },
        ]);
        console.log("Documents inserted!");

        // Find all documents
        const allStudents = await students.find().toArray();
        console.log("All Students:", allStudents);

        // Find with condition
        const topStudents = await students.find({ grade: "A" }).toArray();
        console.log("Top Students:", topStudents);

        // Count documents
        const count = await students.countDocuments();
        console.log("Total Students:", count);

        // Sort documents by marks descending
        const sorted = await students.find().sort({ marks: -1 }).toArray();
        console.log("Sorted by Marks:", sorted);

        // Limit results
        const limited = await students.find().limit(2).toArray();
        console.log("Limited Results:", limited);

        // Skip results
        const skipped = await students.find().skip(1).toArray();
        console.log("Skipped First Document:", skipped);
    } finally {
        // Close connection
        await client.close();
    }
}

run().catch(console.dir);
