Summary:	MySql client for Gnome
Summary(pl):	Graficzny klient baz MySql dla ¶rodowiska Gnome
Name:		gmyclient
Version:	0.3
Release:	0.1
License:	GPL
Group:		X11/Applications/Database
Source0:	http://gmyclient.sourceforge.net/download/%{name}-%{version}.tar.gz
#Patch0:		%{name}-pld.patch
#Patch1:		%{name}-no_libnsl.patch
URL:		http://gmyclient.sourecforge.net/
BuildRequires:	gtk+-devel >= 1.2.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gmyclient is a powerful graphical mysql client to use under gnome.Gmyclient is designed to be a simple, quick, and powerful way to access your MySQL database.It provides you a powerful way to create/edit all MySQL database objects most easy and simple way.
%description -l pl
Gmyclient jest graficznym klientem MySql przeznaczonym dla ¶rodowisa Gnome.Gmyclient'a zaprojektowano tak by zapewnia³ ³atwy, szybki i w pe³ni funkcjonalny dostêp do baz danych MySql.Umo¿liwia on tworzenie i edycje Baz MySql.
%prep
%setup -q
#%patch0 -p1
#%patch1 -p1

%build
#rm -f missing
libtoolize --copy --force
aclocal -I macros
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 
#	Utilitiesdir=%{_applnkdir}/Network/FTP

gzip -9nf README TODO INSTALL NEWS COPYING ChangeLog 

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/pixmaps/*.xpm
%{_datadir}/%{name}/pixmaps/*.png
