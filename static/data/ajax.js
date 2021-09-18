$('#id').click(function(){
    $.ajax(
        url:'/pic/',
        type:'post',
        data:{
            '#'
        },
        success: function(data){
            console.log(data)
            $('#id').val(data)
        }
    )
});