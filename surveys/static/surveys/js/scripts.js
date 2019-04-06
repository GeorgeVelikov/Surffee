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
                else if (textBoxCounter <= choices.length-1){
                    str = choice.substr(1);
                }
                else {
                    break;
                }


                newTextBox.attr("name",     "choice_set-"   + textBoxCounter + "-choice_text");
                newTextBox.attr("id",       "id_choice_set-"+ textBoxCounter + "-choice_text");
                newTextBox.attr("required", '');
                newTextBox.val(str);

                let newRowDiv = $("<div>").addClass('row').attr('id', "row_div_"+textBoxCounter).append(
                    $("<div>").addClass('col-md-12 form-group').attr('id', "col_div_"+textBoxCounter).append(
                    $("<div>").addClass('input-group mb-3 fieldWrapper').attr('id', "wrap_div_"+textBoxCounter).append(
                    $("<div>").addClass('input-group-prepend').attr('id', "pre_div_"+textBoxCounter).append(
                    $("<span>").addClass('input-group-text').text("Choice "+(textBoxCounter+1)))))
                    );

                $("#answer-bois").append(newRowDiv);
                $("#wrap_div_"+textBoxCounter).append(newTextBox);
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
            $("<div>").addClass('col-md-12 form-group').attr('id', "col_div_"+textBoxCounter).append(
            $("<div>").addClass('input-group mb-3 fieldWrapper').attr('id', "wrap_div_"+textBoxCounter).append(
            $("<div>").addClass('input-group-prepend').attr('id', "pre_div_"+textBoxCounter).append(
            $("<span>").addClass('input-group-text').text("Choice "+(textBoxCounter+1)))))
            );


        $("#answer-bois").append(newRowDiv);
        $("#wrap_div_"+textBoxCounter).append(newTextBox);
        $("#id_choice_set-TOTAL_FORMS").val(++textBoxCounter);
    });

    // remove choices from a question
    $("#delete-choice").click(function () {
        if (textBoxCounter>1) {
            textBoxCounter--;
        }
        $("#row_div_"+textBoxCounter).remove();
        $("#id_choice_set-TOTAL_FORMS").val(textBoxCounter);
    });

    // adds default values as you add choices, this is on top of add-new-choice click
    $(".add-edit").click(function () {
        let choices = $("#add-new-choice").attr("data-variable").slice(1, -1).split("', ");
        let str = "";

        if (choices.length > textBoxCounter-1) {
            let choice = choices[textBoxCounter - 1];
            // it does not matter, they're both integers
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
        $(".answer_question_choice").each(function () {
            if(this.checked) {
                $("label[for*="+this.id+"]").attr('class', 'btn btn-success btn-block text-left');
            }

            else {
                $("label[for*="+this.id+"]").attr('class', 'btn btn-secondary btn-block text-left');
            }
        });
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

            $('#word_selection').val(word_selection);
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
    });


    $('.annotations').change(function() {
        var empty = true;
        // cleans all the listed classifications
        $(".classifications").children().remove().end();

        // save annot name, this is for testing really
        var annot_id = $(this).val()

        // create new option and add some text to it
        for(i in all_classifications) {
            var classif = all_classifications[i];

            if (classif.annotation_id == annot_id) {
                var option = new Option()
                $(option).html(classif.name);

                // append option to select
                $(".classifications").append(option);
                empty = false;
            }
        }
        if (empty) {
            var option = new Option()
            $(option).html("NO CLASSIFICATIONS EXIST FOR THIS ANNOTATION");
            $(".classifications").append(option);
        }
    });


    $(".annotation_id").each(function() {
        let input_field = $(($(this).children()[0]));
        console.log( input_field.val() );
    });


    $(".annotation_operation").click(function () {
        noerrors = true;
        let operation = this.id;
        let choice_id = $('#choice_id_post').val();
        let word_text = $('#word_selection').val();
        let class_name = $("#id_classification_name").val();

        if (class_name === "") {
            alert("You need to define the classification of the selection.");
            noerrors = false;
        }

        // if the element does not exist, it's created dynamically
        if (!word_text) {
            alert("You need to make a selection which to classify.");
            noerrors = false;
        }

        if (noerrors) {
            if (operation === "add_one" || operation === "add_all") {
                window.location.href = "./" + +
                                       annotation_id + '/' +
                                       operation + '/' +
                                       choice_id + '/' +
                                       class_name + '/' +
                                       word_text;
            }
            else {
                window.location.href = "./" +
                                       annotation_id + '/' +
                                       operation + '/' +
                                       choice_id + '/' +
                                       word_text;
            }
        }
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



function openTab(evt, tabid) {
    var i, tabcontent, tablinks;

    //hide active content first
    tabcontent = document.getElementsByClassName("tabc");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
        tabcontent[i].className = tabcontent[i].className.replace(" show", "");
        tabcontent[i].className = tabcontent[i].className.replace(" active", "");
    }
    //remove active classes from tabs
    tablinks = document.getElementById("nav-tab").getElementsByTagName("a");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
        tablinks[i].className = tablinks[i].className.replace(" show", "");

    }
    //add active to new tab
    evt.currentTarget.className += " active";

    //display block on new content
    document.getElementById(tabid).style.display = "block";
    document.getElementById(tabid).className += " active show";


}


