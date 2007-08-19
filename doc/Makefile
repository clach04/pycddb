TARGETS=PyCDDB.html PyCDDB.pdf PyCDDB.txt index.html

target : $(TARGETS)

upload : $(TARGETS)
	scp index.html sro@shell.sourceforge.net:/home/groups/p/py/pycddb/htdocs

PyCDDB.html : PyCDDB.sgml
	docbook2html -u PyCDDB.sgml

PyCDDB.pdf: PyCDDB.sgml
	docbook2pdf PyCDDB.sgml

PyCDDB.txt : PyCDDB.sgml
	docbook2txt PyCDDB.sgml
	cp PyCDDB.txt ../README

index.html : PyCDDB.html
	sed -f sourceforge.sed $< > $@
