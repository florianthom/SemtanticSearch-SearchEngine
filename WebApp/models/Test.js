const mongoose = require("mongoose");
const Schema = mongoose.Schema;

// create Schema
const TestSchema = new Schema({
    date: {
        type: String,
        default: Date.now
    },
    name: {
        type: String,
        required: true
    }
});

module.exports = Test = mongoose.model("crawlerdb2",TestSchema);
