Summary:	Library for creating UPnP devices and control points
Name:		gupnp-dlna
Version:	0.10.2
Release:	2
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gupnp-dlna/0.10/%{name}-%{version}.tar.xz
# Source0-md5:	091f1ef019e0777f4409434018d3b3f3
URL:		http://www.gupnp.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gobject-introspection-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk-doc
BuildRequires:	gupnp-devel >= 0.20
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apiver	2.0

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

%package devel
Summary:	Header files for gupnp-dlna library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gupnp-dlna library.

%package apidocs
Summary:	gupnp-dlna library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API and internal documentation for gupnp-dlna library.

%prep
%setup -q

%build
%{__libtoolize}
%{__gtkdocize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/{,*/}*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gupnp-dlna-info-%{apiver}
%attr(755,root,root) %{_bindir}/gupnp-dlna-ls-profiles-%{apiver}
%attr(755,root,root) %ghost %{_libdir}/libgupnp-dlna-%{apiver}.so.?
%attr(755,root,root) %ghost %{_libdir}/libgupnp-dlna-gst-%{apiver}.so.?
%attr(755,root,root) %{_libdir}/libgupnp-dlna-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/libgupnp-dlna-gst-%{apiver}.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib
%{_datadir}/gupnp-dlna-%{apiver}

%dir %{_libdir}/gupnp-dlna
%attr(755,root,root) %{_libdir}/gupnp-dlna/libgstreamer.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi
%{_includedir}/gupnp-dlna-%{apiver}
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gupnp-dlna*

