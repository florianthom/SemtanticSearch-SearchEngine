const express = require("express");
const router = express.Router();

// Pages Model
const Page = require("../../models/Page")

// @route   GET api/pages -> warum - wir haben doch get("/") -> unser Router ist in indexserver.js so
//                              definiert, dass nur "/api/pages" hier ankommt
// @desc    Get all Pages
// @access  Public
router.get("/", (req, res) => {
    Page
        .find()
        .exec(function(err, docs){
            docs = docs.map(function(doc) {
                var date_string = doc['date'];
                var tokenList = date_string.split(".")
                var date = new Date(tokenList[2], tokenList[1], tokenList[0])
                return doc['date'] = date;
            });
            if(err){
                res.json(err)
            } else {
                //docs.sort();
                res.json(docs)
            }
        })

});

// @route   POST api/pages
// @desc    Create a Post
// @access  Public
router.post("/", (req, res) => {
    var date = new Date();
    const newPage = new Page({
        date:  date.getDay().toString() + "." + (date.getMonth() + 1).toString() + "." + date.getFullYear().toString(),
        title: req.body.title,
        location: req.body.location,
        text:  req.body.text,
        number: req.body.number
    });
    newPage.save().then(item => res.json(item));
});

module.exports = router