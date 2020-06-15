ifeq ($(PACKAGE_SET),vm)
	ifeq ($(DISTRIBUTION),centos)
		RPM_SPEC_FILES := \
			python-xcffib.spec
	endif
endif

NO_ARCHIVE := 1

DEBIAN_BUILD_DIRS.buster := debian-pkg/debian
DEBIAN_BUILD_DIRS.stretch := debian-pkg/debian
DEBIAN_BUILD_DIRS := $(DEBIAN_BUILD_DIRS.$(DIST))

SOURCE_COPY_IN.debian := source-debian-copy-in
SOURCE_COPY_IN.qubuntu := source-debian-copy-in
SOURCE_COPY_IN := $(SOURCE_COPY_IN.$(DISTRIBUTION))

source-debian-copy-in: VERSION = $(shell cat $(ORIG_SRC)/version)
source-debian-copy-in: ORIG_FILE = $(CHROOT_DIR)/$(DIST_SRC)/xcffib_$(VERSION).orig.tar.gz
source-debian-copy-in: SRC_FILE  = $(ORIG_SRC)/xcffib-$(VERSION).tar.gz
source-debian-copy-in:
	cp -p $(SRC_FILE) $(ORIG_FILE)
	tar xzf $(SRC_FILE) -C $(CHROOT_DIR)/$(DIST_SRC)/debian-pkg --strip-components=1
