REGISTRY_OWNER:=fazenda
PROJECT_NAME:=weekly-exercises-r
PROJECT_TAG:=latest

all: interact

clean:
	@sudo rm -rf src/*.o src/*.so

build: clean
	@docker buildx build --load --tag ${REGISTRY_OWNER}/${PROJECT_NAME}:${PROJECT_TAG} .

shell: clean build
	@docker run \
		--rm \
		--workdir /usr/src \
		--volume $(shell pwd):/usr/src \
		-it \
		${REGISTRY_OWNER}/${PROJECT_NAME}:${PROJECT_TAG} \
		/bin/bash

interact: clean build
	@docker run \
		--rm \
		--workdir /usr/src \
		--volume $(shell pwd):/usr/src \
		-it \
		${REGISTRY_OWNER}/${PROJECT_NAME}:${PROJECT_TAG} \
		R

test: clean
	@docker run \
		--rm \
		${REGISTRY_OWNER}/${PROJECT_NAME}:${PROJECT_TAG} \
		R -e "devtools::test()"
