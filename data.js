const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;

//database Connection
const {Client} = require('pg')
const  client = new Client({
	user: 'postgres',
	host: 'localhost',
	database: 'icstest',
	password: 'ubuntu',
	port: 5432,
})
client.connect((err) =>
{
	if (err) throw err;
	console.log("Connected!");

	// run the to retrieve data
	client.query("SELECT * FROM icstest.subABool", (error, results) => {
		if(error) throw error;
		// print everything in the table
		console.log(results.rows);
	})
});

//reading in the json file
const fs = require('fs');
const data = fs.readFileSync('num.json');
const num = JSON.parse(data);

app.use(cors());

// default endpoint
app.get('/', (req, res) => {
	const data = fs.readFileSync('num.json');
	const num = JSON.parse(data);
	res.send(num['num']);
});

app.listen(port, () => {
	console.log(`Example app listening at http://localhost:${port}`);
});
