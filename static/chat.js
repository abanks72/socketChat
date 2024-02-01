document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    let username = prompt("Please enter your username:", "User");

    socket.on('connect', () => {
        document.querySelector('#sendButton').onclick = () => {
            const message = document.querySelector('#messageInput').value;
            socket.emit('my event', {username: username, message: message});
        };
    });

    socket.on('my response', data => {
        if(data.username && data.message) {
            const p = document.createElement('p');
            p.innerHTML = `<strong>${data.username}:</strong> ${data.message}`;
            document.querySelector('#messages').append(p);
        }
    });
});
