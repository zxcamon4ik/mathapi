myUID := $(shell id -u)

# Note: Get env variables from .env file
#include .env

.PHONY: echo-i-uid
# Echo user id
echo-i-uid:
	@echo ${myUID}

.PHONY: d-homework-i-run
# Make all actions needed for run homework from zero.
d-homework-i-run:
	@make init-configs &&\
	make d-run

.PHONY: d-homework-i-purge
# Make all actions needed for purge homework related data.
d-homework-i-purge:
	@make d-purge


.PHONY: init-configs
# Configuration files initialization
init-configs:
	@cp .env.example .env &&\
	cp compose.override.dev.yaml compose.override.yaml


.PHONY: d-run
# Just run
d-run:
	@export myUID=${myUID} &&\
	COMPOSE_PROFILES=full_dev \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose up \
			--build



.PHONY: d-run-i-local-dev
# Just run services for local development. For example, Database, Redis, etc.
d-run-i-local-dev:
	@export myUID=${myUID} &&\
	COMPOSE_PROFILES=local_dev \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose \
			up --build \


.PHONY: d-purge
# Purge all data related with services
d-purge:
	@export myUID=${myUID} &&\
	COMPOSE_PROFILES=full_dev \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down --volumes --remove-orphans --rmi local --timeout 0


.PHONY: init-dev
# Init environment for development
init-dev:
	@make poetry-install && \
	pre-commit install

.PHONY: homework-i-run
# Run homework.
homework-i-run:
	@python main.py

.PHONY: homework-i-purge
homework-i-purge:
	@echo Goodbye


# [pre-commit]-[BEGIN]
.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files

.PHONY: pre-commit-autoupdate
# Update "rev" version of all pre-commit hooks.
pre-commit-autoupdate:
	@pre-commit autoupdate

# Pre-commit run for folder:
# https://pre-commit.com/#pre-commit-run:~:text=git%20ls%2Dfiles%20%2D%2D%20%27*.py%27%20%7C%20xargs%20pre%2Dcommit%20run%20%2D%2Dfiles
# git ls-files -- apps/users/ | xargs pre-commit run --files
# [pre-commit]-[END]


# [poetry]-[BEGIN]
.PHONY: poetry-up-pinned-latest
# Update all packages to the latest version allowed by the current constraints.
poetry-up-pinned-latest:
	@poetry up --pinned --latest

.PHONY: poetry-up-pinned-latest-no-install
# Update all packages to the latest version allowed by the current constraints.
poetry-up-pinned-latest-no-install:
	@poetry up --pinned --latest --no-install

.PHONY: poetry-lock
# Lock the current dependencies.
poetry-lock:
	@poetry lock

.PHONY: poetry-install
# Install the current dependencies.
poetry-install:
	@poetry install --no-root --sync


.PHONY: poetry-self-show-plugins
# Show plugins for poetry.
poetry-self-show-plugins:
	@poetry self show --plugins


.PHONY: poetry-export-requirements
# Export the current dependencies to requirements.txt.
poetry-export-requirements:
	@poetry export --format requirements.txt --output requirements.txt --without-hashes
# [poetry]-[END]

# [extra_python]-[BEGIN]
.PHONY: install-pipx
# Install pipx.
# Note: Reloading shell is needed after this action.
install-pipx:
	@python3.12 -m ensurepip &&\
	python3.12 -m pip install --upgrade pip &&\
	python3.12 -m pip install --user pipx &&\
	python3.12 -m pipx ensurepath

.PHONY: install-poetry
# Install poetry.
# Note: Reloading shell is needed after this action.
install-poetry:
	@pipx install poetry &&\
	pipx upgrade poetry &&\
	poetry self add poetry-plugin-export ;\
	poetry self add poetry-plugin-up

.PHONY: install-pre-commit
# Install pre-commit.
install-pre-commit:
	@pipx install pre-commit &&\
	pipx upgrade pre-commit

.PHONY: install-black
# Install black.
install-black:
	@pipx install black &&\
	pipx upgrade black

# [extra_python]-[END]


.PHONY: migrations
# Make migrations
migrations:
	@python manage.py makemigrations mathFX

.PHONY: migrate
# Migrate
migrate:
	@python manage.py migrate mathFX




.PHONY: django-init-db-data
# Generate data for db
django-init-db-data:
	@make django-init-animals



