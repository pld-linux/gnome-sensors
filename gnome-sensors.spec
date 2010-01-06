#
%define		_orig_name	sensors-applet
#
Summary:	GNOME applet that monitors hardware sensors
Summary(pl.UTF-8):	Aplet GNOME monitorujący czujniki sprzętowe
Name:		gnome-sensors
Version:	2.2.1
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sensors-applet/sensors-applet-%{version}.tar.gz
# Source0-md5:	4ba94415125db147efcc1ae76f9703ee
URL:		http://sensors-applet.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gnome-panel-devel >= 2.22.0
BuildRequires:	gtk+2-devel >= 2:2.10.2
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgnomeui-devel >= 2.22.0
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	libtool
BuildRequires:	libxslt-progs >= 1.1.17
BuildRequires:	lm_sensors-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk+2 >= 2:2.10.2
Requires(post,postun):	scrollkeeper
Requires:	%{name}-libs = %{version}-%{release}
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
GNOME Sensors Applet is a simple applet that displays the current
readout of any hardware monitoring sensors that are present in
computer.

%description -l pl.UTF-8
GNOME Sensors jest prostym apletem wyświetlającym aktualne odczyty
dowolnych czujników monitorujących obecnych w komputerze.

%package libs
Summary:	GNOME Sensors Applet library
Summary(pl.UTF-8):	Biblioteka apletu GNOME Sensors
Group:		X11/Libraries

%description libs
GNOME Sensors Applet library.

%description libs -l pl.UTF-8
Biblioteka apletu GNOME Sensors.

%package devel
Summary:	Header files for GNOME Sensors Applet library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki apletu GNOME Sensors
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for GNOME Sensors Applet library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki apletu GNOME Sensors.

%package static
Summary:	Static GNOME Sensors Applet library
Summary(pl.UTF-8):	Statyczna biblioteka apletu GNOME Sensors
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GNOME Sensors Applet library.

%description static -l pl.UTF-8
Statyczna biblioteka apletu GNOME Sensors.

%prep
%setup -q -n %{_orig_name}-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/sensors-applet/plugins/*.{a,la}

%find_lang %{_orig_name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f sensors-applet.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/sensors-applet
%dir %{_libdir}/sensors-applet
%dir %{_libdir}/sensors-applet/plugins
%attr(755,root,root) %{_libdir}/sensors-applet/plugins/*.so
%{_libdir}/bonobo/servers/SensorsApplet.server
%{_iconsdir}/hicolor/*/*/sensors-*
%{_pixmapsdir}/sensors-applet
%{_datadir}/gnome-2.0/ui/SensorsApplet.xml

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsensors-applet-plugin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsensors-applet-plugin.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsensors-applet-plugin.so
%{_libdir}/libsensors-applet-plugin.la
%{_includedir}/sensors-applet

%files static
%defattr(644,root,root,755)
%{_libdir}/libsensors-applet-plugin.a
