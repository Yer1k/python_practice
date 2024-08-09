install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=src/*.py --cov=tests tests/test_*.py

format:	
	black src/*.py tests/*.py

lint:
	pylint --recursive=y src tests
	mypy .
# --disable=R,C --ignore-patterns=test_.*?py tests/*.py


# refactor: format lint

		
all: install lint test format