# TODO: resolve conflict with libcfg+-devel - header files
#	has the same name.
# NOTE: API is NOT documented
Summary:	OSSP cfg - Configuration Parsing
Summary(pl):	OSSP cfg - parsowanie konfiguracji.
Name:		cfg
Version:	0.9.4
Release:	0.1
License:	distributable (see README)
Group:		Libraries
Source0:	ftp://ftp.ossp.org/pkg/lib/cfg/%{name}-%{version}.tar.gz
# Source0-md5:	a41ac64a92a55030f44e307cc5461657
URL:		http://www.ossp.org/pkg/lib/cfg/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex	
BuildRequires:	libtool
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSSP cfg is a ISO-C library for parsing arbitrary C/C++-style
configuration files. A configuration is sequence of directives. Each
directive consists of zero or more tokens. Each token can be either a
string or again a complete sequence. This means the configuration
syntax has a recursive structure and this way allows to create
configurations with arbitrarily nested sections.

Additionally the configuration syntax provides complex
single/double/balanced quoting of tokens, hexadecimal/octal/decimal
character encodings, character escaping, C/C++ and Shell-style
comments, etc. The library API allows importing a configuration text
into an Abstract Syntax Tree (AST), traversing the AST and optionally
exporting the AST again as a configuration text.

#%%description -l pl
# I need API documentation instead pl description.

%package devel
Summary:	OSSP cfg - Configuration Parsing - header files and development libraries
Summary(pl):	OSSP cfg - parsowanie konfiguracji - pliki nag��wkowe i biblioteki dla deweloper�w
Group:		Development/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description devel
OSSP cfg - Configuration Parsing - header files and development
libraries.

%description devel -l pl
OSSP cfg - parsowanie konfiguracji - pliki nag��wkowe i biblioteki dla
deweloper�w.

%package static
Summary:	OSSP cfg - Configuration Parsing - static libraries
Summary(pl):	OSSP cfg - parsowanie konfiguracji - biblioteki statyczne
Group:		Development/Libraries
Requires:       %{name}-devel = %{epoch}:%{version}-%{release}

%description static
OSSP cfg - Configuration Parsing - static libraries.

%description static -l pl
OSSP cfg - parsowanie konfiguracji - biblioteki statyczne.

%prep
%setup -q

%build
mv -f aclocal.m4 acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING README THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a