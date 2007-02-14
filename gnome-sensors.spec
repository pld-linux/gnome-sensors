#
%define		_orig_name	sensors-applet
#
Summary:	GNOME applet that monitors hardware sensors
Summary(pl.UTF-8):	Aplet GNOME monitorujący czujniki sprzętowe
Name:		gnome-sensors
Version:	1.7.8
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sensors-applet/sensors-applet-%{version}.tar.gz
# Source0-md5:	0d71eaae6f4bad3c1b6d44d71929d954
URL:		http://sensors-applet.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.7.2
BuildRequires:	gnome-panel-devel >= 2.15.92
BuildRequires:	gtk+2-devel >= 2:2.10.2
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	libtool
BuildRequires:	libxslt-progs >= 1.1.17
BuildRequires:	lm_sensors-devel >= 2.10.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk+2 >= 2:2.10.2
Requires(post,postun):	scrollkeeper
Requires:	hicolor-icon-theme
Requires:	gnome-panel >= 2.15.92
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Sensors Applet is a simple applet that displays the current
readout of any hardware monitoring sensors that are present in
computer.

%description -l pl.UTF-8
GNOME Sensors jest prostym apletem wyświetlającym aktualne odczyty
dowolnych czujników monitorujących obecnych w komputerze.

%prep
%setup -q -n %{_orig_name}-%{version}

%build
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
%update_icon_cache hicolor

%postun
%scrollkeeper_update_post
%update_icon_cache hicolor

%files -f sensors-applet.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/sensors-applet
%{_libdir}/bonobo/servers/SensorsApplet.server
%{_iconsdir}/hicolor/*/*/sensors-*
%{_pixmapsdir}/sensors-applet
%{_datadir}/gnome-2.0/ui/SensorsApplet.xml
%dir %{_omf_dest_dir}/%{_orig_name}
%{_omf_dest_dir}/%{_orig_name}/*-C.omf
