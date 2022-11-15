.PHONY: dev, open, dependencies, test, coverage, coverage-open

dependencies:
	pip install -r requirements.txt

dev:
	python3.10 main.py

open:
	open http://127.0.0.1:5000

test:
	python3 -m pytest

coverage:
	coverage run -m pytest && coverage report --sort cover

coverage-open:
	coverage run -m pytest && coverage html && open htmlcov/index.html
