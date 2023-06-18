document.getElementById("message-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting and refreshing the page

    var messageInput = document.getElementById("message-input").value; // Get the user input

    var xhr = new XMLHttpRequest();
    var url = "http://localhost:5000/send-message"; // Replace with your Flask server URL

    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            document.getElementById("output").innerText = response.output; // Display the output
        }
    };

    var data = JSON.stringify({ message: messageInput });
    xhr.send(data);
});
