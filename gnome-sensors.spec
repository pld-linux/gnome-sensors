Summary:	GNOME applet that monitors hardware sensors
Summary(pl):	Aplet GNOME do monitorowania sprzêtowych sensorów
Name:		gnome-sensors
Version:	1.7.4
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sensors-applet/sensors-applet-%{version}.tar.gz
# Source0-md5:	ca02bb8c9641468ebb3350b318ac2a86
URL:		http://sensors-applet.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-panel-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libtool
BuildRequires:	lm_sensors-devel
BuildRequires:	pkgconfig
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnomeSensors is a simple GNOME Panel applet that displays the current
readout of any hardware monitoring sensors that are present in your
computer.

%description -l pl
GnomeSensors jest ma³ym apletem GNOME wy¶wietlaj±cym wyniki odczytane
z sensorów monitoruj±cych stan sprzêtu.

%prep
%setup -q -n sensors-applet-%{version}

%build
%configure --disable-scrollkeeper

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

%find_lang sensors-applet --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f sensors-applet.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/sensors-applet
%{_libdir}/bonobo/servers/SensorsApplet.server
%{_iconsdir}/*/*/*/sensors-*
%{_pixmapsdir}/sensors-applet
%{_datadir}/gnome-2.0/ui/SensorsApplet.xml
%{_datadir}/omf/sensors-applet
