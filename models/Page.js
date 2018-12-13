const mongoose = require("mongoose");
const Schema = mongoose.Schema;

// create Schema
const ItemSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    date: {
        type: Date,
        default: Date.now
    }
});

module.exports = Page = mongoose.model("page",ItemSchema);
