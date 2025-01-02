$(document).ready(function() {
    $('#start-button').click(function() {
        $('#status').text('Starting...');
        $.post('/start', function(data) {
            $('#status').text('Process started!');
        }).fail(function() {
            $('#status').text('Failed to start the process.');
        });

        const eventSource = new EventSource('/stream');
        eventSource.onmessage = function(event) {
            $('#log').append(event.data + '<br>');
            $('#log').scrollTop($('#log')[0].scrollHeight);
        };

        setInterval(function() {
            $.get('/logs', function(data) {
                $('#log').html(data.logs.replace(/\n/g, '<br>'));
            });
        }, 5000);

        eventSource.onerror = function() {
            $('#status').text('Failed to receive updates.');
        };
    });
});
