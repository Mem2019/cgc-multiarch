TOPTARGETS := all clean

SUBDIRS := $(wildcard cgc-challenge-corpus/?????_?????)

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
	sed -i -e "s|^include .*|include ../../single-mk|" $@/Makefile
	timeout -s KILL 1m $(MAKE) -C $@ $(MAKECMDGOALS) || true

.PHONY: $(TOPTARGETS) $(SUBDIRS)
