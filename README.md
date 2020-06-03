# Team
A Django web task.which is using Python(3.5),Django(2.2) and Sqllite(DB.This project also contain a django custom command to insert dummy data into the db.

- Please read the full document:-

Technologies Used Python(3.5) Django(2.2) Sqllite3

Install

- pip install -r requirements.txt

Migrations

- python manage.py makemigrations
- python manage.py migrate

Commands :- run these below commands in same order as metnioned.

- python python manage.py team_dummy_data
- python python manage.py player_dummy_data
- python python manage.py player_history_dummy_data
- python python manage.py point_dummy_data


Steps To Follow by using some of above commands:-
  - First download the Python(3.5) along with pip in your system.
  - Install all requirement using this command "pip install –r requirement.txt".
  - Go into mytask folder where we have manage.py file.
  - Run command "python manage.py makemigrations" and "python manage.py migrate".
  - To insert dummy data in db run above mentioned command.
  - Now run python local server using "python manage.py runserver".
  - Hit this url in browser http://localhost:8000/team/ to get the data.
  
 Note:- To schedule the match fixture us admin panel.
 URL:- http://localhost:8000/admin/team/
 
 Step to add the data using admin panel to Match model.
  - open the url in browser.click on add , select the team from dropdown and Save to store data into the model.
 
 Flow:-
   - By following all the commands and migrations setup the project and add data into the models.
   - On home page will get the team names and macth scheduled (if data added from panel.)
   - By clicking on team name will get the list of the players respect to the team and after clicking on player will get the player history.
   - By clicking on match will get the point of the team.
