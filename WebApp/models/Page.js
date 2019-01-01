const mongoose = require("mongoose");
const Schema = mongoose.Schema;

// create Schema
const PageSchema = new Schema({
    date: {
        type: String,
        required: true
    },
    title: {
        type: String,
        required: true
    },
    location: {
        type: String,
        required: true
    },
    text: {
        type: String,
        required: true
    },
    number: {
        type: [String],
        required: true
    }
});
var collectionName = 'crawlerdb'

module.exports = Page = mongoose.model("page",PageSchema,collectionName);
