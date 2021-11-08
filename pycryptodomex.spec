#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycryptodomex
Version  : 3.11.0
Release  : 19
URL      : https://files.pythonhosted.org/packages/47/14/dd9ad29cd29ea4cc521286f2cb401ca7ac6fd5db0791c5e9bacaf2c9ac78/pycryptodomex-3.11.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/47/14/dd9ad29cd29ea4cc521286f2cb401ca7ac6fd5db0791c5e9bacaf2c9ac78/pycryptodomex-3.11.0.tar.gz
Summary  : Cryptographic library for Python
Group    : Development/Tools
License  : Python-2.0 Unlicense
Requires: pycryptodomex-license = %{version}-%{release}
Requires: pycryptodomex-python = %{version}-%{release}
Requires: pycryptodomex-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
PyCryptodome
        ============
        
        PyCryptodome is a self-contained Python package of low-level
        cryptographic primitives.
        
        It supports Python 2.7, Python 3.5 and newer, and PyPy.

%package license
Summary: license components for the pycryptodomex package.
Group: Default

%description license
license components for the pycryptodomex package.


%package python
Summary: python components for the pycryptodomex package.
Group: Default
Requires: pycryptodomex-python3 = %{version}-%{release}

%description python
python components for the pycryptodomex package.


%package python3
Summary: python3 components for the pycryptodomex package.
Group: Default
Requires: python3-core
Provides: pypi(pycryptodomex)

%description python3
python3 components for the pycryptodomex package.


%prep
%setup -q -n pycryptodomex-3.11.0
cd %{_builddir}/pycryptodomex-3.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636413593
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pycryptodomex
cp %{_builddir}/pycryptodomex-3.11.0/Doc/LEGAL/copy/LICENSE.python-2.2 %{buildroot}/usr/share/package-licenses/pycryptodomex/e2e326a9a73b4a86d3aa275bb1b9797ab1f047b7
cp %{_builddir}/pycryptodomex-3.11.0/LICENSE.rst %{buildroot}/usr/share/package-licenses/pycryptodomex/6738e7ba3da8371457774d36ee2fbca80f9cca5e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pycryptodomex/6738e7ba3da8371457774d36ee2fbca80f9cca5e
/usr/share/package-licenses/pycryptodomex/e2e326a9a73b4a86d3aa275bb1b9797ab1f047b7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
