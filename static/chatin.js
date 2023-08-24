 // Your JavaScript code for interacting with the chat
 function sendMessage() {
    var inputElement = document.getElementById('messageInput');
    //Aqui esta el mensaje
    var message = inputElement.value.trim();
    // Call the backend Python code to get the response
    // For simplicity, let's assume we are using a variable "response" here
    
    inputElement.value = '';

    
    //Ruta
    fetch('http://127.0.0.1:5000/repetir', {
        method: 'POST',
        headers: {
            //Tipo de informacion enviada . . .
            'Content-Type': 'application/json'
        },
        // Informacion que se envia, stringify convierte lo que se escriban en Json
        body: JSON.stringify({"msg" : message})
    })
    //
    .then(response => response.json())
    .then(data => {
        // Manejar la respuesta del servidor
        var msg = data.msg;

        var chatBox = document.getElementById('chatBox');
        var messageElement = document.createElement('div');
        messageElement.textContent = "Tu: " + message;
        chatBox.appendChild(messageElement);
        var responseElement = document.createElement('div');
        responseElement.textContent = msg;
        chatBox.appendChild(responseElement);
    })
    .catch(error => {
        console.error('Error al realizar la petición POST:', error);
    });
}

// Victor Rodriguez 

