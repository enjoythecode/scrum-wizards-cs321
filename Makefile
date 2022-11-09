.PHONY: dev, open, dependencies, rmdb, new, docker-build, docker-run

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

docker-build:
	docker image build -t flask-docker .

docker-run:
	docker run -p 5000:5000 -d flask-docker
