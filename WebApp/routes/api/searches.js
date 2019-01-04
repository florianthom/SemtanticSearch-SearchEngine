const express = require("express");
const router = express.Router();

// Searches Model
//const Test = require("../../models/Test")

// @route   GET api/searches -> warum - wir haben doch get("/") -> unser Router ist in indexserver.js so
//                              definiert, dass nur "/api/pages" hier ankommt
// @desc    Retrieve Search-Results
// @access  Public
router.get("/:id", (req, res) => {
    console.log(req.params.id)




    //Test.find()
        //.then(tests => res.json(tests));






});


module.exports = router