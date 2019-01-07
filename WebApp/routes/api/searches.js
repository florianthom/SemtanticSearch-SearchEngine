const express = require("express");
const router = express.Router();
var zerorpc = require("zerorpc");

//calls the method on the python object
// client.invoke("methodname", "firstpara", "secondspara...", classback - function)
client = new zerorpc.Client();
client.connect("tcp://127.0.0.1:4242");


// Searches Model
//const Test = require("../../models/Test")

// @route   GET api/searches -> warum - wir haben doch get("/") -> unser Router ist in indexserver.js so
//                              definiert, dass nur "/api/pages" hier ankommt
// @desc    Retrieve Search-Results
// @access  Public
router.get("/", (req, res) => { ///:dateFROM/:dateTO
    console.log("in backend")
    console.log(req.query.searchString);
    console.log(req.query.dateFROM);
    console.log(req.query.dateTO);

    
    client.invoke("get_results",
        req.query.searchString,
        req.query.dateFROM,
        req.query.dateTO,
        function(error, reply, streaming) {
            res.json(JSON.parse(reply));
    });


});


module.exports = router