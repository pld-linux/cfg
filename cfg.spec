# TODO: 1. Resolve conflict with libcfg+-devel - header files
#	   as the same name.
#	2. Fix refreshing configure.
# NOTE: Lack of C API documentation in manpage
#
# Conditional builds:
%bcond_with	ex	# build with external OSSP ex library
%bcond_without	perl	# build Perl bindings to C API
#
Summary:	OSSP cfg - Configuration Parsing
Summary(pl.UTF-8):   OSSP cfg - parsowanie konfiguracji
Name:		cfg
Version:	0.9.9
Release:	0.1
Epoch:		0
License:	distributable (see README)
Group:		Libraries
Source0:	ftp://ftp.ossp.org/pkg/lib/cfg/%{name}-%{version}.tar.gz
# Source0-md5:	66576d4d4ee01b29666aa19aaa3faa71
URL:		http://www.ossp.org/pkg/lib/cfg/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
%{?with_ex:BuildRequires:	ex-devel}
BuildRequires:	flex
BuildRequires:	libtool
%{?with_perl:BuildRequires:	perl-devel}
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

%description -l pl.UTF-8
OSSP cfg to biblioteka ISO-C do parsowania dowolnych plików
konfiguracyjnych w stylu C/C++. Konfiguracja jest sekwencją dyrektyw.
Każda dyrektywa zawiera zero lub więcej tokenów. Każdy token może być
łańcuchem albo znowu całą sekwencją. Oznacza to, że składnia
konfiguracji ma strukturę rekurencyjną, co pozwala tworzyć
konfiguracje z dowolnie zagnieżdżonymi sekcjami.

Składnia konfiguracji udostępnia dodatkowo złożone
pojedyncze/podwójne/zrównoważone cytowanie tokenów,
szesnastkowe/ósemkowe/dziesiętne kodowanie znaków, cytowanie znaków,
komentarze w stylu C/C++ i powłoki itp. API biblioteki umożliwia
importowanie tekstu konfiguracji do abstrakcyjnych drzew składniowych
(AST), przechodzenie po AST i opcjonalnie eksportowanie AST z powrotem
do tekstu konfiguracji.

%package devel
Summary:	OSSP cfg - Configuration Parsing - header files and development libraries
Summary(pl.UTF-8):   OSSP cfg - parsowanie konfiguracji - pliki nagłówkowe i biblioteki dla deweloperów
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
OSSP cfg - Configuration Parsing - header files and development
libraries.

%description devel -l pl.UTF-8
OSSP cfg - parsowanie konfiguracji - pliki nagłówkowe i biblioteki dla
deweloperów.

%package static
Summary:	OSSP cfg - Configuration Parsing - static libraries
Summary(pl.UTF-8):   OSSP cfg - parsowanie konfiguracji - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
OSSP cfg - Configuration Parsing - static libraries.

%description static -l pl.UTF-8
OSSP cfg - parsowanie konfiguracji - biblioteki statyczne.

%package -n perl-cfg
Summary:	OSSP cfg - Configuration Parsing - Perl bindings
Summary(pl.UTF-8):   OSSP cfg - parsowanie konfiguracji - dowiązania Perla
Group:		Development/Languages/Perl

%description -n perl-cfg
OSSP cfg - Configuration Parsing - Perl bindings to C API.

%description -n perl-cfg -l pl.UTF-8
OSSP cfg - parsowanie konfiguracji - dowiązania Perla do API C.

%prep
%setup -q

%build
# don't uncomment what is commented out below -
# - since v0.9.7 it doesn't work
#mv -f aclocal.m4 acinclude.m4
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
%configure \
	%{?with_ex:--with-ex} \
	%{?with_perl:--with-perl}

%{__make}

%if %{with_perl}
cd perl
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLDIRS=vendor

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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
%{_mandir}/man3/cfg.3*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a

%files -n perl-cfg
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/OSSP
%{perl_vendorarch}/OSSP/cfg.pm
%dir %{perl_vendorarch}/auto/OSSP
%dir %{perl_vendorarch}/auto/OSSP/cfg
%{perl_vendorarch}/auto/OSSP/cfg/cfg.bs
%attr(755,root,root) %{perl_vendorarch}/auto/OSSP/cfg/cfg.so
%{_mandir}/man3/OSSP::cfg.3pm*
