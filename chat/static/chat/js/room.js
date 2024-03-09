const chatLog = document.getElementById('chat-log')
const messageInput = document.getElementById('chat-message-input')
const submitBtn = document.getElementById('chat-message-submit')
const currentUserId = JSON.parse(document.getElementById('current-user-id').textContent)
const otherUserId = JSON.parse(document.getElementById('other-user-id').textContent)


const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + otherUserId + '/'
)


chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data)
    const message = data.message
    addMessageToLog(message)
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


submitBtn.onclick = function() {
    const message = messageInput.value.trim()
    if (message !== '') {
        chatSocket.send(JSON.stringify({
            'message': message
        }))
        messageInput.value = ''
    }
}


function addMessageToLog(content) {
    const messageDiv = document.createElement('div')
    messageDiv.classList.add('message')

    // const senderSpan = document.createElement('span')
    // senderSpan.classList.add('sender')
    // senderSpan.textContent = sender

    const contentSpan = document.createElement('span')
    contentSpan.classList.add('content')
    contentSpan.textContent = content

    // messageDiv.appendChild(senderSpan)
    messageDiv.appendChild(contentSpan)

    chatLog.appendChild(messageDiv)
    chatLog.scrollTop = chatLog.scrollHeight
}