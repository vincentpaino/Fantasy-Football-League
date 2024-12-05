Vince Paino's CS_3380 Project
-- Fantasy Football Database --

This application is ran from the python3 package mysql:
https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html


Requirements to deploy this program:

Before starting, ensure you have the following installed:

Python or Python3 (Preferably the latest version)
pip (Python package installer)

Setup Instructions:
Clone the repository to your local machine:
git clone https://github.comyour-usernamefantasy-football-database.git
Navigate to the project directory:
bash
Copy code
cd fantasy-football-database
Set up a virtual environment (recommended):
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install all dependencies:
bash
Copy code
pip install -r requirements.txt
Set up the database by running the setup script:
bash
Copy code
python setup_database.py
This will create an SQLite database where all fantasy football data (players, stats, etc.) will be stored.
















Python venv info:
"A virtual environment in Python is a self-contained directory with its own installation 
of Python and its own libraries. This isolation ensures that the dependencies you install 
for one project don’t interfere with other projects."

"After creating the environment, you’ll need to activate it to use the isolated interpreter and libraries."
Command: venv\Scripts\activate (Have to do this each time, you'll see (venv) \Users\... in the terminal)

Git help:

Before doing anything, always run
'git pull origin main'

To push code...
Always check 'git status'

if on main branch...
Do 'git add .' to add all the files 

Then 'git commit -m "__" '

Then 'git push origin main'


DB structure help:

fantasy_football_db/
├── app.py                # Main script: combines querying, initialization, and execution
├── db/
│   ├── __init__.py       # Optional, for package initialization
│   ├── connection.py     # Contains the database connection logic
│   ├── schema.py         # Handles database schema creation and initialization
├── utils.py              # Optional: Validation, data generation, helper functions
├── README.md             # Project overview
├── requirements.txt      # Dependencies
└── config.py             # Configuration (e.g., DB credentials)
In this setup:

app.py: Acts as the entry point, orchestrating the workflow by calling functions from connection.py or schema.py.
Database-related code is grouped in db/ but without excessive splitting.
Miscellaneous helpers go into utils.py.

Key Points for 3NF:
Primary Key Exists: The table must already satisfy 2NF.
No Transitive Dependencies: Non-key attributes cannot depend on other non-key attributes. They must depend only on the primary key.
Minimal Redundancy: Ensures that data is stored only where it belongs, reducing redundancy and improving integrity.


Instructions for students during the Zoom demo.

Step 1: Explain why your relation schemas are in 3NF (~1 min) 

Step 2: Demonstrate how you create the database/tables and populate the tables for your application (~1 mins) 

Step 3: Demonstrate your application’s first functionality (~2 mins)  

Step 4: Demonstrate your application’s second functionality (~2 mins) 

Step 5: Demonstrate your application’s third functionality (~2 mins) 