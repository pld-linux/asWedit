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
# Source0-md5:	c3d00e0886a2316e46ef05f4c204c0ed
# http://www.uni-koeln.de/ftp/www/asWedit-4.0/i18n-resources/
Source1:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-cz.tar.gz
# Source1-md5:	fd559437bcd9acfdf868b07da53fb7e1
Source2:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-da.tar.gz
# Source2-md5:	bf9a82c5bed2fb364f8e189a439d3e17
Source3:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-de.tar.gz
# Source3-md5:	5d74c0a19e8e36db291765716b96989a
Source4:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-en.tar.gz
# Source4-md5:	d9b6fbef34752878e2b81095d130a7d5
Source5:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-es.tar.gz
# Source5-md5:	443c0bb77495e963c1ba6882400651fd
Source6:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-fr.tar.gz
# Source6-md5:	16ead513e41338408f2e7382687e5ab9
Source7:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-nl.tar.gz
# Source7-md5:	4ec10e437609c83822657996b0a78c20
Source8:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-pl.tar.gz
# Source8-md5:	7c905e467e8126ad39703174f8dedbac
Source9:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-pt.tar.gz
# Source9-md5:	ea7cdb75af11b42cd847b0c6a4a2e923
Source10:	http://www.advasoft.com/asWedit/i18n-resources/AsWedit-%{resver}-sv.tar.gz
# Source10-md5:	4bf99d3481f7471d78cccf2b81f482dc
Source11:	%{name}.wmconfig
# Source11-md5:	cfcf138ffaf619f0e84a952383635d44
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
