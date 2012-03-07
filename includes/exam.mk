
.PHONY: default clean realclean

default: $(shell ls *.tex | sed 's/^\(.*\)\.tex$$/\1.pdf/')

%-ANSWERS.pdf: %-ANSWERS.tex %.tex 
	pdflatex $<

%.pdf: %.tex
	pdflatex $<

clean:
	rm -f *.aux *.log *.dvi

realclean: clean
	rm -f *.dvi *.pdf
