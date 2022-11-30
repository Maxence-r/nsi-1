const express = require('express');
const router = express.Router();
const Party = require('../models/party');
const Partyjj = require('../models/partyjj');

router.get('/', (req, res) => {
    res.render('index');
});

router.get('/hp', (req, res) => {
    Party.find().limit(4).sort({$natural:-1}) 
    .then(party => res.json(party))
    .catch(error => res.status(400).json({ error }));
});

router.get('/jj', (req, res) => {
    Partyjj.find().limit(4).sort({$natural:-1})
    .then(partyjj => res.json(partyjj))
    .catch(error => res.status(400).json({ error }));
});

router.post('/auth/hp', (req, res) => {
    const party = new Party({
        owner: req.body.owner,
        content: req.body.content,
        moyenne: req.body.moyenne,
        first: req.body.first
    });
    party.save()
    .then(lien => res.status(201).json(lien._id))
    .catch(error => res.status(400).json({ error }));
});

router.get('/auth/:id', (req, res) => {
    Party.findOne({ _id: req.params.id })
    .then(party => res.json(party))
    .catch(error => res.status(400).json({ erreur: 'Aucun résultat' }));
});

router.post('/jj', (req, res) => {
    const partyjj = new Partyjj({
        owner: req.body.owner,
        word: req.body.word,
        try: req.body.try
    });
    partyjj.save()
    .then(lien => res.status(201).json(lien._id))
    .catch(error => res.status(400).json({ error }));
});



module.exports = router;