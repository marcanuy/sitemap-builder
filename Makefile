install:
	python3 -m pip install --user --upgrade setuptools wheel 
	python3 -m pip install --user --upgrade twine
generate-package:
	python3 setup.py sdist bdist_wheel
upload-test:
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
upload:
	python3 -m twine upload dist/*
test:
	python -m unittest discover
