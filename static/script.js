$(document).ready(function() {
    $('#start-button').click(function() {
        $('#status').text('Starting...');
        $.post('/start', function(data) {
            $('#status').text('Process started!');
        }).fail(function() {
            $('#status').text('Failed to start the process.');
        });

        // Open a connection to the /stream endpoint to receive logs
        const eventSource = new EventSource('/stream');

        eventSource.onmessage = function(event) {
            $('#log').append(event.data + '<br>');  // Append each new log line to the log div
            $('#log').scrollTop($('#log')[0].scrollHeight);  // Scroll to the bottom to see the latest log
        };

        eventSource.onerror = function() {
            $('#status').text('Failed to receive updates.');
        };
    });
});
