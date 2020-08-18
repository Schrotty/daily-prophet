const express = require('express');
const fileUpload = require('express-fileupload');
const cors = require('cors');
const bodyParser = require('body-parser');
const morgan = require('morgan');
const fs = require('fs');

const app = express()

//serve dist directory
app.use(express.static("dist"))

//enable middleware for file upload
app.use(fileUpload({
    createParentPath: true
}))

//add other middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(morgan('dev'));

//start app
const port = process.env.PORT || 8080;
const file = './dist/index.json'

app.get('/media', function (request, response) {
    response.send(loadData())
})

fs.open(file, 'r', function (err) {
    if (err) fs.writeFile(file, "[]", function () {
        console.log('Created empty index.json')
    })
})

app.delete('/media', function (request, response) {
    try {
        if (!request.params) {
            response.send({
                status: false,
                message: 'No files were deleted!'
            })
        } else {
            const filename = request.body.id
            deleteFromData(filename, function () {
                fs.unlinkSync('./dist/storage/' + filename)
            })

            response.send({
                status: true,
                message: 'Delete complete!',
                data: {
                    name: filename,
                }
            })
        }
    } catch (e) {
        console.log(e)
        response.status(500).send(e)
    }
})

app.post('/upload', function(request, response) {
    try {
        if (!request.files) {
            response.send({
                status: false,
                message: 'No files were uploaded!'
            })
        } else {
            let media = request.files.media
            updateDataWith(media, function () {
                media.mv('./dist/storage/' + media.name)
            })

            response.send({
                status: true,
                message: 'Upload complete!',
                data: {
                    name: media.name,
                    mimeType: media.mimetype,
                    size: media.size
                }
            })
        }
    } catch (e) {
        console.log(e)
        response.status(500).send(e)
    }
});

app.put('/activate', function (request, response) {
    try {
        if (!request.body.id) {
            response.send({
                status: false,
                message: 'No file activated!'
            })
        } else {
            activateMedia(request.body.id, function () {
                return true
            })
        }
    } catch (e) {
        response.status(500).send(e)
    }
})

app.listen(port, () => {
    console.log(`DailyProphet listening at http://localhost:${port}`)
})

// FUNCTIONS
function activateMedia(filename, callback) {
    loadDataAsync(function (err, data) {
        if (err) {
            console.log(err)
            return
        }

        const index = JSON.parse(data)
        index.forEach(e => e.selected = e.filename === filename)

        fs.writeFile(file, JSON.stringify(index), 'utf8', callback)
    })
}

function deleteFromData(identifier, callback) {
    loadDataAsync(function (err, data) {
        if (err) {
            console.log(err)
            return
        }

        const index = JSON.parse(data);
        const filtered = index.filter(function (value) {
            return value.filename !== identifier
        })

        fs.writeFile(file, JSON.stringify(filtered), 'utf8', callback)
    })
}

function updateDataWith(item, callback) {
    loadDataAsync(function (err, data) {
        if (err) {
            console.log(err)
            return
        }

        const index = JSON.parse(data);
        index.push({
            filename: item.name,
            type: item.mimetype.split('/')[0],
            selected: !hasSelected()
        })

        fs.writeFile(file, JSON.stringify(index), 'utf8', callback)
    })
}

function hasSelected() {
    return getSelected().length >= 1
}

function getSelected() {
    return JSON.parse(loadData()).filter(function (value) {
        return value.selected === true
    })
}

function loadData() {
    return fs.readFileSync(file, 'utf8')
}

function loadDataAsync(callback) {
    return fs.readFile(file, 'utf8', callback)
}