### Logs Analysis Project

This Udacity course project analyzes existing data from several SQL tables for a fake newspaper website in order to determine related information. This information includes which articles are the most popular, which authors are the most popular, and which days there was a higher than 1% error rate for for users trying to access the newspaper website. 

To effectively run the code for this project, you will need the Linux-based Virtual Machine as well as the newsdata.sql project data (instructions on how to access both are in the Udacity course). Start up your VM, cd into the correct directory, and run the code, like so. This will produce the results of the data analysis for this project.

`vagrant ssh
cd /vagrant
python3 LogsAnalysis.py`

**How It Works**
The code simply connects to the news database, then executes three separate SQL queries to answer each of the three questions the project asks for. The result of each query is formatted in Python for readability.

**Issues**
Using the code editor Sublime Text seemed to prevent me from breaking up my SQL queries using enter, but if it makes it more readable and your text editor allows for it, feel free to add enters into the SQL queries.