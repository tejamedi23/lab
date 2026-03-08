const { MongoClient } = require("mongodb");

async function run() {
    const uri = "mongodb://localhost:27017"; // connection string
    const client = new MongoClient(uri);

    try {
        await client.connect();
        const db = client.db("nodejspracticedb");
        const collection = db.collection("students");

        // COUNT documents
        const count = await collection.countDocuments();
        console.log("Total students:", count);

        // LIMIT results (only first 3)
        const limited = await collection.find().limit(3).toArray();
        console.log("Limited results:", limited);

        // SORT results (by marks descending)
        const sorted = await collection.find().sort({ marks: -1 }).toArray();
        console.log("Sorted results:", sorted);

        // SKIP results (skip first 2, then show next ones)
        const skipped = await collection.find().skip(2).toArray();
        console.log("Skipped results:", skipped);

    } catch (err) {
        console.error(err);
    } finally {
        await client.close();
    }
}

run().catch(console.dir);
