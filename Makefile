checkconfig:
	docker-compose -f local.yml config

build:
	docker-compose -f local.yml up --build -d --remove-orphans

checklogs:
	docker-compose -f local.yml logs

checkvol_postgres:
	docker volume inspect swifty_authors_local_postgres_data

checkvol_backups:
	docker volume inspect swifty_authors_local_postgres_data_backups

checkvol_media:
	docker volume inspect swifty_authors_media_volume

checkvol_static:
	docker volume inspect swifty_authors_static_volume

up:
	docker-compose -f local.yml up -d

restart:
	docker-compose -f local.yml restart

pip:
	docker-compose -f local.yml run --rm api pip install -r requirements/local.txt

migrate:
	docker-compose -f local.yml run --rm api python3 manage.py migrate

makemigrations:
	docker-compose -f local.yml run --rm api python3 manage.py makemigrations

collectstatic:
	docker-compose -f local.yml run --rm api python3 manage.py collectstatic --no-input --clear

backup:
	docker-compose -f local.yml exec postgres backup

superuser:
	docker-compose -f local.yml run --rm api python3 manage.py createsuperuser

down:
	docker-compose -f local.yml down

down-v:
	docker-compose -f local.yml down -v

authors_db:
	docker-compose -f local.yml exec postgres psql --username=authors_user --dbname=authors_db

flake8:
	docker-compose -f local.yml exec api flake8 .

black-check:
	docker-compose -f local.yml exec api black --check --exclude=migrations .

black-diff:
	docker-compose -f local.yml exec api black --diff --exclude=migrations .

black:
	docker-compose -f local.yml exec api black --exclude=migrations .

isort-check:
	docker-compose -f local.yml exec api isort . --check-only --skip venv --skip migrations

isort-diff:
	docker-compose -f local.yml exec api isort . --diff --skip venv --skip migrations

isort:
	docker-compose -f local.yml exec api isort . --skip venv --skip migrations

generatekey:
	python -c 'import secrets; print(secrets.token_urlsafe(38))'
