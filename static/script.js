$(document).ready(function() {
    $('#start-button').click(function() {
        $('#status').text('Starting...');
        $.post('/start', function(data) {
            $('#status').text('Process started!');
        }).fail(function() {
            $('#status').text('Failed to start the process.');
        });
    });
});