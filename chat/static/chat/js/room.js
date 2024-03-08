const textarea = document.getElementById('chat-log')
const messageInput = document.getElementById('chat-message-input')
const submitBtn = document.getElementById('chat-message-submit')


const roomName = JSON.parse(document.getElementById('room-name').textContent)

const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
)


chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data)
    textarea.value += (data.message + '\n')
}


chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly')
}


messageInput.focus()
messageInput.onkeyup = function(e) {
    if (e.keyCode === 13) {
        submitBtn.click()
    }
}


submitBtn.onclick = function(e) {
    const message = messageInput.value
    chatSocket.send(JSON.stringify({
        'message': message
    }))

    messageInput.value = ''
}