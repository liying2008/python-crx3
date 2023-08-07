.PHONY: protoc build publish
init:
	pip install -r requirements-dev.txt
test:
	# This runs all of the tests on all supported Python versions.
	tox

protoc:
	protoc -I=./src/crx3 --python_out=pyi_out:./src/crx3 ./src/crx3/crx3.proto

build:
	rm -fr build dist .egg crx3.egg-info
	python setup.py sdist bdist_wheel

publish: build
	pip install 'twine>=1.5.0'
	twine upload dist/*
