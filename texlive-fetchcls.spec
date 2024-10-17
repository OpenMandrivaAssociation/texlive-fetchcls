Name:		texlive-fetchcls
Version:	45245
Release:	2
Summary:	Fetch the current class name
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fetchcls
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fetchcls.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fetchcls.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fetchcls.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
With standard LaTeX you are able to check for the class in use
invoking the kernel command \@ifclassloaded. However, doing so
you cannot get the explicit class name, unless you want to loop
over every possible class name until \@ifclassloaded returns
true -- don't do that! With the help of the present package you
can obtain the name of the current class with significantly
less effort. Just load the package as usual:
\usepackage{fetchcls}; then, the control sequence \classname
will hold the name you were looking for.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fetchcls
%{_texmfdistdir}/tex/latex/fetchcls
%doc %{_texmfdistdir}/doc/latex/fetchcls

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
