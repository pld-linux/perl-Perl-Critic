#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Perl
%define	pnam	Critic
Summary:	Perl::Critic - Critique Perl source code for best-practices
Summary(pl.UTF-8):	Perl::Critic - krytyka kodu źródłowego w Perla pod kątem najlepszych praktyk
Name:		perl-Perl-Critic
Version:	1.132
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	76042c0516190419e0424f10366231ae
URL:		http://search.cpan.org/dist/Perl-Critic/
BuildRequires:	perl-B-Keywords >= 1.05
BuildRequires:	perl-List-MoreUtils >= 0.19
BuildRequires:	perl-Module-Build >= 0.4200
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.63
BuildRequires:	perl-Config-Tiny >= 2
BuildRequires:	perl-Email-Address >= 1.889
BuildRequires:	perl-Exception-Class >= 1.23
BuildRequires:	perl-IO-String
BuildRequires:	perl-Module-Pluggable >= 3.1
BuildRequires:	perl-PPI >= 1.224
BuildRequires:	perl-PPIx-Regexp >= 0.027
BuildRequires:	perl-PPIx-Utilities >= 1.001
BuildRequires:	perl-PPIx-QuoteLike
BuildRequires:	perl-PadWalker
BuildRequires:	perl-Pod-Spell >= 1
BuildRequires:	perl-Readonly >= 2.00
BuildRequires:	perl-String-Format >= 1.13
BuildRequires:	perl-Task-Weaken
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Memory-Cycle
BuildRequires:	perl-Test-Simple >= 0.92
BuildRequires:	perl-version >= 0.77
BuildRequires:	perltidy
%endif
Requires:	perl(Exporter) >= 5.63
Requires:	perl-B-Keywords >= 1.05
Requires:	perl-Config-Tiny >= 2
Requires:	perl-Email-Address >= 1.889
Requires:	perl-Exception-Class >= 1.23
Requires:	perl-List-MoreUtils >= 0.19
Requires:	perl-Module-Pluggable >= 3.1
Requires:	perl-PPI >= 1.220
Requires:	perl-PPIx-Regexp >= 0.027
Requires:	perl-PPIx-Utilities >= 1.001
Requires:	perl-Readonly >= 2.00
Requires:	perl-String-Format >= 1.13
Requires:	perl-dirs >= 4-4
Requires:	perl-version >= 0.77
Suggests:	perl-Term-ANSIColor >= 2.02
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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Perl/Critic/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md TODO.pod extras
%attr(755,root,root) %{_bindir}/perlcritic
%{perl_vendorlib}/Perl/Critic.pm
%{perl_vendorlib}/Perl/Critic
%dir %{perl_vendorlib}/Test/Perl/Critic
%{perl_vendorlib}/Test/Perl/Critic/Policy.pm
%{_mandir}/man1/perlcritic.1*
%{_mandir}/man3/Perl::Critic*.3pm*
%{_mandir}/man3/Test::Perl::Critic::Policy.3pm*
