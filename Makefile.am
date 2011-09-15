MAINTAINERCLEANFILES = Makefile.in
vmctldir = @HA_NOARCHDATAHBDIR@/vm-ctl
vmctl_SCRIPTS = vm-ctl
vmctl_CONFIG = vm-ctl.conf
vmctllinkdir = /usr/sbin

vmctlcfgdir = @CONFIG_DIR@
SHAREDIR = $(vmctldir)
SPEC = $(PACKAGE_NAME).spec
TARFILE = $(PACKAGE_NAME)-$(VERSION).tar.gz
EXTRA_DIST = $(vmctl_SCRIPTS) $(vmctl_CONFIG) $(SPEC)

install-data-hook:
	@$(NORMAL_INSTALL)
	test -z "$(vmctlcfgdir)" || $(mkdir_p) "$(DESTDIR)$(vmctlcfgdir)"
	$(INSTALL_DATA) "$(vmctl_CONFIG)" "$(DESTDIR)$(vmctlcfgdir)"
	test -z "$(vmctllinkdir)" || $(mkdir_p) "$(DESTDIR)$(vmctllinkdir)"
	ln -sf $(vmctldir)/$(vmctl_SCRIPTS) $(vmctllinkdir)

uninstall-local:
	rm -rf $(vmctllinkdir)/vm-ctl

$(TARFILE):
	$(MAKE) dist

RPM_ROOT	= $(shell pwd)
RPMBUILDOPTS	= --define "_sourcedir $(RPM_ROOT)" \
		  --define "_specdir $(RPM_ROOT)"

srpm: clean
	rm -f $(TARFILE)
	$(MAKE) $(SPEC) $(TARFILE)
	rpmbuild $(RPMBUILDOPTS) $(DEFINE) --nodeps -bs --rmsource $(SPEC)

rpm: clean
	rm -f $(TARFILE)
	$(MAKE) $(SPEC) $(TARFILE)
	rpmbuild $(RPMBUILDOPTS) $(DEFINE) -ba --rmsource $(SPEC)
