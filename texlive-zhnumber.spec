# revision 28347
# category Package
# catalog-ctan /macros/latex/contrib/zhnumber
# catalog-date 2012-11-24 00:28:04 +0100
# catalog-license lppl1.3
# catalog-version 1.6
Name:		texlive-zhnumber
Version:	1.6
Release:	3
Summary:	Typeset Chinese representations of numbers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zhnumber
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zhnumber.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zhnumber.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zhnumber.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands to typeset Chinese
representations of numbers. The main difference between this
package and CJKnumb is that the commands provided are
expandable in the 'proper' way.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/zhnumber/config/zhnumber-big5.cfg
%{_texmfdistdir}/tex/latex/zhnumber/config/zhnumber-gbk.cfg
%{_texmfdistdir}/tex/latex/zhnumber/config/zhnumber-utf8.cfg
%{_texmfdistdir}/tex/latex/zhnumber/zhnumber.sty
%doc %{_texmfdistdir}/doc/latex/zhnumber/README
%doc %{_texmfdistdir}/doc/latex/zhnumber/zhnumber.pdf
#- source
%doc %{_texmfdistdir}/source/latex/zhnumber/zhnumber.dtx
%doc %{_texmfdistdir}/source/latex/zhnumber/zhnumber.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
