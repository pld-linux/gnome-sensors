Summary:	GNOME applet that monitors hardware sensors
Summary(pl):	Aplet GNOME do monitorowania sprzêtowych sensorów
Name:		gnome-sensors
Version:	0.2.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	GnomeSensors-%{version}.tar.gz
# Source0-md5:	3ebdfddaff3cfb4ca7ad5ee7e48b2002
Source1:	%{name}.m4
Patch0:		%{name}-configure.patch
Patch1:		%{name}-via.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel >= 1.0.0
BuildRequires:	gnome-core-devel >= 1.1.0
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	lm_sensors-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var

%description
GnomeSensors is a simple Gnome Panel applet that displays the current
readout of any hardware monitoring sensors that are present in your
computer.

%description -l pl
GnomeSensors jest ma³ym apletem Gnome wy¶wietlaj±cym wyniki odczytane
z sensorów monitoruj±cych stan sprzêtu.

%prep
%setup -q -n GnomeSensors-%{version}
%patch0 -p1
%patch1 -p1

install %{SOURCE1} macros/

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__automake}
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
