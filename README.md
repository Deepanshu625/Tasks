# Tasks
Steps to run the project
* clone the project from git to your local system using this command
  ```
  git clone https://github.com/Deepanshu625/Tasks.git
  ```
* Open project in terminal and go to the folder /read_excel/props/ by and install the requiremenent file.
  ```
  cd Tasks/
  pip install -Ur requirements.txt
  ```
  
  * create a superuser
  ```
   python manage.py createsuperuser
  ```
  
 * Run the django app
  ```
  python manage.py runserver
  ```
  
* Now, start your browser and open this link

  ```
  http://127.0.0.1:8000/admin/
  ```
* Add few users

API details:
  * get all todo,  http://127.0.0.1:8000/todoall?user=admin
  * get single todo,  http://127.0.0.1:8000/todo?user=admin&id=1
  * post new todo,  http://127.0.0.1:8000/todo?user=admin&title=<>&details=<>&bookmark=True
  * update old todo,  http://127.0.0.1:8000/todo?id=1&user=admin&title=<>&details=<>&bookmark=True
  * delete a todo, http://127.0.0.1:8000/todo?user=admin&id=1
  
  
