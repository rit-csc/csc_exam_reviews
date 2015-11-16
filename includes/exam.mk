INCLUDEPATH := $(dir $(lastword $(MAKEFILE_LIST)))

TARGETS = *.pdf
DEPS_DIR = .deps
LATEXMK = latexmk -recorder -use-make -deps

# We want latexmk to *always* run because make does not have the
# necessary info on dependencies.
.PHONY: %.pdf default clean realclean

default: $(shell ls *.tex | sed 's/^\(.*\)\.tex$$/\1.pdf/')

export TEXINPUTS := $(TEXINPUTS):$(INCLUDEPATH)

$(foreach file,$(TARGETS),$(eval -include $(DEPS_DIR)/$(file)deps))

$(DEPS_DIR):
	mkdir $@

%.pdf: %.tex
	if [ ! -e $(DEPS_DIR) ]; then mkdir $(DEPS_DIR); fi
	$(LATEXMK) -pdf -deps-out=$(DEPS_DIR)/$@deps $<

clean:
	rm -f *.log *.aux
	rm -f *.dvi

realclean: clean
	rm -rf .deps
	rm -f *.fdb_latexmk
	rm -f *.fls
	rm -f *.pdf
	# rm *.pyc, *.o, *.class?

