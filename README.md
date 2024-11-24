Vince Paino's CS_3380 Project
-- Fantasy Football Database --

This application is ran from the python3 package mysql:
https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html












Python venv info:
"A virtual environment in Python is a self-contained directory with its own installation 
of Python and its own libraries. This isolation ensures that the dependencies you install 
for one project don’t interfere with other projects."

"After creating the environment, you’ll need to activate it to use the isolated interpreter and libraries."
Command: venv\Scripts\activate

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

