.PHONY: dev, open, dependencies

dependencies:
	pip install -r requirements.txt

dev:
	python3.10 main.py

open:
	open http://127.0.0.1:5000

