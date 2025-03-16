const express = require('express')
const http = require('http')
const { Server } = require('socket.io')
const { User } = require('./models.js')

app = express()
PORT = 3000




const server = http.createServer(app);

// Attach Socket.IO to the HTTP server
const io = new Server(server);


// Create a new user
app.post('/users', (req, res) => {
    const {username, password} = req.body

    user = new User({
        username, password
    })

    res.json({

        detail : "User created successfully"
    })
})

// Login
app.post('/login', (req, res) => {
    const {username, password} = req.body

    user = User.get({username})
    if(user.verify(password)){
        token = jwt.sign({user})
    }

    res.json({
        token : token
    })
})

// Start the server
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});