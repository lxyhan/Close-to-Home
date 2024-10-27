import { MongoClient } from 'mongodb';
import { promisify } from 'util'; // Add this line

const uri = process.env.MONGODB_URI;

if (!uri) {
  throw new Error('MongoDB connection string is missing in .env file');
}

const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

export async function connectToDatabase() {
  try {
    await client.connect();
    return client.db('myDatabase'); // Replace with your database name
  } catch (error) {
    console.error('Error connecting to MongoDB:', error);
    throw error;
  }
}
