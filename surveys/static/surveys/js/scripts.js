// Load feather buttons
$(document).ready(function () {
    feather.replace();

    // global tb counter
    var textBoxCounter = 1;

    // shows all choices in a question as the page loads
    $("#add-new-choice").ready(function () {
        var choices = $("#add-new-choice").attr("data-variable").slice(1,-1).split("', ");
        var str = "";

        while (choices.length >= textBoxCounter-1) {

            var oldTextBox = $("#id_choice_set-" + (textBoxCounter-1) + "-choice_text");
            var newTextBox = oldTextBox.clone();
            var choice = choices[textBoxCounter];
            str = choice;

            if (textBoxCounter == choices.length-1) {
                str = choice.slice(1,-1);
            }
            else{
                str = choice.substr(1);
            }

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

    // add more choices to a question
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

    // remove choices from a question
    $("#delete-choice").click(function () {
        if (textBoxCounter>1) {
            textBoxCounter--;
        }
        $("#col_div_"+textBoxCounter).remove();
        $("#row_div_"+textBoxCounter).remove();
        $("#id_choice_set-TOTAL_FORMS").val(textBoxCounter);
    });

    // adds default values as you add choices, this is on top of add-new-choice click
    $(".add-edit").click(function () {
        var choices = $("#add-new-choice").attr("data-variable").slice(1,-1).split("', ");
        var str = "";

        if (choices.length > textBoxCounter-1) {
            var choice = choices[textBoxCounter-1];

            if (choices.length == textBoxCounter) {
                str = choice.slice(1,-1);
            }
            else {
                str = choice.substr(1);
            }
        }

        $("#id_choice_set-"+(textBoxCounter-1)+"-choice_text").val(str);
    });

    $(".answer_question_choice").change(function () {
        if(this.checked) {
            $("#"+this.id).parent().attr('class', 'btn btn-success btn-block text-left');
        }

        else {
            $("#"+this.id).parent().attr('class', 'btn btn-secondary btn-block text-left');
        }
    });




    $(".select_me").select(function() {
        word_selection = $(this).selection();
        $.post( "word_context", { word_selection: word_selection } );
    });

    // just a helper function to test stuff
    function redirect() {
        alert("what did you expect lmao");
    }

});

// create_chart returns render of the chart
// used in the results.html
function create_chart(name, json_data) {
    FusionCharts.ready(function(){
        var chart = new FusionCharts({
            type: 'Column3D',
            width: '400',
            height: '200',
            dataFormat: 'json',
            renderAt: name,
            dataSource: json_data
        }).render();
    });
}