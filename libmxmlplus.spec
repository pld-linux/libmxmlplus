Summary:	Minimal XML library for C++
Summary(pl.UTF-8):	Minimalna biblioteka XML dla C++
Name:		libmxmlplus
Version:	0.9.2
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://downloads.sourceforge.net/mxml/%{name}-%{version}.tar.gz
# Source0-md5:	562b3aedaa78a16bf963f43327566e6a
Patch0:		%{name}-ac.patch
Patch1:		%{name}-c++.patch
URL:		http://mxml.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minimal XML is a library meant for extrememly fast and non-validating
XML parsing.

%description -l pl.UTF-8
Minimal XML jest biblioteką z przeznaczeniem do ekstremalnie szybkiej
analizy XML bez kontroli poprawności.

%package devel
Summary:	Header files for libmxmlplus
Summary(pl.UTF-8):	Pliki nagłówkowe dla libmxmlplus
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for libmxmlplus.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libmxmlplus.

%package static
Summary:	Static libmxmlplus library
Summary(pl.UTF-8):	Statyczna biblioteka libmxmlplus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmxmlplus library.

%description static -l pl.UTF-8
Statyczna biblioteka libmxmlplus.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# use include subdir to avoid conflicts with libmxml or mxml
%configure \
	--includedir=%{_includedir}/mxmlplus \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS RELNOTES TODO
%attr(755,root,root) %{_libdir}/libmxmlplus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmxmlplus.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmxmlplus.so
%{_libdir}/libmxmlplus.la
%{_includedir}/mxmlplus

%files static
%defattr(644,root,root,755)
%{_libdir}/libmxmlplus.a
