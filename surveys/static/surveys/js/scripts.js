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
                $("label[for*="+this.id+"]").attr('class', 'btn btn-success btn-block');
            }

            else {
                $("label[for*="+this.id+"]").attr('class', 'btn btn-secondary btn-block');
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


    $('.annotation_name').keyup(function () {
        var match = false;

        for (annot in all_annotations) {
                annot_name = all_annotations[annot].name
                if (annot_name == $(this).val()) {
                    match = true;
                }
            }

        if ($(this).val().length == 0 || match) {
            $("#new").attr("disabled", "");
        }
        else {
            $("#new").removeAttr("disabled");
        }
    });

    $('.annotations').change(function() {
        var empty = true;
        // cleans all the listed classifications
        $(".classifications").children().remove().end();

        // save annot name, this is for testing really
        var annot_id = $(this).val()

        $("#delete").removeAttr("disabled");
        $("#select").removeAttr("disabled");
        $("#select").val(annot_id.replace("./", ""));

        // create new option and add some text to it
        for(i in all_classifications) {
            var classif = all_classifications[i];
            if (classif.annotation_id == annot_id.replace("./", "")) {
                var option = new Option()
                $(option).html(classif.name);
                $(option).attr("disabled", "");
                $(option).addClass("list-group-item");
                // append option to select
                $(".classifications").append(option);
                empty = false;
            }
        }
        if (empty) {
            var option = new Option()
            $(".classifications").css("background-color", "red");
            $(option).css("font-size", 24);
            $(option).css("color", "white");
            $(option).attr("disabled", "");
            $(option).html("NO CLASSIFICATIONS EXIST");
            $(".classifications").append(option);
        }
        else {
            $(".classifications").css("background-color", "white");
        }

        $(".annotation_manager_operation").each(function () {
            this.value = annot_id;
        });
    });



    $(".annotation_id").each(function() {
        let input_field = $(($(this).children()[0]));
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



    // analyse generator page
    $("#survey_select_list").change(function() {
        $("#annotation_select_list").children().remove().end();
        var survey_id = $(this).val();

        var option = new Option()
        $(option).html("Please select an annotation from the ones used in the survey");
        $(option).addClass("list-group-item");
        $(option).attr("selected", "");
        $(option).attr("disabled", "");
        $(option).attr("hidden", "");
        $("#annotation_select_list").append(option);

        // wow set of arrays does not actually work, js is wonderful
        var annot_set = new Set();
        var used_indexes = new Array();
        for (let annotuple of all_annotations_analysis[survey_id]) {
            if (jQuery.inArray(annotuple[0], used_indexes) ==-1) {
                used_indexes.push(annotuple[0]);
                annot_set.add(annotuple);
            }

        }

        $("#annotation_select_list").removeAttr("disabled");
        for(let annot_tuple of annot_set.values()) {
            var option = new Option()
            $(option).html(annot_tuple[1]);
            $(option).addClass("list-group-item");
            $(option).attr("value", annot_tuple[0]);
            $("#annotation_select_list").append(option);
        }

        enableAnalysisCreateButton();
    });

    $("#id_analysis_name").keyup(function() {
        enableAnalysisCreateButton();
    });

    $(".analysis_option").change(function () {
        $(".analysis_option").each(function () {
            $(this).find('input').attr('checked', false);
        });

        $(this).find('input').attr('checked', true);
        enableAnalysisCreateButton();
    });

    function enableAnalysisCreateButton() {
        var analysisName = $("#id_analysis_name");

        var hasSurvey = $("#survey_select_list").val();
        var hasAnnotation = $("#annotation_select_list").val();
        var hasName = $("#id_analysis_name").val().length > 0;
        var hasAnalysisType;

        $(".analysis_option").each(function () {
            if ($(this).find('input').attr('checked')) {
                hasAnalysisType = true;
            }
        });

        if (hasName && hasSurvey && hasAnnotation && hasAnalysisType) {
            $("#create_analysis_button").removeAttr("disabled");
        }
    }

    if ($(".single_term_table").length) {
        /*
        for (let word of single_analysis_words) {
            console.log(word.fields);
        }

        for (let choice of single_analysis_choices) {
            console.log(choice);
        }

        for (let answer of single_analysis_answers) {
            console.log(answer.fields);
        }

        for (let classif of single_analysis_classifications) {
            console.log(classif);
        }
        */
    }

    var terms_added = []
    $("#addterm").on('click', function (){
        var class_id = $("#addtermform");

        if (class_id.val() == null) {

            alert("Please select a classification");
        }

        else {
            var opt = $(':selected', class_id);
            $(opt).css("background-color", "lightgreen")

            if (!terms_added.includes(class_id)) {
                $("#termtables").children().remove().end();
                terms_added.push(class_id.val());
                updateAnalysis(terms_added, constraints_added);

            }
            else {
                // alert("Classification already added");
            }
        }
    });

    $("#addconstraint").on('click', function (){
        var constraint = $("#addconform");

        if (constraint.val() == null) {

            alert("Please select a constraint");
        }

        else {
            //constraints_added
            var opt = $(':selected', constraint);
            $(opt).css("background-color", "lightgreen")
            key = opt.parent().attr('id');

            if (!constraints_added[key].includes(constraint.val())) {
                $("#termtables").children().remove().end();
                constraints_added[key].push(constraint.val());

                updateAnalysis(terms_added, constraints_added);
            }

            else {
                // alert("Constraint already added");
            }
        }
    });

});

function updateAnalysis(terms_added, constraints_added){
    var check = "#termtables #insidecontainer";
    if (!$(check).length) {
        var term_table = $("#termtables");
        var inside_container = $('<div id="insidecontainer" class="container-fluid"></div>');

        var data_row = $('<div class="row"></div>');

        $(inside_container).appendTo(term_table);
        $(data_row).appendTo(inside_container);

        var term_string = "";
        if (terms_added.length) {
            for (let term of terms_added) {
                for (let classif of single_analysis_classifications) {
                    if (term == classif.pk)
                    term_string += classif.fields.name + ", "
                }
            }
            term_string = term_string.slice(0,-2);
        }

        if (term_string === "") {
            term_string = "None";
        }

        var term_string_box = $('<div class="col-6"> <h4 id="term_string_list">Constraints: </h4> <div>' + term_string + '</div> </div>')
        term_string_box.appendTo(data_row);

        // shows which constraints are given
        var constraint_string = "";
        if(constraints_added) {
            for (key in constraints_added) {
                if (constraints_added[key].length) {
                    constraint_string += key + ": (";
                    for(let val of constraints_added[key]) {
                        constraint_string += val + ", ";
                    }
                    constraint_string = constraint_string.slice(0,-2) + ");<br>"
                }
            }
            constraint_string = constraint_string.slice(0,-5);
        }

        if (constraint_string === "") {
            constraint_string = "None";
        }

        var constraint_box = $('<div class="col-6"> <h4 id="constraint_list">Constraints: </h4> <div>' + constraint_string + '</div> </div>')
        constraint_box.appendTo(data_row);
    }

    for(let class_id of terms_added) {


        // words of the selected classification in the choices
        var words_in_choices = {}
        for(let word of single_analysis_words) {

            if (word.fields.text in words_in_choices && word.fields.classification == class_id) {
                words_in_choices[word.fields.text].push(word.fields.choice);
            }

            if (!(word.fields.text in words_in_choices) && word.fields.classification == class_id) {
                words_in_choices[word.fields.text] = [word.fields.choice];
            }
        }

        // blue bar
        var row_div = $('<br><div class="row bg-info" > </div>');
        $(row_div).appendTo($("#insidecontainer"));
        $('<div class="col-3"> # </div>').appendTo(row_div);

        for(word in words_in_choices) {
            $('<div class="col-3">' + word + '</div>').appendTo(row_div);
        }

        // answers shown under a blue bar
        var i = 0;
        for (let answer of single_analysis_answers) {
            var row = $('<div id="' + answer.pk + '" class="row"> </div>');

            if(i & 1 == 1) { // if number is even
                $(row).css("background-color", "lightgray");
            }

            $('<div class="col-3">' + (i+1) + '</div>').appendTo(row);
            i=i+1;
            for(word in words_in_choices) {
                var choices = words_in_choices[word];
                var user_votes = choices.filter(element => answer.fields.choice.includes(element));
                var ratio = user_votes.length / single_analysis_questions.length;

                $('<div class="col-3">' + ratio.toFixed(2) + '</div>').appendTo(row);
            }
            $(row).appendTo($("#insidecontainer"));

        }
    }
}


// just a helper function to test stuff
function redirect() {

        alert("what did you expect lmao");
    }

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
