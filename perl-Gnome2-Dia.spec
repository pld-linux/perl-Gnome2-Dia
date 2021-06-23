#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%define		pdir	Gnome2
%define		pnam	Dia
Summary:	Perl interface to DiaCanvas2 library
Summary(pl.UTF-8):	Interfejs perlowy do biblioteki DiaCanvas2
Name:		perl-Gnome2-Dia
Version:	0.06
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	https://downloads.sourceforge.net/gtk2-perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f60fdf94b751f56eb50abf92222e0a9b
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	diacanvas-devel >= 0.13.0
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= 1.040
BuildRequires:	perl-Gnome2-Canvas >= 1.000
BuildRequires:	perl-Gnome2-Print >= 0.94
BuildRequires:	perl-Gtk2 >= 1.040
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	diacanvas >= 0.13.0
Requires:	perl-Glib >= 1.144
Requires:	perl-Gnome2-Canvas >= 1.000
Requires:	perl-Gnome2-Print >= 0.94
Requires:	perl-Gtk2 >= 1.144
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows a Perl developer to use the DiaCanvas2 library to
create all kinds of spiffy diagramming tools.

Note: this module is deprecated and no longer maintained.

%description -l pl.UTF-8
Ten moduł pozwala programistom perlowym używać biblioteki DiaCanvas2
do tworzenia wszelkiego rodzaju narzędzi z diagramami.

Uwaga: ten moduł jest przestarzały i nie jest już utrzymywany.

%package devel
Summary:	Development files for Perl Gnome2-Dia bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Gnome2-Dia dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	diacanvas-devel >= 0.13.0
Requires:	perl-Cairo-devel
Requires:	perl-Glib-devel >= 1.120
Requires:	perl-Gtk2-devel >= 1.121

%description devel
Development files for Perl Gnome2-Dia bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Gnome2-Dia dla Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/Dia/*.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/Dia/{Event,Export,Shape}/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%{perl_vendorarch}/Gnome2/Dia.pm
%dir %{perl_vendorarch}/Gnome2/Dia
%dir %{perl_vendorarch}/auto/Gnome2/Dia
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Dia/Dia.so
%{_mandir}/man3/Gnome2::Dia*.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Gnome2/Dia/Install
