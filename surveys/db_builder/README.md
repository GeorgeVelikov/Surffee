# DB_Builder
This part of the program is meant to automate the process of building surveys for testing and display.
Each directory in here contains files the DB_Builder will read to create surveys.

# How to run
(Might change later)
Go to django shell and run following commands
>\>>>from surveys.db_builder.DB_Builder import Build  
>\>>>Build()

# File syntax
Records in \[...] are optional  
Records in \{...} are name of files from specified directory  
(e.g. \{choice> means that this record must contain a name of a file in choice/ directory)
1. users
    > username ; password ; email address ; \[superuser]
1. surveys
    > creator ; survey name ; {descriptions} ; active/inactive ; {pi_choices} ; {questions} ; \[number of respondents]
1. questions
    > question text ; type of question(S/M) ; {choices}
1. descriptions
    > the content of this file will be the description of the survey
1. pi_choices
    > each line contains one of the personal information choices to be added
1. choices
    > each line contains one of the choices to be added