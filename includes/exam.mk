INCLUDEPATH := $(dir $(lastword $(MAKEFILE_LIST)))

.PHONY: default clean realclean

default: $(shell ls *.tex | sed 's/^\(.*\)\.tex$$/\1.pdf/')

export TEXINPUTS := $(TEXINPUTS):$(INCLUDEPATH)

INCLUDEDEPS:=$(INCLUDEPATH)/csclogo.pdf\
	     $(INCLUDEPATH)/csc.sty

%-ANSWERS.pdf: %-ANSWERS.tex %.tex $(INCLUDEDEPS)
	pdflatex $<
	pdflatex $<

%.pdf: %.tex $(INCLUDEDEPS)
	pdflatex $<
	pdflatex $<

clean:
	rm -f *.aux *.log *.dvi

realclean: clean
	rm -f *.dvi *.pdf
