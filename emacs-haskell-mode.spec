%define rname haskell-mode
%define name emacs-haskell-mode
%define version 2.1
%define release %mkrel 6

Summary: Major mode for editing Haskell code with emacs
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.iro.umontreal.ca/~monnier/elisp/haskell-mode-2.1.tar.bz2
License: GPL
Group: Development/Other
BuildArch: noarch
BuildRequires: emacs
Url: http://haskell.org/haskell-mode/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Haskell Mode for Emacs

%prep
%setup -q -n %{rname}-%{version}

%build
make

%install
rm -rf $RPM_BUILD_ROOT

# NB: prefering .el files (so that it's version independant)
install -d %buildroot%{_datadir}/emacs/site-lisp
install -m644 *.el %buildroot%_datadir/emacs/site-lisp

install -d $RPM_BUILD_ROOT%{_sysconfdir}/emacs/site-start.d
cat <<EOF >$RPM_BUILD_ROOT%{_sysconfdir}/emacs/site-start.d/%{rname}.el
(load "%_datadir/emacs/site-lisp/haskell-site-file")
;(add-hook 'haskell-mode-hook 'turn-on-haskell-decl-scan)
;(add-hook 'haskell-mode-hook 'turn-on-haskell-hugs)
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc index.html NEWS
%config(noreplace) /etc/emacs/site-start.d/%{rname}.el
%_datadir/*/site-lisp/*


