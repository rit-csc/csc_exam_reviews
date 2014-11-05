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

%.pdf: %.tex $(INCLUDEDEPS)
	pdflatex $< 
	pdflatex $< 

	make clean

clean:
	rm -f *.aux *.log *.dvi *.o *.pyc

realclean: clean
	rm -f *.dvi *.pdf *.o *.pyc
