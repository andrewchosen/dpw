//Author: Andrew Lancaster

$(document).ready(function(){

    $("button").on("click", function(e){
        if ($("#food_name1").val() && !$("#calories1").val() || !$("#quantity1").val()){
            e.preventDefault();
            $("form").prepend("<div id='error'>Error: Please fill out the required fields.");
            $("#food1").find("input").each(function(ev){
                if(!$(this).val()){
                    $(this).addClass("error");
                }
            });
        }
    });

    $("input").change(function(){
        if($(this).hasClass("error")){
            $(this).removeClass("error");
        }
    });

});