Name:		texlive-zhnumber
Version:	2.5
Release:	1
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
%{_texmfdistdir}/tex/latex/zhnumber
%doc %{_texmfdistdir}/doc/latex/zhnumber
#- source
%doc %{_texmfdistdir}/source/latex/zhnumber

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
