#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Perl
%define	pnam	Critic
Summary:	Perl::Critic - Critique Perl source code for best-practices
Summary(pl):	Perl::Critic - krytyka kodu ¼ród³owego w Perla pod k±tem najlepszych praktyk
Name:		perl-Perl-Critic
Version:	0.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8c4a32c603916a82c106804659bb7518
URL:		http://search.cpan.org/dist/Perl-Critic/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Config-Tiny >= 2
BuildRequires:	perl-IO-String
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Module-Pluggable >= 3.1
BuildRequires:	perl-PPI >= 1.118
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

%description -l pl
Perl::Critic to rozszerzalny szkielet do tworzenia i nanoszenia
standardów kodowania dla kodu ¼ród³owego w Perlu. Zasadniczo jest to
statyczny silnik do analizy kodu ¼ród³owego. Perl::Critic jest
rozpowszechniany z wieloma modu³ami Perl::Critic::Policy, próbuj±cymi
wymusiæ ró¿ne wskazania dotycz±ce kodowania. Wiêkszo¶æ modu³ów Policy
jest oparta na ksi±¿ce "Perl Best Practices" Damiana Conwaya. Jednak
Perl::Critic nie jest ograniczony do PDB i bêdzie obs³ugiwa³ polityki
nawet niezgodne z Conwayem. Poprzez interfejs Perl::Critic mo¿na
w³±czaæ, wy³±czaæ i dostrajaæ polityki. Mo¿na tak¿e tworzyæ nowe
modu³y Policy odpowiadaj±ce w³asnym gustom.

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
%{perl_vendorlib}/Perl/Critic.pm
%{perl_vendorlib}/Perl/Critic
%{_mandir}/man1/perlcritic.1*
%{_mandir}/man3/Perl::Critic*
