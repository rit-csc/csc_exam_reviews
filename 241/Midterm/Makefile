
.PHONY: default clean realclean

default: $(shell ls *.tex | sed 's/\(.*\)\.tex$$/ \1.pdf/')

#%.dvi: %.tex
#	latex $<


%-ANSWERS.pdf: %-ANSWERS.tex %.tex
	pdflatex $<

%.pdf: %.tex
	pdflatex $<

clean:
	rm -f *.aux *.log *.dvi

realclean: clean
	rm -f *.dvi *.pdf
