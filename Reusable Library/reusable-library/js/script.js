//Author: Andrew Lancaster

$(document).ready(function(){

    $("button").on("click", function(e){
        if ($("#food_name1").val() && !$("#calories1").val() || !$("#quantity1").val()){
            e.preventDefault();
            $("#error").html("Error: Please fill out the required fields.").show();
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