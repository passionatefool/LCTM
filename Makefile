.PHONY: all
all: build

.PHONY: build
build:
	python3 gen_readme/gen-readme.py --path=./algorithms --cache=./cache/questions.json --tmpl=./readme.jinja > README.md

.PHONY: docker-build
docker-build:
	DOCKER_BUILDKIT=0 docker build -t passionatefool/lctm ./gen_readme
	docker run --rm -v "`pwd`/cache":/app/cache -v "`pwd`/readme.jinja":/app/readme.jinja -v "`pwd`/algorithms":/app/algorithms passionatefool/lctm "python3 gen-readme.py --path=./algorithms --cache=./cache/questions.json --tmpl=./readme.jinja" > README.md

.PHONY: githook
githook:
	git config core.hooksPath $(PWD)/hooks
