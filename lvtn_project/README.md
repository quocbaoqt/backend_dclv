### install venv ###
virtualenv venv

### active venv ####
.\venv\Scripts\activate

### install requirements ###
pip install -r requirements.txt

### CREATE DB USER ###
psql -U postgres -c "CREATE ROLE lvtn_user LOGIN NOSUPERUSER INHERIT CREATEDB CREATEROLE;"

### CREATE DB ###
Win+R -> cmd -> psql -U postgres -> CREATE DATABASE lvtn_db WITH OWNER "lvtn_user";

### migrations ###
python manage.py makemigrations 

!!! IF NO CHANGE DETECTED -> python manage.py makemigrations apartment (tương tự cho user và common_models....) 

### migrate ###
python manage.py migrate

### create super user ###
python manage.py createsuperuser

### RUN SERVER ###
python manage.py runserver


