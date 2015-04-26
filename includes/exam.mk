INCLUDEPATH := $(dir $(lastword $(MAKEFILE_LIST)))

.PHONY: default clean realclean

default: $(shell ls *.tex | sed 's/^\(.*\)\.tex$$/\1.pdf/')

ifeq ($(shell ls -1 code/ | wc -l),0)
CODEINC := ''
else
CODEINC := $(shell ls -d code/*)
endif

ifeq ($(shell ls -1 questions/ | wc -l),0)
QUESTINC := ''
else
QUESTINC := $(shell ls -d questions/*)
endif

export TEXINPUTS := $(TEXINPUTS):$(INCLUDEPATH)

INCLUDEDEPS:=$(INCLUDEPATH)/csclogo.pdf\
	     $(INCLUDEPATH)/csc.sty\
	     $(QUESTINC)\
	     $(CODEINC)

%-ANSWERS.pdf: %-ANSWERS.tex %.tex $(INCLUDEDEPS)
	pdflatex $<
	pdflatex $<
	mv *.pdf out/pdf/answers
	mv *.log out/log/
	mv *.aux out/aux/

%.pdf: %.tex $(INCLUDEDEPS)
	pdflatex $< 
	pdflatex $< 
	mv *.pdf out/pdf/blanks
	mv *.log out/log/
	mv *.aux out/aux/

clean:
	rm -f out/log/* out/aux/*
	rm -f out/*/*.dvi

realclean: clean
	rm -f out/*/*/*
	rm -f out/pdf/*.pdf
	# rm *.pyc, *.o, *.class?

