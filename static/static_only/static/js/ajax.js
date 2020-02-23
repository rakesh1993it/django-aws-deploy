$(function(){

 $(document).on('click', '.search_result_close a', function(){
//$('.search_result_close a').on("click",function(e) {
       $('.search_result').remove();
     //  alert(1);

});


    $('#search').keyup(function() {
    
        $.ajax({
            type: "POST",
            url: "/artimages/search/",
            data: { 
                'search_text' : $('#search').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
        
    });

});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}