# Vince Paino's CS_3380 Project
-- Fantasy Football Database --

This application is ran from the python3 package mysql:
https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html


Requirements to deploy this program:

Before starting, ensure you have the following installed:

Python or Python3 (Preferably the latest version),
pip (Python package installer),
MySQL Server and Workbench

### Setup Instructions:

Clone the repository:
git clone https://github.com/vincentpaino/Fantasy-Football-League
Navigate to the project directory:
(i.e. cd fantasy-football-database)
Set up a virtual environment (optional):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install all dependencies:
pip install mysql-connector-python
Set up the database by including your own connection (on your own local machine) to the MySQL Server:
Example code:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootpassword"
    )
    cursor = connection.cursor()

main() function is ran through app.py (python app.py)