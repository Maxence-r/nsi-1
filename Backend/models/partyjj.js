const mongoose = require("mongoose");

const PartyjjShema = mongoose.Schema({
    owner: { type: String, required: true},
    word: { type: String, required: true},
    try: { type: Number, required: true},
});

const Partyjj = mongoose.model("partyjjsave", PartyjjShema);

module.exports = Partyjj;