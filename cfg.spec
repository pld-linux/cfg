# TODO: resolve conflict with libcfg+-devel - header files
#	has the same name.
# NOTE: API is NOT documented
Summary:	OSSP cfg - Configuration Parsing
Summary(pl):	OSSP cfg - parsowanie konfiguracji
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
BuildRequires:	flex	
BuildRequires:	libtool
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

%description -l pl
OSSP cfg to biblioteka ISO-C do parsowania dowolnych plików
konfiguracyjnych w stylu C/C++. Konfiguracja jest sekwencj± dyrektyw.
Ka¿da dyrektywa zawiera zero lub wiêcej tokenów. Ka¿dy token mo¿e byæ
³añcuchem albo znowu ca³± sekwencj±. Oznacza to, ¿e sk³adnia
konfiguracji ma strukturê rekurencyjn±, co pozwala tworzyæ
konfiguracje z dowolnie zagnie¿d¿onymi sekcjami.

Sk³adnia konfiguracji udostêpnia dodatkowo z³o¿one
pojedyncze/podwójne/zrównowa¿one cytowanie tokenów,
szesnastkowe/ósemkowe/dziesiêtne kodowanie znaków, cytowanie znaków,
komentarze w stylu C/C++ i pow³oki itp. API biblioteki umo¿liwia
importowanie tekstu konfiguracji do abstrakcyjnych drzew sk³adniowych
(AST), przechodzenie po AST i opcjonalnie eksportowanie AST z powrotem
do tekstu konfiguracji.

%package devel
Summary:	OSSP cfg - Configuration Parsing - header files and development libraries
Summary(pl):	OSSP cfg - parsowanie konfiguracji - pliki nag³ówkowe i biblioteki dla deweloperów
Group:		Development/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description devel
OSSP cfg - Configuration Parsing - header files and development
libraries.

%description devel -l pl
OSSP cfg - parsowanie konfiguracji - pliki nag³ówkowe i biblioteki dla
deweloperów.

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
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
