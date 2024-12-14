const express = require('express');
const http = require('http');
const socketIo = require('socket.io');


const app = express();
const server = http.createServer(app);
const io = socketIo(server)


app.get('/', (req, res) => {
    res.sendFile(__dirname + '/main.html');
})

io.on('connection', (socket) => {
    console.log('User connected!');
    
    socket.on('chat message', (msg) => {
        io.emit('chat message', msg)
    });

    socket.on('disconnect', () => {
        console.log('User disconnected!')
    })
});

server.listen(3000, () => {
    console.log('Listening on *:3000');
})

