
.PHONY: build

build:
	$(MAKE) -C 140
	$(MAKE) -C 141
	$(MAKE) -C 142
	$(MAKE) -C mop

publish: build
	rm -rf publish/
	find . -name '*.pdf' -exec echo \'{}\' \; \
	| xargs -n1 dirname	\
	| sed s/\'/\\\'/g	\
	| sed s/\"/\\\"/g	\
	| awk '{print "'\''publish/"$$0"'\''"}'	\
	| tee /dev/tty | xargs -n1 mkdir -p
	find . -name '*.pdf' -exec ln -f {} publish/{} \;

realclean:
	$(MAKE) -C 140 $@
	$(MAKE) -C 141 $@
	$(MAKE) -C 142 $@
	$(MAKE) -C mop $@
	$(RM) -rf publish

%:
	$(MAKE) -C 140 $@
	$(MAKE) -C 141 $@
	$(MAKE) -C 142 $@
	$(MAKE) -C mop $@
