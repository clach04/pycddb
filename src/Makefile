all: rpm wininst

rpm:
	python setup.py bdist --formats=rpm

wininst:
	python setup.py bdist --formats=wininst

clean:
	rm -fr build dist