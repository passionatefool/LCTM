.PHONY: all
all: build

.PHONY: build
build:
	python3 gen_readme/gen-readme.py --path=./algorithms --cache=./cache/questions.json --tmpl=./readme.jinja --output=./README.md

.PHONY: docker-build
docker-build:
	DOCKER_BUILDKIT=0 docker build -t passionatefool/lctm ./gen_readme
	docker run --rm -v "`pwd`":/app passionatefool/lctm build

.PHONY: githook
githook:
	git config core.hooksPath $(PWD)/hooks
