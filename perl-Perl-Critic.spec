#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Perl
%define	pnam	Critic
Summary:	Perl::Critic - Critique Perl source code for best-practices
Summary(pl.UTF-8):	Perl::Critic - krytyka kodu źródłowego w Perla pod kątem najlepszych praktyk
Name:		perl-Perl-Critic
Version:	1.105
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	25915a2e00784a7e3b94d6ffaaf20b22
URL:		http://search.cpan.org/dist/Perl-Critic/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-B-Keywords >= 1.05
BuildRequires:	perl-Config-Tiny >= 2
BuildRequires:	perl-Exception-Class >= 1.23
BuildRequires:	perl-IO-String
BuildRequires:	perl-List-MoreUtils >= 0.19
BuildRequires:	perl-Module-Pluggable >= 3.1
BuildRequires:	perl-PPI >= 1.205
BuildRequires:	perl-Readonly
BuildRequires:	perl-Set-Scalar >= 1.20
BuildRequires:	perl-String-Format >= 1.13
%endif
Requires:	perl-Config-Tiny >= 2
Requires:	perl-Module-Pluggable >= 3.1
Requires:	perl-PPI >= 1.118
Requires:	perl-Set-Scalar >= 1.20
Requires:	perl-String-Format >= 1.13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Perl::Critic.*)'
%description
Perl::Critic is an extensible framework for creating and applying
coding standards to Perl source code. Essentially, it is a static
source code analysis engine. Perl::Critic is distributed with a
number of Perl::Critic::Policy modules that attempt to enforce
various coding guidelines. Most Policy modules are based on Damian
Conway's book Perl Best Practices. However, Perl::Critic is not
limited to PBP and will even support Policies that contradict Conway.
You can enable, disable, and customize those Polices through the
Perl::Critic interface. You can also create new Policy modules that
suit your own tastes.

%description -l pl.UTF-8
Perl::Critic to rozszerzalny szkielet do tworzenia i nanoszenia
standardów kodowania dla kodu źródłowego w Perlu. Zasadniczo jest to
statyczny silnik do analizy kodu źródłowego. Perl::Critic jest
rozpowszechniany z wieloma modułami Perl::Critic::Policy, próbującymi
wymusić różne wskazania dotyczące kodowania. Większość modułów Policy
jest oparta na książce "Perl Best Practices" Damiana Conwaya. Jednak
Perl::Critic nie jest ograniczony do PDB i będzie obsługiwał polityki
nawet niezgodne z Conwayem. Poprzez interfejs Perl::Critic można
włączać, wyłączać i dostrajać polityki. Można także tworzyć nowe
moduły Policy odpowiadające własnym gustom.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Perl/Critic/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes extras
%attr(755,root,root) %{_bindir}/perlcritic
%dir %{perl_vendorlib}/Perl
%{perl_vendorlib}/Perl/Critic.pm
%{perl_vendorlib}/Perl/Critic
%{_mandir}/man1/perlcritic.1*
%{_mandir}/man3/Perl::Critic*
