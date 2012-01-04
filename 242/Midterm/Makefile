
.PHONY: default clean realclean

default: $(shell ls *.tex | sed 's/\(.*\)\.tex$$/\1.dvi \1.pdf/')

%.dvi: %.tex
	latex $<

%.pdf: %.tex
	pdflatex $<

clean:
	rm -f *.aux *.log *.dvi

realclean: clean
	rm -f *.dvi *.pdf
