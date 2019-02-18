// Load feather buttons
$(document).ready(function () {
    feather.replace();

    var textBoxCounter = 1;

    $("#add-new-choice").ready(function () {
        var choices = $("#add-new-choice").attr("data-variable").slice(1,-1).split(', ');
        var str = "";

        while (choices.length >= textBoxCounter-1) {

            var oldTextBox = $("#id_choice_set-" + (textBoxCounter-1) + "-choice_text");
            var newTextBox = oldTextBox.clone();
            var choice = choices[textBoxCounter];
            str = choice.slice(1,-1);

            newTextBox.attr("name",     "choice_set-"   + textBoxCounter + "-choice_text");
            newTextBox.attr("id",       "id_choice_set-"+ textBoxCounter + "-choice_text");
            newTextBox.attr("required", '');
            newTextBox.val(str);

            var newRowDiv = $("<div>").addClass('row').attr('id', "row_div_"+textBoxCounter).append(
                            $("<div>").addClass('col-sm-2').text("Choice "+(textBoxCounter+1)),
                            $("<div>").addClass('col-sm-6 form-group').attr('id', "col_div_"+textBoxCounter)
            );

            $("#answer-bois").append(newRowDiv);
            $("#col_div_"+textBoxCounter).append(newTextBox);
            $("#id_choice_set-TOTAL_FORMS").val(++textBoxCounter);
        }
    });

    $("#add-new-choice").click(function () {
        var oldTextBox = $("#id_choice_set-" + (textBoxCounter-1) + "-choice_text");
        var newTextBox = oldTextBox.clone();

        newTextBox.attr("name",     "choice_set-"   + textBoxCounter + "-choice_text");
        newTextBox.attr("id",       "id_choice_set-"+ textBoxCounter + "-choice_text");
        newTextBox.attr("required", '');
        newTextBox.val("");

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
        var choices = $("#add-new-choice").attr("data-variable").slice(1,-1).split(', ');
        var str = "";

        if (choices.length > textBoxCounter-1) {
            var choice = choices[textBoxCounter-1];
            str = choice.slice(1,-1);
        }

        $("#id_choice_set-"+(textBoxCounter-1)+"-choice_text").val(str);
    });

    function redirect() {
        alert("what did you expect lmao");
    }

});

