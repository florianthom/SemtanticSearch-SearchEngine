const express = require('express')
const mongoose = require('mongoose')
const bodyParser = require('body-parser')
const pages = require("./routes/api/pages")
const tests = require("./routes/api/tests")
const searches = require("./routes/api/searches")



const app = express();

// Bodyparser Middleware
// Returns middleware that only parses json and only looks at requests where the Content-Type header matches the type option.
app.use(bodyParser.json());

// DB Config

const db = require("./config/keys").mongoURI;

// conncect to mongo
mongoose
    .connect(db, {useNewUrlParser: true})
    .then(() => console.log("MongoDB connected..."))
    .catch(err => console.log(err));

// Use routes
app.use("/api/pages", pages)
app.use("/api/tests", tests)
app.use("/api/searches", searches)


const port = process.env.PORT || 5000;

app.listen(port, () => console.log("Server started on port " + port));