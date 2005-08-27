# $Rev: 3322 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	Xxf86dga library
Summary(pl):	Biblioteka Xxf86dga
Name:		xorg-lib-libXxf86dga
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXxf86dga-%{version}.tar.bz2
# Source0-md5:	ca59bc212086501c762f54333182c219
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRoot:	%{tmpdir}/libXxf86dga-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xxf86dga library.

%description -l pl
Biblioteka Xxf86dga.


%package devel
Summary:	Header files libXxf86dga development
Summary(pl):	Pliki nagłówkowe do biblioteki libXxf86dga
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXxf86dga = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-xf86dgaproto-devel

%description devel
Xxf86dga library.

This package contains the header files needed to develop programs that
use these libXxf86dga.

%description devel -l pl
Biblioteka Xxf86dga.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXxf86dga.


%package static
Summary:	Static libXxf86dga libraries
Summary(pl):	Biblioteki statyczne libXxf86dga
Group:		Development/Libraries
Requires:	xorg-lib-libXxf86dga-devel = %{version}-%{release}

%description static
Xxf86dga library.

This package contains the static libXxf86dga library.

%description static -l pl
Biblioteka Xxf86dga.

Pakiet zawiera statyczną bibliotekę libXxf86dga.


%prep
%setup -q -n libXxf86dga-%{version}


%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}


%clean
rm -rf $RPM_BUILD_ROOT


%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,wheel) %{_libdir}/libXxf86dga.so.*


%files devel
%defattr(644,root,root,755)
%{_libdir}/libXxf86dga.la
%attr(755,root,wheel) %{_libdir}/libXxf86dga.so
%{_pkgconfigdir}/xxf86dga.pc
%{_mandir}/man3/*.3*


%files static
%defattr(644,root,root,755)
%{_libdir}/libXxf86dga.a
