const { MongoClient } = require('mongodb');

// Connection URI
const uri = "mongodb://localhost:27017"; // Replace with your connection string

// Create a new MongoClient
const client = new MongoClient(uri);
let db = null


async function run() {
  try {
    // Connect to the MongoDB server
    await client.connect();
    console.log("Connected to MongoDB!");

    // Access a database
    db = client.db("testdb");


  } catch (err) {
    console.error(err);
  } finally {
    // Close the connection
    await client.close();
  }
}

run().catch(console.error);




class BaseModel{

    static collection

    static async get(id){
        return await this.collection.find({id : id}).toArray();
    }

    static async insert(data){
        this.collection.insert(data)
    }
}

class User extends BaseModel{

    static collection = db.collection('users')

    constructor({username, password = undefined}) {
        super()
        this.password = password;
        if(password){
            this.role = "admin";
        }else{
            this.role = 'user';
        }
        this.username = username;
        this.id = id;


        User.insert(this)
        
    }
}


class Quizz extends BaseModel{
    static collection = db.collection('quizzes')

    constructor({title, questions = []}){
        this.title = title;
        this.questions = questions;
    }
}

class Question extends BaseModel{
    static collection = db.collection('questions')

    constructor({question, answers = []}){
        this.question = question;
        this.answers = answers;
    }
}

module.exports = {
    User, Quizz, Question, db
}
