//Author: Andrew Lancaster

$(document).ready(function(){

//    Validate fields on form submission
    $("button").on("click", function(e){
        if ($("#food_name1").val() && !$("#calories1").val() || !$("#quantity1").val()){
            e.preventDefault();
            error("Please fill out the required fields.");
            $("#food1").find("input").each(function(ev){
                if(!$(this).val()){
                    $(this).addClass("error");
                }
            });
        }else if(!$("#daily_calories").val()){
            e.preventDefault();
            error("Please tell us what your daily calorie goal is.");
            $("#daily_calories").addClass("error");
        }
    });

//    If user corrects empty input, remove error class
    $("input").change(function(){
        if($(this).hasClass("error")){
            $(this).removeClass("error");
        }
    });

//    Error output function
    var error = function(message){
        $("#error").html("Error: " + message).show();
    }
});