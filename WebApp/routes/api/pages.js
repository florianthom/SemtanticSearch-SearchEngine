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
        .limit(30)
        .then(pages => res.json(pages))

});

// @route   GET api/pages -> warum - wir haben doch get("/") -> unser Router ist in indexserver.js so
//                              definiert, dass nur "/api/pages" hier ankommt
// @desc    Get all Pages
// @access  Public
router.get("/:id", (req, res) => {
    console.log("id:");
    console.log(req.params.id);
    Page
        .findById(req.params.id)
        .then(pages => {
            console.log("pages");
            res.json(pages);
        })

});

// @route   POST api/pages
// @desc    Create a Post
// @access  Public
router.post("/", (req, res) => {
    var date = new Date();
    const newPage = new Page({
        date:  (date.getDay()-1).toString() + "." + (date.getMonth() + 1).toString() + "." + date.getFullYear().toString(),
        title: req.body.title,
        location: req.body.location,
        text:  req.body.text,
        number: req.body.number
    });
    newPage.save().then(item => res.json(item));
});

// @route   DELETE api/pages
// @desc    Delete a Post
// @access  Public
router.delete("/:id", (req, res) => {
   Page.findById(req.params.id)
    .then(page => page.remove().then(() => res.json({success: true})))
    .catch(err => res.status(404).json({success: false}))
});

module.exports = router