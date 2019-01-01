const express = require("express");
const router = express.Router();

// Pages Model
const Test = require("../../models/Test")

// @route   GET api/pages -> warum - wir haben doch get("/") -> unser Router ist in indexserver.js so
//                              definiert, dass nur "/api/pages" hier ankommt
// @desc    Get all Pages
// @access  Public
router.get("/", (req, res) => {
    console.log("hallo")
    Test.find()
        .then(tests => res.json(tests));
});



// @route   POST api/pages
// @desc    Create a Post
// @access  Public
router.post("/", (req, res) => {
    console.log("newTest.name")

    const newTest = new Test({
        name: req.body.name
    });
    newTest.save().then(test => res.json(test));
});

module.exports = router