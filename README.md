# Antiragging-Cell-Website
The anti-ragging cell website serves as a crucial platform to promote a safe and welcoming campus environment by providing information, resources, and a confidential reporting system to address any instances of ragging and ensure the well-being of students.
## Technologies used
The following technologies were used to build this app:
- Flask for API and backend
- Jinja2 templates 
- Bootstrap
- SQLite for database

## Features
The app has the following features:

- Flask security and token based authentication
- Clear Reporting Mechanism: A user-friendly interface to report ragging incidents anonymously, ensuring confidentiality and encouraging students to come forward.
- Educational Content: Informative sections with articles, videos, and resources explaining the consequences of ragging, the legal framework, and its impact on victims and society.

- Anti-Ragging Policy: Displaying the institution's strict policy against ragging, along with the details of penalties for offenders and support for victims.
- Notifications via email to authorities

# Folder Structure

- `db_directory` has the sqlite DB. It can be anywhere on the machine. Adjust the path in ``application/config.py`. Repo ships with one required for testing.
- `application` is where our application code is
- `.gitignore` - ignore file
- `setup.sh` set up the virtualenv inside a local `.env` folder. Uses `pyproject.toml` and `poetry` to setup the project
- `local_run.sh`  Used to run the flask application in development mode
- `templates` - Default flask templates folder



