VENV = venv

THETA0 = 0
THETA1 = 0

.PHONY: up down clean re

all : up

up:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r dependencies.txt

clean :
	rm -rf venv
	rm -rf __pycache__
	

re: clean all
