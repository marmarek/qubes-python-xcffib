Name: python-xcffib
Version: 0.5.1
Release: 1%{?dist}
Url: https://github.com/tych0/xcffib
Summary: A drop in replacement for xpyb, an XCB python binding
License: Apache License 2.0
Group: Development/Languages/Python
Source: https://pypi.python.org/packages/48/e8/83dc668044f0393c5b7bea1afdf42bf25005ca067bb130db924f673261ad/xcffib-0.5.1.tar.gz

BuildArch: noarch
BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-pycparser
BuildRequires: libxcb-devel
BuildRequires: python-cffi >= 1.1.2
BuildRequires: python-six
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-pycparser
BuildRequires: python%{python3_pkgversion}-cffi >= 1.1.2
BuildRequires: python%{python3_pkgversion}-six
Requires: python-six
Requires: python-cffi >= 1.1.2
Requires: libxcb

%description
xcffib is intended to be a (mostly) drop-in replacement for xpyb.  xpyb
has an inactive upstream, several memory leaks, is python2 only and doesn't
have pypy support. xcffib is a binding which uses cffi, which mitigates
some of the issues described above. xcffib also builds bindings for 27 of
the 29 (xprint and xkb are missing) X extensions in 1.10.

%package -n python%{python3_pkgversion}-xcffib
Summary:	A drop in replacement for xpyb, an XCB python binding
Requires:	python%{python3_pkgversion}-six
Requires:  	python%{python3_pkgversion}-cffi >= 1.1.2

%description -n python%{python3_pkgversion}-xcffib
xcffib is intended to be a (mostly) drop-in replacement for xpyb.  xpyb
has an inactive upstream, several memory leaks, is python2 only and doesn't
have pypy support. xcffib is a binding which uses cffi, which mitigates
some of the issues described above. xcffib also builds bindings for 27 of
the 29 (xprint and xkb are missing) X extensions in 1.10.

%prep
%setup -q -n xcffib-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build

%install
%{__python2} setup.py install --root %{buildroot}
%{__python3} setup.py install --root %{buildroot}

%files
%doc LICENSE
%doc README.md
%{python2_sitelib}/xcffib
%{python2_sitelib}/xcffib*.egg-info

%files -n python%{python3_pkgversion}-xcffib
%doc LICENSE
%doc README.md
%{python3_sitelib}/xcffib
%{python3_sitelib}/xcffib*.egg-info

%changelog
