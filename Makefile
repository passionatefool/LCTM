.PHONY: all
all: build

.PHONY: build
build:
	python3 ./gen_readme/gen-readme.py './algorithms' > README.md

.PHONY: docker-build
docker-build:
	DOCKER_BUILDKIT=0 docker build -t passionatefool/lctm ./gen_readme
	docker run --rm -v "`pwd`/algorithms":/app/algorithms passionatefool/lctm "python3 gen-readme.py ./algorithms" > README.md

.PHONY: githook
githook:
	git config core.hooksPath $(PWD)/hooks
