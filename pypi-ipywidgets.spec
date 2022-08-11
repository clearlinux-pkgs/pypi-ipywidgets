#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ipywidgets
Version  : 7.7.1
Release  : 72
URL      : https://files.pythonhosted.org/packages/05/25/e29e5bffcc09710dd3ddf7c50a73697c0a822cbf23983ec5b874019353f2/ipywidgets-7.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/05/25/e29e5bffcc09710dd3ddf7c50a73697c0a822cbf23983ec5b874019353f2/ipywidgets-7.7.1.tar.gz
Summary  : Interactive HTML widgets for Jupyter notebooks
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-ipywidgets-license = %{version}-%{release}
Requires: pypi-ipywidgets-python = %{version}-%{release}
Requires: pypi-ipywidgets-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
ipywidgets, also known as jupyter-widgets or simply widgets, are interactive
HTML widgets for Jupyter notebooks and the IPython kernel.

%package license
Summary: license components for the pypi-ipywidgets package.
Group: Default

%description license
license components for the pypi-ipywidgets package.


%package python
Summary: python components for the pypi-ipywidgets package.
Group: Default
Requires: pypi-ipywidgets-python3 = %{version}-%{release}

%description python
python components for the pypi-ipywidgets package.


%package python3
Summary: python3 components for the pypi-ipywidgets package.
Group: Default
Requires: python3-core
Provides: pypi(ipywidgets)
Requires: pypi(ipykernel)
Requires: pypi(ipython)
Requires: pypi(ipython_genutils)
Requires: pypi(jupyterlab_widgets)
Requires: pypi(traitlets)
Requires: pypi(widgetsnbextension)

%description python3
python3 components for the pypi-ipywidgets package.


%prep
%setup -q -n ipywidgets-7.7.1
cd %{_builddir}/ipywidgets-7.7.1
pushd ..
cp -a ipywidgets-7.7.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655937318
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

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ipywidgets
cp %{_builddir}/ipywidgets-7.7.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ipywidgets/5dc7e0ef3878c3d4a92a7233208e6f91553de266
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ipywidgets/5dc7e0ef3878c3d4a92a7233208e6f91553de266

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
