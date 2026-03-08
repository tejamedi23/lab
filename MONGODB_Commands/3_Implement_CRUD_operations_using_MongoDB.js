const { MongoClient } = require("mongodb");

// Connection string (adjust if needed)
const uri = "mongodb://localhost:27017";

async function run() {
    const client = new MongoClient(uri);
    try {
        await client.connect();
        console.log("Connected to MongoDB!");

        // Database and Collection
        const db = client.db("nodejspracticedb");
        const students = db.collection("students");

        // --- CREATE ---
        await students.insertMany([
            { name: "Alice", grade: "A", marks: 90 },
            { name: "Bob", grade: "B", marks: 75 },
            { name: "Charlie", grade: "C", marks: 60 }
        ]);
        console.log("Documents inserted!");

        // --- READ ---
        const allStudents = await students.find().toArray();
        console.log("All Students:", allStudents);

        const topStudents = await students.find({ grade: "A" }).toArray();
        console.log("Top Students:", topStudents);

        // --- UPDATE ---
        await students.updateOne(
            { name: "Bob" },
            { $set: { grade: "A", marks: 85 } }
        );
        console.log("Updated Bob’s record!");

        const updatedBob = await students.findOne({ name: "Bob" });
        console.log("Bob after update:", updatedBob);

        // --- DELETE ---
        await students.deleteOne({ name: "Charlie" });
        console.log("Deleted Charlie’s record!");

        const remaining = await students.find().toArray();
        console.log("Remaining Students:", remaining);

    } catch (err) {
        console.error(err);
    } finally {
        await client.close();
    }
}

run().catch(console.dir);
