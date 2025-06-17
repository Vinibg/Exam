SHELL := /bin/bash
ARG ?= ""

.PHONY: setup
setup:
	docker build -t  vinibagodi/inatel .

.PHONY: run
run:
	docker run --rm -v $${PWD}/:/app/ ex1 ${ARG}