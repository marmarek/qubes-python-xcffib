%if 0%{?qubes_builder}
%define _sourcedir %(pwd)
%endif

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

%if 0%{?fedora} && ! 0%{?rhel}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pycparser
BuildRequires: python3-cffi >= 1.1.2
BuildRequires: python3-six
%endif

%if 0%{?rhel}
BuildRequires: python34-devel
BuildRequires: python34-setuptools
BuildRequires: python34-pycparser
BuildRequires: python34-cffi >= 1.1.2
BuildRequires: python34-six
%endif

Requires: python-six
Requires: python-cffi >= 1.1.2
Requires: libxcb

%description
xcffib is intended to be a (mostly) drop-in replacement for xpyb.  xpyb
has an inactive upstream, several memory leaks, is python2 only and doesn't
have pypy support. xcffib is a binding which uses cffi, which mitigates
some of the issues described above. xcffib also builds bindings for 27 of
the 29 (xprint and xkb are missing) X extensions in 1.10.

%if 0%{?fedora} && ! 0%{?rhel}
%package -n python3-xcffib
Summary:	A drop in replacement for xpyb, an XCB python binding
Requires:	python3-six
Requires:  	python3-cffi >= 1.1.2

%description -n python3-xcffib
xcffib is intended to be a (mostly) drop-in replacement for xpyb.  xpyb
has an inactive upstream, several memory leaks, is python2 only and doesn't
have pypy support. xcffib is a binding which uses cffi, which mitigates
some of the issues described above. xcffib also builds bindings for 27 of
the 29 (xprint and xkb are missing) X extensions in 1.10.
%endif

%if 0%{?rhel} 
%package -n python34-xcffib
Summary:	A drop in replacement for xpyb, an XCB python binding
Requires:	python34-six
Requires:  	python34-cffi >= 1.1.2

%description -n python34-xcffib
xcffib is intended to be a (mostly) drop-in replacement for xpyb.  xpyb
has an inactive upstream, several memory leaks, is python2 only and doesn't
have pypy support. xcffib is a binding which uses cffi, which mitigates
some of the issues described above. xcffib also builds bindings for 27 of
the 29 (xprint and xkb are missing) X extensions in 1.10.
%endif

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

%if 0%{?fedora} && ! 0%{?rhel}
%files -n python3-xcffib
%doc LICENSE
%doc README.md
%{python3_sitelib}/xcffib
%{python3_sitelib}/xcffib*.egg-info
%endif

%if 0%{?rhel}
%files -n python34-xcffib
%doc LICENSE
%doc README.md
%{python3_sitelib}/xcffib
%{python3_sitelib}/xcffib*.egg-info
%endif

%changelog
