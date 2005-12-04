Summary:	Xxf86dga library
Summary(pl):	Biblioteka Xxf86dga
Name:		xorg-lib-libXxf86dga
Version:	0.99.3
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/lib/libXxf86dga-%{version}.tar.bz2
# Source0-md5:	0f70bbf4d8d9477002a5295952643504
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xxf86dga library.

%description -l pl
Biblioteka Xxf86dga.

%package devel
Summary:	Header files for libXxf86dga library
Summary(pl):	Pliki nagłówkowe biblioteki libXxf86dga
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-xf86dgaproto-devel

%description devel
Xxf86dga library.

This package contains the header files needed to develop programs that
use libXxf86dga.

%description devel -l pl
Biblioteka Xxf86dga.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXxf86dga.

%package static
Summary:	Static libXxf86dga library
Summary(pl):	Biblioteka statyczna libXxf86dga
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXxf86dga.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXxf86dga.so
%{_libdir}/libXxf86dga.la
%{_pkgconfigdir}/xxf86dga.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXxf86dga.a
