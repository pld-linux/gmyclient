Summary:	MySQL client for Gnome
Summary(pl):	Graficzny klient baz MySQL dla ¶rodowiska Gnome
Name:		gmyclient
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://gmyclient.sourceforge.net/download/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-acfix.patch
URL:		http://gmyclient.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.3
BuildRequires:	libglade-gnome-devel
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gmyclient is a powerful graphical mysql client to use under gnome.
Gmyclient is designed to be a simple, quick, and powerful way to
access your MySQL database.It provides you a powerful way to
create/edit all MySQL database objects most easy and simple way.

%description -l pl
Gmyclient jest graficznym klientem MySQL przeznaczonym dla ¶rodowiska
Gnome. Gmyclienta zaprojektowano tak, by zapewnia³ ³atwy, szybki i w
pe³ni funkcjonalny dostêp do baz danych MySQL. Umo¿liwia on tworzenie
i edycjê baz MySQL.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
aclocal -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Office/Databases,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Office/Databases
install pixmaps/gmyclient_icon.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO NEWS ChangeLog
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/gmyclient
%dir %{_libdir}/gmyclient/plugins
%attr(755,root,root) %{_libdir}/gmyclient/plugins/*.so
%{_datadir}/%{name}
%{_applnkdir}/Office/Databases/%{name}.desktop
%{_pixmapsdir}/*
