const express = require('express')
const mongoose = require('mongoose')
const bodyParser = require('body-parser')


const app = express();

// Bodyparser Middleware
// Returns middleware that only parses json and only looks at requests where the Content-Type header matches the type option.
app.use(bodyParser.json());

// DB Config

const db = require("./config/keys").mongoURI;

// conncect to mongo
mongoose
    .connect(db, {useNewUrlParser: true})
    .then(() => console.log("MongoDB Connected..."))
    .catch(err => console.log(err));

const port = process.env.PORT || 5000;

app.listen(port, () => console.log("Server started on port " + port));