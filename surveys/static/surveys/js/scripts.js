// Load feather buttons
$(document).ready(function () {
    feather.replace();

    // global tb counter
    let textBoxCounter = 1;


    // check if the element exists first
    if ($("#add-new-choice").length) {
        // shows all choices in a question as the page loads
        $(this).ready(function () {
            let choices = $("#add-new-choice").attr("data-variable").slice(1, -1).split("', ");
            let str = "";

            while (choices.length >= textBoxCounter-1) {

                let oldTextBox = $("#id_choice_set-" + (textBoxCounter - 1) + "-choice_text");
                let newTextBox = oldTextBox.clone();
                let choice = choices[textBoxCounter];
                str = choice;

                if (textBoxCounter === choices.length-1) {
                    str = choice.slice(1,-1);
                }
                else{
                    str = choice.substr(1);
                }

                newTextBox.attr("name",     "choice_set-"   + textBoxCounter + "-choice_text");
                newTextBox.attr("id",       "id_choice_set-"+ textBoxCounter + "-choice_text");
                newTextBox.attr("required", '');
                newTextBox.val(str);

                let newRowDiv = $("<div>").addClass('row').attr('id', "row_div_" + textBoxCounter).append(
                    $("<div>").addClass('col-sm-2').text("Choice " + (textBoxCounter + 1)),
                    $("<div>").addClass('col-sm-6 form-group').attr('id', "col_div_" + textBoxCounter)
                );

                $("#answer-bois").append(newRowDiv);
                $("#col_div_"+textBoxCounter).append(newTextBox);
                $("#id_choice_set-TOTAL_FORMS").val(++textBoxCounter);
            }
        });
    }
    // add more choices to a question
    $("#add-new-choice").click(function () {
        let oldTextBox = $("#id_choice_set-" + (textBoxCounter - 1) + "-choice_text");
        let newTextBox = oldTextBox.clone();

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
        let choices = $("#add-new-choice").attr("data-variable").slice(1, -1).split("', ");
        let str = "";

        if (choices.length > textBoxCounter-1) {
            let choice = choices[textBoxCounter - 1];

            if (choices.length === textBoxCounter) {
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

    // doing this instead of .post as I wanted to package the data in the form post data
    $(".select_me").select(function() {
            // grab the highlighted text on the select_me inputs
        let word_selection = $(this).selection();
        let parent_element = $($(this).parent());
        let choice_id = parent_element.attr('id');

        // removes the help text if we make a selection
        if ($('#annotation_help').length ) {
            $('#annotation_help').remove();
        }

        // if we have a caching field, just update val in it; else if we don't, create an input field and populate it
        if ($('#word_selection').length ) {

            $(this).val(word_selection);
        }
        else {
            let input = $("<input>").attr("name", "word_selection")
                                    .attr("id", "word_selection")
                                    .attr("readonly", "")
                                    .attr("class", "textinput textInput form-control")
                                    .val(word_selection);
            $('#selection').append($(input));
        }

        // same as word_selection, only used for choice ID
        if ($('#choice_id_post').length ) {

            $('#choice_id_post').val(choice_id);
        }
        else {
            let input = $("<input>").attr("name", "choice_id_selected")
                                    .attr("id", "choice_id_post")
                                    .attr("readonly", "")
                                    .attr("hidden", "")
                                    .attr("class", "textinput textInput form-control")
                                    .val(choice_id);
            $('#selection').append($(input));
        }
        highlight($(this));
        updateAnnotationOperationHref();
    });

    $(".annotation_id").each(function() {
        let input_field = $(($(this).children()[0]));
        console.log( input_field.val() );
    });

    $("#id_classification_name").on('input', updateAnnotationOperationHref);

    function updateAnnotationOperationHref() {
        $(".annotation_operation").each(function() {
            let operation = $(this).attr('id');
            let choice_id = $('#choice_id_post').val();
            let word_text = $('#word_selection').val();
            let class_name = $("#id_classification_name").val();

            $(this).attr('href', './' +
                          annotation_id + '/' +
                          operation + '/' +
                          choice_id + '/' +
                          class_name + '/' +
                          word_text);
        });
    }

    // just a helper function to test stuff
    function redirect() {
        alert("what did you expect lmao");
    }

});

// create_chart returns render of the chart
// used in the results.html
function create_chart(name, json_data) {
    FusionCharts.ready(function(){
        let chart = new FusionCharts({
            type: 'Column3D',
            width: '500',
            height: '300',
            dataFormat: 'json',
            renderAt: name,
            dataSource: json_data
        }).render();
    });
}