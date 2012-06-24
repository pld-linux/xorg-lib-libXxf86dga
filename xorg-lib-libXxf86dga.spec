Summary:	Xxf86dga library
Summary(pl):	Biblioteka Xxf86dga
Name:		xorg-lib-libXxf86dga
Version:	1.0.0
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC4/lib/libXxf86dga-%{version}.tar.bz2
# Source0-md5:	424ec894a76968aaab1a2c09760e272a
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
Summary(pl):	Pliki nag��wkowe biblioteki libXxf86dga
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

Pakiet zawiera pliki nag��wkowe niezb�dne do kompilowania program�w
u�ywaj�cych biblioteki libXxf86dga.

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

Pakiet zawiera statyczn� bibliotek� libXxf86dga.

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
