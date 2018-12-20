### Logs Analysis Project

This Udacity course project analyzes existing data from several SQL tables for a fake newspaper website in order to determine related information. This information includes which articles are the most popular, which authors are the most popular, and which days there was a higher than 1% error rate for for users trying to access the newspaper website. 

### How It Works

The code simply connects to the news database, then executes three separate SQL queries to answer each of the three questions the project asks for. The result of each query is formatted in Python for readability. 

This project uses a python file that connects to the NEWS database and runs a unique query.  The results are printed in Command Prompt.

### Prerequisites

In order for the files in this repository to work, you will need a terminal, such as Git Bash, a virtual machine, the News database that is provided in the course, and Python 3.

### Installing

GitBash can be downloaded and installed from the [GitBash website](https://git-for-windows.github.io/).

The virtual machine can be accessed using [Virtual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and [Vagrant](https://www.vagrantup.com/downloads.html).

Once the virtual machine has been successfully installed, the News database can then be accessed.  The .sql file which contains the database can be downloaded [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).  Ensure that the extracted files are placed in the shared vagrant directory.

If you do not have Python 3.6 installed on your computer, the most recent version can be downloaded from the [Downloads page on the Python Software Foundation website](https://www.python.org/downloads/).

Once these steps have been completed, the repository should be downloaded and saved in the shared vagrant directory.

### Running the Files

The first thing that needs to be done is loading the data into the virtual machine.  To do that, first start up the virtual machine using **vagrant up**, and log into the virtual machine using **vagrant ssh**.  After logging in, cd into the **/vagrant** shared directory and enter the command **psql -d news -f newsdata.sql**.  After the data has been loaded the queries can be run successfully using the **python3** command for the LogsAnalysis.py script.  The results of each query will print in the prompt.
