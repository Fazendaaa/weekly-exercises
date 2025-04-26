REGISTRY_OWNER:=fazenda
PROJECT_NAME:=weekly-exercises-py
PROJECT_TAG:=latest

all: interact

build:
	@docker buildx build --load --tag ${REGISTRY_OWNER}/${PROJECT_NAME}:${PROJECT_TAG} .

shell: build
	@docker run \
		--rm \
		--workdir /usr/src \
		--volume $(shell pwd):/usr/src \
		-it \
		${REGISTRY_OWNER}/${PROJECT_NAME}:${PROJECT_TAG} \
		/bin/sh

interact: build
	@docker run \
		--rm \
		--workdir /usr/src \
		--volume $(shell pwd):/usr/src \
		-it \
		${REGISTRY_OWNER}/${PROJECT_NAME}:${PROJECT_TAG} \
		python

test: build
	@docker run \
		--rm \
		-it \
		${REGISTRY_OWNER}/${PROJECT_NAME}:${PROJECT_TAG} \
		poetry run pytest --profile-svg && \
		poetry run python -m snakeviz prof/combined.prof

poetry-build:
	@poetry build

check: poetry-build
	@twine check dist/*
