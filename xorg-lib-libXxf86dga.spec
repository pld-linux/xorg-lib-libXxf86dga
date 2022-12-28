Summary:	XFree86-DGA extension client library
Summary(pl.UTF-8):	Biblioteka kliencka rozszerzenia XFree86-DGA
Name:		xorg-lib-libXxf86dga
Version:	1.1.6
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXxf86dga-%{version}.tar.xz
# Source0-md5:	74d1acf93b83abeb0954824da0ec400b
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel >= 1.6
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel >= 2.0.99.2
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libX11 >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XFree86-DGA (Direct Graphics Access) extension client library.

%description -l pl.UTF-8
Biblioteka kliencka rozszerzenia XFree86-DGA (Direct Graphics Access -
bezpośredniego dostępu do grafiki).

%package devel
Summary:	Header files for libXxf86dga library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXxf86dga
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel >= 1.6
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-xf86dgaproto-devel >= 2.0.99.2

%description devel
This package contains the header files needed to develop programs that
use libXxf86dga.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXxf86dga.

%package static
Summary:	Static libXxf86dga library
Summary(pl.UTF-8):	Biblioteka statyczna libXxf86dga
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static libXxf86dga library.

%description static -l pl.UTF-8
Pakiet zawiera statyczną bibliotekę libXxf86dga.

%prep
%setup -q -n libXxf86dga-%{version}

# support __libmansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,\.so man__libmansuffix__/,.so man3/,' man/*.man

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
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libXxf86dga.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXxf86dga.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXxf86dga.so
%{_includedir}/X11/extensions/Xxf86dga.h
%{_includedir}/X11/extensions/xf86dga1.h
%{_pkgconfigdir}/xxf86dga.pc
%{_mandir}/man3/XDGA*.3*
%{_mandir}/man3/XF86DGA.3*
%{_mandir}/man3/XFree86-DGA.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXxf86dga.a
