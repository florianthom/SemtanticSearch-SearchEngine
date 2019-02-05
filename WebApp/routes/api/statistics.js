const express = require("express");
const router = express.Router();

var storage = {abcd: 1234};

router.get("/", (req, res) => {
    console.log("in backend statistics")
    client.invoke("get_searched_words",
        function(error, reply, streaming) {
            res.json(JSON.parse(reply));
    });
});


module.exports = router