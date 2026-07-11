%global tl_name fetchcls
%global tl_revision 45245

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Fetch the current class name
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fetchcls
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fetchcls.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fetchcls.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fetchcls.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
With standard LaTeX you are able to check for the class in use invoking
the kernel command \@ifclassloaded. However, doing so you cannot get the
explicit class name, unless you want to loop over every possible class
name until \@ifclassloaded returns true -- don't do that! With the help
of the present package you can obtain the name of the current class with
significantly less effort. Just load the package as usual:
\usepackage{fetchcls}; then, the control sequence \classname will hold
the name you were looking for.

