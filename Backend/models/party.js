const mongoose = require("mongoose");

const PartyShema = mongoose.Schema({
    owner: { type: String, required: true},
    content: { type: Object, required: true},
    moyenne: { type: Number, required: true},
    first: { type: Object, required: true},
});

const Party = mongoose.model("partysave", PartyShema);

module.exports = Party;
