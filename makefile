run:
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

restartdb:
	dropdb rent_hotel_db
	createdb rent_hotel_db
	python3 manage.py createsuperuser

