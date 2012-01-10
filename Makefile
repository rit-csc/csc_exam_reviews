
.PHONY: build

build:
	$(MAKE) -C 241
	$(MAKE) -C 242

%:
	$(MAKE) -C 241 $@
	$(MAKE) -C 242 $@
