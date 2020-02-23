$('.rateit').bind('click', function(e) {

    e.preventDefault();

    var ri = $(this);
    var value = ri.rateit('value');
    var object_id = ri.data('article_id');

    $.ajax({
        url: '/artimages/rate/?xhr',
        data: {
            object_id: article_id,
            value: value
        },
        type: 'post',
            success: function(data, response) {
            console.log("ajax call succeeded!");
        },
            error: function(data, response) {
            console.log("ajax call failed!");
        }
    });
});