.PHONY: build publish
init:
	pip install -r requirements-dev.txt
test:
	# This runs all of the tests on all supported Python versions.
	tox


build:
	rm -fr build dist .egg crx3.egg-info
	python setup.py sdist bdist_wheel

publish: build
	pip install 'twine>=1.5.0'
	twine upload dist/*
