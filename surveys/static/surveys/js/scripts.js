// Load feather buttons
$(document).ready(function () {
    feather.replace();

    var textBoxCounter = 1;

    $("#add-new-choice").click(function () {
        var oldTextBox = $("#id_choice_set-" + (textBoxCounter-1) + "-choice_text");
        var newTextBox = oldTextBox.clone();

        newTextBox.attr("name",     "choice_set-"   + textBoxCounter + "-choice_text");
        newTextBox.attr("id",       "id_choice_set-"+ textBoxCounter + "-choice_text");

        var newRowDiv = $("<div>").addClass('row').attr('id', "row_div_"+textBoxCounter).append(
            $("<div>").addClass('col-sm-2').text("Choice "+(textBoxCounter+1)),
            $("<div>").addClass('col-sm-6 form-group').attr('id', "col_div_"+textBoxCounter)
        );

        $("#answer-bois").append(newRowDiv);
        $("#col_div_"+textBoxCounter).append(newTextBox);
        $("#id_choice_set-TOTAL_FORMS").val(++textBoxCounter);
    });

    $("#delete-choice").click(function () {
        if (textBoxCounter>1) {
            textBoxCounter--;
        }
        $("#col_div_"+textBoxCounter).remove();
        $("#row_div_"+textBoxCounter).remove();
        $("#id_choice_set-TOTAL_FORMS").val(textBoxCounter);
    });


    $(".add-edit").click(function () {
        $("#id_choice_set-"+(textBoxCounter-1)+"-choice_text").val(textBoxCounter);
    });

    function redirect() {
        alert("what did you expect lmao");
    }




});

