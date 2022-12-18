.PHONY: dev, open, dependencies, rmdb, new, test, coverage, coverage-open, pre-commit-install, checkall

dependencies:
	pip install -r requirements.txt

dev:
	python3.10 main.py

open:
	open http://127.0.0.1:5000

rmdb:
	rm instance/database.db

new:
	make rmdb
	osascript -e 'tell application "Terminal" to activate' \
  -e 'tell application "System Events" to tell process "Terminal" to keystroke "t" using command down' \
  -e 'tell application "Terminal" to do script "sleep 1" in selected tab of the front window' \
  -e 'tell application "Terminal" to do script "make open" in selected tab of the front window'
	make dev

test:
	(. venv/bin/activate && venv/bin/python -m pytest)

coverage:
	coverage run -m pytest && coverage report --sort cover

coverage-open:
	coverage run -m pytest && coverage html && open htmlcov/index.html

pre-commit-install:
	pre-commit install

check:
	pre-commit run

checkall:
	pre-commit run --all-files

# uses radon [https://pypi.org/project/radon/] to analyze codebase and write results to
# a folder.
# make sure radon is installed, documentation mentions it supports *up to* python 3.8
analyze:
	./radon_analyze.sh
