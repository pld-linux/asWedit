Summary:      text and HTML editor
Name:         asWedit
Version:      4.0
Copyright:    Non-commercially distributable
Group:        Applications/Editors
Release:      1d
######        http://www.advasoft.com/asWedit/
Source0:      %{name}-%{version}-i386.linux.tar.gz
######        http://www.advasoft.com/asWedit/i18n-resources/
Source1:      AsWedit-%{version}-cz.tar.gz
Source2:      AsWedit-%{version}-da.tar.gz
Source3:      AsWedit-%{version}-de.tar.gz
Source4:      AsWedit-%{version}-en.tar.gz
Source5:      AsWedit-%{version}-es.tar.gz
Source6:      AsWedit-%{version}-fr.tar.gz
Source7:      AsWedit-%{version}-nl.tar.gz
Source8:      AsWedit-%{version}-pl.tar.gz
Source9:      AsWedit-%{version}-pt.tar.gz
Source10:     AsWedit-%{version}-sv.tar.gz
Patch:        %{name}-helpDir.patch
Buildroot:    /var/tmp/%{name}-%{version}-root 
ExclusiveArch: i386
ExclusiveOs:   Linux
Group(pl):    Aplikacje/Edytory
Summary(pl):  edytor tekstowy i HTML

%description
asWedit is powerfull editor for text file and HTML pages.

%description -l pl
asWedit jest edytorem plików tekstowych i HTML. Bardzo ³adnie pod¶wietla
sk³adnie HTML i co wa¿niejsze nie pozwala na tworzenie niezgodnych ze 
specyfikacj± HTML 4.0 stron WWW.

%prep
# %setup -q
%setup -q -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10
%patch -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -D asWedit $RPM_BUILD_ROOT/usr/X11R6/bin/asWedit
install -D asWedit.hlp $RPM_BUILD_ROOT/usr/X11R6/lib/asWedit.hlp

install -D AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/AsWedit
install -D cz/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/cz/app-defaults/AsWedit
install -D da/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/da/app-defaults/AsWedit
install -D de/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/de/app-defaults/AsWedit
install -D en/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/en/app-defaults/AsWedit
install -D es/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/es/app-defaults/AsWedit
install -D fr/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/fr/app-defaults/AsWedit
install -D nl/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/nl/app-defaults/AsWedit
install -D pl/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/pl/app-defaults/AsWedit
install -D pt/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/pt/app-defaults/AsWedit
install -D sv/AsWedit $RPM_BUILD_ROOT/usr/X11R6/lib/X11/sv/app-defaults/AsWedit

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(711,root,root) /usr/X11R6/bin/asWedit
/usr/X11R6/lib/asWedit.hlp
/usr/X11R6/lib/X11/app-defaults/AsWedit

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

%changelog
* Tue Jan  5 1999 Artur Frysiak <wiget@usa.net>
[4.0-1d]
- first rpm release
