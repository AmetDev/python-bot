const fs = require('fs');
const ParkingController = require("./PostController.js");
const express = require('express');
const Router = express.Router;
let router = new Router();

router = require('express').Router();
router.post('/posts', async (req, res) => {
    try {
        const parking = req.body;
        const parkingData = JSON.parse(fs.readFileSync('database.json'));
        parkingData.push(parking);
        fs.writeFileSync('database.json', JSON.stringify(parkingData));
        res.json(parkingData);
    } catch (e) {
        res.status(500).json({ error: e.message });
    }
  });
router.get('/posts', async (req, res) => {
    try {
        const parkingData = JSON.parse(fs.readFileSync('database.json'));
        res.json(parkingData);
    } catch (e) {
        res.status(500).json({ error: e.message });
    }
  });
  router.get('/posts', async(req, res) => {
    try {
        const indexCity = req.query.index_city;
        const parkingData = JSON.parse(fs.readFileSync('database.json'));
        const filteredData = parkingData.filter(obj => obj.index_city === indexCity);
        res.json(filteredData);
    } catch (e) {
        res.status(500).json({ error: e.message });
    }
});




router.get('/posts/:id', async (req, res) => {
    try {
        const id = Number(req.params.id);

        const parkingData = JSON.parse(fs.readFileSync('database.json'));
        const parking = parkingData.find((p) => p.owner_id === id);
        res.json(parking);
    } catch (e) {
        res.status(500).json({ error: e.message });
    }
})
router.put('/posts',  async (req, res) => {
    try {
        const updatedParking = req.body;
        const parkingData = JSON.parse(fs.readFileSync('database.json'));
        const parkingIndex = parkingData.findIndex((p) => p.owner_id === updatedParking.owner_id);
        parkingData[parkingIndex] = updatedParking;
        fs.writeFileSync('database.json', JSON.stringify(parkingData));
        res.json(parkingData);
    } catch (e) {
        res.status(500).json({ error: e.message });
    }
})
router.put('/posts/:id', async (req, res) => {
    try {
        const id = Number(req.params.id);
        const updateData = req.body;

        const parkingData = JSON.parse(fs.readFileSync('database.json'));
        const parkingIndex = parkingData.findIndex((p) => p.owner_id === id);
        parkingData[parkingIndex].owner_number_parking_spaces = updateData.owner_number_parking_spaces;
        parkingData[parkingIndex].User_number_of_free_place_parking = updateData.User_number_of_free_place_parking;
        fs.writeFileSync('database.json', JSON.stringify(parkingData));

        res.json(parkingData[parkingIndex]);
    } catch (e) {
        res.status(500).json({ error: e.message });
    }
});

router.delete('/posts/:id', async (req, res) => {
    try {
        const id = req.params.id;
        const parkingData = JSON.parse(fs.readFileSync('database.json'));
        const parkingIndex = parkingData.findIndex((p) => p.owner_id === id);
        const deletedParking = parkingData.splice(parkingIndex, 1);
        fs.writeFileSync('database.json', JSON.stringify(parkingData));
        res.json(deletedParking);
    } catch (e) {
        res.status(500).json({ error: e.message });
    }
})

module.exports = router

//Hello world