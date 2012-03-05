
.PHONY: build

build:
	$(MAKE) -C 241
	$(MAKE) -C 242
	$(MAKE) -C 243

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
	$(MAKE) -C 241 $@
	$(MAKE) -C 242 $@
	$(RM) -rf publish

%:
	$(MAKE) -C 241 $@
	$(MAKE) -C 242 $@
	$(MAKE) -C 243 $@
