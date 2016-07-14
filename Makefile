all: env test

checkenv:
	@which convert || @echo "Please install imagemagick"
	@which tesseract || @echo "Please install tesseract"
	@which python3 || @echo "Please install Python 3"
	@echo "== System env: OK"

env:checkenv
	pip3 install -r requirements.txt
	@echo "== Python env: OK"

test:
	python3 main.py test.png | grep -c "Alt J"
	python3 main.py test.png | grep -c "Flume Remix"
	@echo "== Tests: OK"
