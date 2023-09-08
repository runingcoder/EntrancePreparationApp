# Entrance Preparation App

This is an entrance preparation app that has quiz functionality where students can attempt different question sets on IOE and IOM fields.
They can track their progress by creating their own account and see their progress in charts too.

## Technology used:
Python, Django, Javascript, HTML, CSS

## Instructions for installation:
1. Install PostgreSQL development library: `sudo apt-get install libpq-dev`
2. Make a python environment: `virtualenv myenv`
3. Activate the environment: `source myenv/bin/activate`
4. Install the requirements: `pip install -r requirements.txt`
5. Setup the pgadmin in your pc: [https://computingforgeeks.com/how-to-install-pgadmin-4-on-ubuntu/](https://computingforgeeks.com/how-to-install-pgadmin-4-on-ubuntu/)
6. Make a database and import the sql file.
67. Run the following commands:
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

## Demo screenshots!!

<img src = "images/mainPage.png" width = "800" height = '600'><br>
<img src = "images/quizConfirm.png" width = "800" height = '600'><br>
<img src = "images/quiz.png" width = "800" height = '600'><br>
<img src = "images/progress.png" width = "800" height = '600'><br>


## Credit
This project was completed as a part of Minor project of the curriculum of third year of the department of Electronics and Computer Engineering in Pulchowk Campus.
