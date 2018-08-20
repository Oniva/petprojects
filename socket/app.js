
var express = require('express')
  , routes = require('./routes')
  , http = require('http');

var app = express();
app.set('port', process.env.PORT || 8080);
var server = http.createServer(app);
var io = require('socket.io').listen(server);

io.on('connection', (client) => {
  client.on('chat message', msg => {
    console.log(msg);
    io.emit('message', msg);
  });
});
// app.use(express.static("public"));
app.use(express.static('client/build'));
routes.get('/');

server.listen(8000);


module.exports = app;