.PHONY: all
all: build

.PHONY: build
build:
	python3 ./gen_readme/gen-readme.py './algorithms' > README.md

.PHONY: githook
githook:
	git config core.hooksPath $(PWD)/hooks
