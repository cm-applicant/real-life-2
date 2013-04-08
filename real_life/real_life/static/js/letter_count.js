$(function (){
    $('#content').on('keyup', function (evt) {
        var len = $(this).val().length,
            span = $('#content_length');
        
        if (len === 0) {
            span.hide();
            return;
        }
        
        span.show();
        span.text('Letter count: ' + len);
    });
});