Summary:	GNOME applet that monitors hardware sensors
Summary(pl):	Aplet GNOME do monitorowania sprzętowych sensorów
Name:		gnome-sensors
Version:	0.2.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.brendy.addr.com/linux/gnomesensors/GnomeSensors-%{version}.tar.gz
Patch0:		%{name}-configure.patch
Patch1:		%{name}-via.patch
BuildRequires:	lm_sensors-devel
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gnome-core-devel >= 1.1.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var

%description
GnomeSensors is a simple Gnome Panel applet that displays the current
readout of any hardware monitoring sensors that are present in your
computer.

%description -l pl
GnomeSensors jest małym apletem Gnome wyświetlającym wyniki odczytane
z sensorów monitorujących stan sprzętu.

%prep
%setup -q -n GnomeSensors-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__autoconf}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnorbadir=%{_sysconfdir}/CORBA/servers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README

%{_sysconfdir}/CORBA/servers/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applets/Monitors/*
%{_pixmapsdir}/*.xpm
