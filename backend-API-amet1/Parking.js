const fs = require('fs');

let rawdata = fs.readFileSync('database.json');
let Parking = JSON.parse(rawdata);
module.exports = Parking
//