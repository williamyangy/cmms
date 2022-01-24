# textbookdb
Textbook database

Using Django 3.0 and Django-Rest-Framework.

Bootstrap Admin template.

## Setup
- Create virtual environment
> virtualenv venv
- Activate virtual environment
> source venv/bin/activate
- Install requirements
> pip3 install -r requirements.txt
- Start web server
> python3 manage.py runserver

Sever is available at http://localhost:8000

## Import data
All data files are located under bms/management/init_data folder. To import some data run command
> python3 manage.py seed --mode course_discipline

Other modes can be found in the bms/management/commands/seed.py file.
