#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycryptodomex
Version  : 3.9.8
Release  : 3
URL      : https://files.pythonhosted.org/packages/f5/79/9d9206688385d1e7a5ff925e7aab1d685636256e34a409037aa7adbbe611/pycryptodomex-3.9.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/f5/79/9d9206688385d1e7a5ff925e7aab1d685636256e34a409037aa7adbbe611/pycryptodomex-3.9.8.tar.gz
Summary  : Cryptographic library for Python
Group    : Development/Tools
License  : Apache-2.0 Python-2.0
Requires: pycryptodomex-license = %{version}-%{release}
Requires: pycryptodomex-python = %{version}-%{release}
Requires: pycryptodomex-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
PyCryptodome
        ============
        
        PyCryptodome is a self-contained Python package of low-level
        cryptographic primitives.
        
        It supports Python 2.6 and 2.7, Python 3.4 and newer, and PyPy.

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
%setup -q -n pycryptodomex-3.9.8
cd %{_builddir}/pycryptodomex-3.9.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1593714154
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pycryptodomex
cp %{_builddir}/pycryptodomex-3.9.8/Doc/LEGAL/copy/LICENSE.python-2.2 %{buildroot}/usr/share/package-licenses/pycryptodomex/e2e326a9a73b4a86d3aa275bb1b9797ab1f047b7
cp %{_builddir}/pycryptodomex-3.9.8/LICENSE.rst %{buildroot}/usr/share/package-licenses/pycryptodomex/9d06d2f12955e69e3c7e9f53538abd61e9354ac9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pycryptodomex/9d06d2f12955e69e3c7e9f53538abd61e9354ac9
/usr/share/package-licenses/pycryptodomex/e2e326a9a73b4a86d3aa275bb1b9797ab1f047b7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
