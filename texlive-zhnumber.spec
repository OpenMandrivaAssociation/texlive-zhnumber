%global tl_name zhnumber
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0
Release:	%{tl_revision}.1
Summary:	Typeset Chinese representations of numbers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/zhnumber
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zhnumber.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zhnumber.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zhnumber.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands to typeset Chinese representations of
numbers. The main difference between this package and CJKnumb is that
the commands provided are expandable in the 'proper' way.

