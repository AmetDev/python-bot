class ParkingService {
	async create(parking) {
		const createdParking = await Parking.create(parking)
		return createdParking
	}

	async getAll() {
		const parkings = await Parking.find()
		return parkings
	}
	async getOne(id) {
		if (!id) {
			throw new Error('не указан ID')
		}
		const parking = await Parking.findById(id)
		return parking
	}

	async update(parking) {
		if (!parking._id) {
			throw new Error('не указан ID')
		}
		const updatedParking = await Parking.findByIdAndUpdate(
			parking._id,
			parking,
			{ new: true }
		)
		return updatedParking
	}

	async delete(id) {
		if (!id) {
			throw new Error('не указан ID')
		}
		const parking = await Parking.findByIdAndDelete(id)
		return parking
	}
}

module.exports = ParkingService
