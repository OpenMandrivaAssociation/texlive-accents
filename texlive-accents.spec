Name:		texlive-accents
Version:	51497
Release:	2
Summary:	Multiple mathematical accents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/accents
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/accents.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/accents.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for multiple accents in mathematics, with nice
features concerning the creation of accents and placement of
scripts.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/accents
%doc %{_texmfdistdir}/doc/latex/accents

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
