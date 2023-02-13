const express = require('express');
const fileUpload = require('express-fileupload')


const PORT = 9098;

const app = express()
const routes = require('./router');

app.use(express.json())
app.use(express.static('static'))
app.use(fileUpload({}))
app.use('/', routes);
async function startApp() {
    try {

        app.listen(PORT, () => console.log('SERVER STARTED ON PORT ' + PORT))
    } catch (e) {
        console.log(e)
    }
}

startApp()
