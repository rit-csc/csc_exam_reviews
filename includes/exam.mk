INCLUDEPATH := $(dir $(lastword $(MAKEFILE_LIST)))

.PHONY: default clean realclean

default: $(shell ls *.tex | sed 's/^\(.*\)\.tex$$/\1.pdf/')

export TEXINPUTS := $(TEXINPUTS):$(INCLUDEPATH)

INCLUDEDEPS:=$(INCLUDEPATH)/csclogo.pdf\
	     $(INCLUDEPATH)/csc.sty\
	     questions/*

%-ANSWERS.pdf: %-ANSWERS.tex %.tex $(INCLUDEDEPS)
	pdflatex $<
	pdflatex $<

%.pdf: %.tex $(INCLUDEDEPS)
	pdflatex $< $INCLUDEPATH/questions/*.tex
	pdflatex $< $INCLUDEPATH/questions/*.tex

	make clean

clean:
	rm -f *.aux *.log *.dvi *.o

realclean: clean
	rm -f *.dvi *.pdf *.o
