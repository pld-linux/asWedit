Summary:       Text and HTML editor
Summary(pl):   Edytor tekstowy i HTML
Name:          asWedit
Version:       4.0
Copyright:     Non-commercially distributable
Group:         Applications/Editors
Group(pl):     Aplikacje/Edytory
Release:       2
######         http://www.advasoft.com/asWedit
Source0:        %{name}-%{version}-i386.linux.tar.gz
######         http://www.advasoft.com/asWedit/i18n-resources
Source1:       AsWedit-%{version}-cz.tar.gz
Source2:       AsWedit-%{version}-da.tar.gz
Source3:       AsWedit-%{version}-de.tar.gz
Source4:       AsWedit-%{version}-en.tar.gz
Source5:       AsWedit-%{version}-es.tar.gz
Source6:       AsWedit-%{version}-fr.tar.gz
Source7:       AsWedit-%{version}-nl.tar.gz
Source8:       AsWedit-%{version}-pl.tar.gz
Source9:       AsWedit-%{version}-pt.tar.gz
Source10:      AsWedit-%{version}-sv.tar.gz
Source11:      %{name}.wmconfig
Patch:         %{name}-helpDir.patch
Requires:      libc
BuildRoot:	/tmp/%{name}-%{version}-root
ExclusiveArch: %{ix86}

%description
asWedit is powerful editor for text file and HTML pages. It contains
syntax highlighting and HTML 4.0 validating.

%description -l pl
AsWedit jest edytorem plików tekstowych i HTML. Bardzo ³adnie pod¶wietla
sk³adnie HTML i co wa¿niejsze nie pozwala na tworzenie niezgodnych ze 
specyfikacj± HTML 4.0 stron WWW.

%prep
%setup -q -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10
%patch -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,lib/X11/app-defaults}
install -d $RPM_BUILD_ROOT/usr/X11R6/lib/X11/{cz,da,de,en,es,fr,nl,pl,pt,sv}/app-defaults
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

install  -s asWedit $RPM_BUILD_ROOT/usr/X11R6/bin/asWedit
install  asWedit.hlp $RPM_BUILD_ROOT/usr/X11R6/lib/asWedit.hlp

install  AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/AsWedit
install  cz/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/cz/app-defaults/AsWedit
install  da/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/da/app-defaults/AsWedit
install  de/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/de/app-defaults/AsWedit
install  en/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/en/app-defaults/AsWedit
install  es/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/es/app-defaults/AsWedit
install  fr/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fr/app-defaults/AsWedit
install  nl/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/nl/app-defaults/AsWedit
install  pl/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/pl/app-defaults/AsWedit
install  pt/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/pt/app-defaults/AsWedit
install  sv/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/sv/app-defaults/AsWedit
install  %{SOURCE11} $RPM_BUILD_ROOT/etc/X11/wmconfig/asWedit

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) /usr/X11R6/bin/asWedit
/usr/X11R6/lib/asWedit.hlp
/usr/X11R6/lib/X11/app-defaults/AsWedit

%config(missingok) /etc/X11/wmconfig/*

%lang(cz) /usr/X11R6/lib/X11/cz/app-defaults/AsWedit
%lang(da) /usr/X11R6/lib/X11/da/app-defaults/AsWedit
%lang(de) /usr/X11R6/lib/X11/de/app-defaults/AsWedit
%lang(en) /usr/X11R6/lib/X11/en/app-defaults/AsWedit
%lang(es) /usr/X11R6/lib/X11/es/app-defaults/AsWedit
%lang(fr) /usr/X11R6/lib/X11/fr/app-defaults/AsWedit
%lang(nl) /usr/X11R6/lib/X11/nl/app-defaults/AsWedit
%lang(pl) /usr/X11R6/lib/X11/pl/app-defaults/AsWedit
%lang(pt) /usr/X11R6/lib/X11/pt/app-defaults/AsWedit
%lang(sv) /usr/X11R6/lib/X11/sv/app-defaults/AsWedit
