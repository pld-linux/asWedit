Summary:	Text and HTML editor
Summary(pl):	Edytor tekstu i HTML
Name:		asWedit
Version:	4.0
%define	resver	4.0
License:	non-commercial
Group:		Applications/Editors
Release:	4
# advasoft.com seems not working, one of working mirrors:
# http://www.uni-koeln.de/ftp/www/asWedit-4.0/ 
Source0:	http://www.advasoft.com/asWedit/%{name}-%{version}-i386.linux.tar.gz
# http://www.uni-koeln.de/ftp/www/asWedit-4.0/i18n-resources/
Source1:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-cz.tar.gz
Source2:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-da.tar.gz
Source3:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-de.tar.gz
Source4:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-en.tar.gz
Source5:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-es.tar.gz
Source6:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-fr.tar.gz
Source7:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-nl.tar.gz
Source8:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-pl.tar.gz
Source9:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-pt.tar.gz
Source10:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-sv.tar.gz
Source11:	%{name}.wmconfig
Patch0:		%{name}-helpDir.patch
URL:		http://www.advasoft.com/asWedit/
Requires:	libc
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
asWedit is powerful editor for text file and HTML pages. It contains
syntax highlighting and HTML 4.0 validating.

%description -l pl
AsWedit jest edytorem plików tekstowych i HTML. Bardzo ³adnie
pod¶wietla sk³adniê HTML i, co wa¿niejsze, nie pozwala na tworzenie
niezgodnych ze specyfikacj± HTML 4.0 stron WWW.

%prep
%setup -q -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/X11/app-defaults} \
	$RPM_BUILD_ROOT%{_libdir}/X11/{cs,da,de,en,es,fr,nl,pl,pt,sv}/app-defaults \
	$RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig

install  asWedit $RPM_BUILD_ROOT%{_bindir}/asWedit
install  asWedit.hlp $RPM_BUILD_ROOT%{_libdir}/asWedit.hlp

install  AsWedit $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/AsWedit
install  cz/AsWedit $RPM_BUILD_ROOT%{_libdir}/X11/cs/app-defaults/AsWedit
install  da/AsWedit $RPM_BUILD_ROOT%{_libdir}/X11/da/app-defaults/AsWedit
install  de/AsWedit $RPM_BUILD_ROOT%{_libdir}/X11/de/app-defaults/AsWedit
install  en/AsWedit $RPM_BUILD_ROOT%{_libdir}/X11/en/app-defaults/AsWedit
install  es/AsWedit $RPM_BUILD_ROOT%{_libdir}/X11/es/app-defaults/AsWedit
install  fr/AsWedit $RPM_BUILD_ROOT%{_libdir}/X11/fr/app-defaults/AsWedit
install  nl/AsWedit $RPM_BUILD_ROOT%{_libdir}/X11/nl/app-defaults/AsWedit
install  pl/AsWedit $RPM_BUILD_ROOT%{_libdir}/X11/pl/app-defaults/AsWedit
install  pt/AsWedit $RPM_BUILD_ROOT%{_libdir}/X11/pt/app-defaults/AsWedit
install  sv/AsWedit $RPM_BUILD_ROOT%{_libdir}/X11/sv/app-defaults/AsWedit
install %{SOURCE11} $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/asWedit

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/asWedit
%{_libdir}/asWedit.hlp
%{_libdir}/X11/app-defaults/AsWedit

%config(missingok) %{_sysconfdir}/X11/wmconfig/*

%{_libdir}/X11/en/app-defaults/AsWedit
%lang(cs) %{_libdir}/X11/cs/app-defaults/AsWedit
%lang(da) %{_libdir}/X11/da/app-defaults/AsWedit
%lang(de) %{_libdir}/X11/de/app-defaults/AsWedit
%lang(es) %{_libdir}/X11/es/app-defaults/AsWedit
%lang(fr) %{_libdir}/X11/fr/app-defaults/AsWedit
%lang(nl) %{_libdir}/X11/nl/app-defaults/AsWedit
%lang(pl) %{_libdir}/X11/pl/app-defaults/AsWedit
%lang(pt) %{_libdir}/X11/pt/app-defaults/AsWedit
%lang(sv) %{_libdir}/X11/sv/app-defaults/AsWedit
