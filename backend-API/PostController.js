const fs = require('fs')

const ParkingService = require('./ParkingService.js')
class ParkingController {
	async create(req, res) {
		try {
			const parking = req.body
			const parkingData = JSON.parse(fs.readFileSync('database.json'))
			parkingData.push(parking)
			fs.writeFileSync('database.json', JSON.stringify(parkingData))
			res.json(parkingData)
		} catch (e) {
			res.status(500).json({ error: e.message })
		}
	}

	async getAll(req, res) {
		try {
			const parkingData = JSON.parse(fs.readFileSync('database.json'))
			res.json(parkingData)
		} catch (e) {
			res.status(500).json({ error: e.message })
		}
	}

	async getOne(req, res) {
		try {
			const id = req.params.id
			const parkingData = JSON.parse(fs.readFileSync('database.json'))
			const parking = parkingData.find(p => p.owner_id === id)
			res.json(parking)
		} catch (e) {
			res.status(500).json({ error: e.message })
		}
	}

	async update(req, res) {
		try {
			const updatedParking = req.body
			const parkingData = JSON.parse(fs.readFileSync('database.json'))
			const parkingIndex = parkingData.findIndex(
				p => p.owner_id === updatedParking.owner_id
			)
			parkingData[parkingIndex] = updatedParking
			fs.writeFileSync('database.json', JSON.stringify(parkingData))
			res.json(parkingData)
		} catch (e) {
			res.status(500).json({ error: e.message })
		}
	}

	async delete(req, res) {
		try {
			const id = req.params.id
			const parkingData = JSON.parse(fs.readFileSync('database.json'))
			const parkingIndex = parkingData.findIndex(p => p.owner_id === id)
			const deletedParking = parkingData.splice(parkingIndex, 1)
			fs.writeFileSync('database.json', JSON.stringify(parkingData))
			res.json(deletedParking)
		} catch (e) {
			res.status(500).json({ error: e.message })
		}
	}
}

module.exports = ParkingController
