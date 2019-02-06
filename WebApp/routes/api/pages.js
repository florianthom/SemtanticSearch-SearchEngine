const express = require("express");
const router = express.Router();

// why do i store the information here (local)? Better for testing
// Better solution build new collection in mongo with id of the page as id.
//  under each id store a list of userOnPage-Times
var storageForTimeOnPage = {};

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
    Page
        .findById(req.params.id)
        .then(pages => {
            //pages.timeOnPage = storageForTimeOnPage[pages._id] == undefined ? [] : storageForTimeOnPage[pages._id];
             // ... = spread operator to copy pages attributes to a new obj
             // why ._doc? because under this attr, the document attr are stored (idk maybe a mongoose thing)
            result = {...pages._doc, timeOnPage: storageForTimeOnPage[pages._id] == undefined ? [] : (function () {
                            arr = storageForTimeOnPage[pages._id];
                            sum = arr.reduce(function(a, b) { return a + b; });
                            avg = (sum / arr.length).toFixed(1)
                            return [avg];
                        })()};
                        

                
            res.json(result);
        });

});



router.post("/:id", (req, res) => {

    id = req.params.id;
    if(storageForTimeOnPage.hasOwnProperty(id))
    {
        storageForTimeOnPage[id].push(req.body.time); // time in ms
    }
    else
    {
        storageForTimeOnPage[id] = [req.body.time]; // time in ms
    }
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