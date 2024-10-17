%define rname haskell-mode

Summary: Major mode for editing Haskell code with emacs
Name:    emacs-haskell-mode
Version: 2.4
Release: 2
Source0: http://www.iro.umontreal.ca/~monnier/elisp/haskell-mode-%{version}.tar.gz
License: GPL
Group: Development/Other
BuildArch: noarch
BuildRequires: emacs
Url: https://haskell.org/haskell-mode/

%description
Haskell Mode for Emacs

%prep
%setup -q -n %{rname}-%{version}

%build
make

%install
# NB: prefering .el files (so that it's version independant)
install -d %buildroot%{_datadir}/emacs/site-lisp
install -m644 *.el %buildroot%_datadir/emacs/site-lisp

install -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
cat <<EOF >%{buildroot}%{_sysconfdir}/emacs/site-start.d/%{rname}.el
(load "%{_datadir}/emacs/site-lisp/haskell-site-file")
;(add-hook 'haskell-mode-hook 'turn-on-haskell-decl-scan)
;(add-hook 'haskell-mode-hook 'turn-on-haskell-hugs)
EOF


%files
%doc NEWS
%config(noreplace) /etc/emacs/site-start.d/%{rname}.el
%_datadir/*/site-lisp/*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1-6mdv2011.0
+ Revision: 618050
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 2.1-5mdv2010.0
+ Revision: 428559
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.1-4mdv2009.0
+ Revision: 244701
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 2.1-2mdv2008.1
+ Revision: 132849
- BR emacs
- kill re-definition of %%buildroot on Pixel's request
- import emacs-haskell-mode


* Mon Dec  5 2005 Pixel <pixel@mandriva.com> 2.1-2mdk
- fix loading

* Mon Nov 28 2005 Pixel <pixel@mandriva.com> 2.1-1mdk
- first package

