#
%define		_orig_name	sensors-applet
#
Summary:	GNOME applet that monitors hardware sensors
Summary(pl):	Aplet GNOME monitoruj±cy czujniki sprzêtowe
Name:		gnome-sensors
Version:	1.7.4
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sensors-applet/sensors-applet-%{version}.tar.gz
# Source0-md5:	ca02bb8c9641468ebb3350b318ac2a86
URL:		http://sensors-applet.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.7.1
BuildRequires:	gnome-panel-devel >= 2.14.2
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	libtool
BuildRequires:	libxslt-progs >= 1.1.17
BuildRequires:	lm_sensors-devel >= 2.10.0
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk+2 >= 2:2.10.0
Requires(post,postun):	scrollkeeper
Requires:	hicolor-icon-theme
Requires:	gnome-panel >= 2.14.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Sensors Applet is a simple applet that displays the current
readout of any hardware monitoring sensors that are present in
computer.

%description -l pl
GNOME Sensors jest prostym apletem wy¶wietlaj±cym aktualne odczyty
dowolnych czujników monitoruj±cych obecnych w komputerze.

%prep
%setup -q -n %{_orig_name}-%{version}

%build
LDFLAGS="%{rpmldflags} -Wl,--as-needed"
%configure \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

%find_lang %{_orig_name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor

%postun
%scrollkeeper_update_post
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor

%files -f sensors-applet.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/sensors-applet
%{_libdir}/bonobo/servers/SensorsApplet.server
%{_iconsdir}/hicolor/*/*/sensors-*
%{_pixmapsdir}/sensors-applet
%{_datadir}/gnome-2.0/ui/SensorsApplet.xml
%{_datadir}/omf/sensors-applet
