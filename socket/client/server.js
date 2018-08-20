const io = require('socket.io')();

io.on('connection', (client) => {
  client.on('chat message', msg => {
    console.log(msg);
    io.emit('message', msg);
  });
});

const port = 8000;
io.listen(port);
console.log('listening on port ', port);
