// Load feather buttons
$(document).ready(function () {
    feather.replace();

    var textBoxCounter = 1;

    $("#add-new-choice").click(function () {
        var oldTextBox = $("#id_choice_set-"+(textBoxCounter-1)+"-choice_text");
        var newTextBox = oldTextBox.clone();
        newTextBox.attr("name","choice_set-"+textBoxCounter + "-choice_text");
        newTextBox.attr("id","id_choice_set-"+textBoxCounter + "-choice_text");
        var newRowDiv = "<div class='row' id='row_div_"+textBoxCounter+"'></div>";
        $("#answer-bois").append(newRowDiv);

        $("#row_div_"+textBoxCounter).append(newTextBox);
        $("#id_choice_set-TOTAL_FORMS").val(++textBoxCounter);
    });

    $("#delete-choice").click(function () {
       textBoxCounter--;
       $("#row_div_"+textBoxCounter).remove();
       $("#id_choice_set-TOTAL_FORMS").val(textBoxCounter);
    });

    function redirect() {
        alert("what did you expect lmao");
    }




});

