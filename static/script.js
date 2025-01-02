document.addEventListener('DOMContentLoaded', function() {
    const startButton = document.getElementById('start-button');
    const statusDiv = document.getElementById('status');

    startButton.addEventListener('click', function() {
        fetch('/start')
            .then(response => response.json())
            .then(data => {
                statusDiv.innerText = data.status;
            })
            .catch(error => {
                console.error('Error:', error);
                statusDiv.innerText = 'An error occurred while starting the bot.';
            });
    });
});