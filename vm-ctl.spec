########################################
# Derived definitions
########################################
%define name vm-ctl
%define version 1.0
%define release 1
%define prefix /usr
%define vmctldir vm-ctl
Summary: Pacemaker VirtualDomain resource  generator.
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Group: Applications
Source: %{name}-%{version}.tar.gz
License: GPL
Vendor: NIPPON TELEGRAPH AND TELEPHONE CORPORATION
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildRequires: make
BuildArch: noarch
Requires: pacemaker >= 1.0.10

########################################
%description
Generate crm-file from cmmandline and config-file.

########################################
%prep
########################################
rm -rf $RPM_BUILD_ROOT

########################################
%setup -q
########################################

########################################
%build
########################################

########################################
%configure
########################################

########################################
%pre
########################################

########################################
%install
########################################
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT%{prefix}/sbin
ln -sf %{prefix}/share/pacemaker/%{vmctldir}/%{name} $RPM_BUILD_ROOT%{prefix}/sbin/%{name}

########################################
%clean
########################################
if
	[ -n "${RPM_BUILD_ROOT}"  -a "${RPM_BUILD_ROOT}" != "/" ]
then
	rm -rf $RPM_BUILD_ROOT
fi
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

########################################
%post
########################################
true
########################################
%preun
########################################
true
########################################
%postun
########################################
true

########################################
%files
########################################
%defattr(-,root,root)
%dir %{prefix}/share/pacemaker/%{vmctldir}
%config /etc/vm-ctl.conf
%{prefix}/share/pacemaker/%{vmctldir}/%{name}
%{prefix}/sbin/%{name}

########################################
%changelog
########################################
* Tue May 31 2011 Yuusuke IIDA <iidayuus@intellilink.co.jp>
- initial release
