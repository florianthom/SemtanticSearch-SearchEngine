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

router.post("/:id", (req, res) => {

    id = req.params.id;
    client.invoke("write_articles_longer_read_than_4_s",
        req.params.id,
        function(error, reply, streaming) {});

    res.json(JSON.parse({}));
});


module.exports = router