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

    if (data.message) {
        const senderId = data.sender_id
        const message = data.message
        const timestamp = data.timestamp.substring(11, 16)

        addMessageToLog(senderId, message, timestamp)
    } else if (data.previous_messages){
        const previousMessages = data.previous_messages

        previousMessages.forEach(messageData => {
            const senderId = messageData.sender_id
            const message = messageData.message
            const timestamp = messageData.timestamp.substring(11, 16)

            addMessageToLog(senderId, message, timestamp)
        })
    }
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
    }
    messageInput.value = ''
}


function addMessageToLog(senderId, content, timestamp) {
    const messageDiv = document.createElement('div')
    messageDiv.classList.add('message')
    if (senderId === currentUserId) {
        messageDiv.classList.add('sent')
    } else {
        messageDiv.classList.add('received')
    }

    const contentSpan = document.createElement('span')
    contentSpan.classList.add('content')
    contentSpan.textContent = content

    const timeSpan = document.createElement('span')
    timeSpan.classList.add('time-span')
    timeSpan.textContent = timestamp

    messageDiv.appendChild(contentSpan)
    messageDiv.appendChild(timeSpan)

    chatLog.appendChild(messageDiv)
    chatLog.scrollTop = chatLog.scrollHeight
}