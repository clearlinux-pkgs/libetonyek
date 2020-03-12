#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libetonyek
Version  : 0.1.9
Release  : 4
URL      : https://dev-www.libreoffice.org/src/libetonyek-0.1.9.tar.xz
Source0  : https://dev-www.libreoffice.org/src/libetonyek-0.1.9.tar.xz
Summary  : Library for parsing Apple Keynote file format structure
Group    : Development/Tools
License  : MPL-2.0-no-copyleft-exception
Requires: libetonyek-bin = %{version}-%{release}
Requires: libetonyek-lib = %{version}-%{release}
Requires: libetonyek-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : doxygen
BuildRequires : glm-dev
BuildRequires : mdds-dev
BuildRequires : pkgconfig(cppunit)
BuildRequires : pkgconfig(liblangtag)
BuildRequires : pkgconfig(librevenge-0.0)
BuildRequires : pkgconfig(librevenge-generators-0.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(zlib)
BuildRequires : sed

%description
libetonyek is a library and a set of tools for reading and converting
Apple iWork documents (Keynote, Pages and Numbers). Supported versions
are Keynote 2-6, Pages 1-4 and Numbers 1-2. See FEATURES for more
details about what is currently supported.

%package bin
Summary: bin components for the libetonyek package.
Group: Binaries
Requires: libetonyek-license = %{version}-%{release}

%description bin
bin components for the libetonyek package.


%package dev
Summary: dev components for the libetonyek package.
Group: Development
Requires: libetonyek-lib = %{version}-%{release}
Requires: libetonyek-bin = %{version}-%{release}
Provides: libetonyek-devel = %{version}-%{release}
Requires: libetonyek = %{version}-%{release}

%description dev
dev components for the libetonyek package.


%package doc
Summary: doc components for the libetonyek package.
Group: Documentation

%description doc
doc components for the libetonyek package.


%package lib
Summary: lib components for the libetonyek package.
Group: Libraries
Requires: libetonyek-license = %{version}-%{release}

%description lib
lib components for the libetonyek package.


%package license
Summary: license components for the libetonyek package.
Group: Default

%description license
license components for the libetonyek package.


%prep
%setup -q -n libetonyek-0.1.9
cd %{_builddir}/libetonyek-0.1.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583992798
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --with-mdds=1.5
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1583992798
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libetonyek
cp %{_builddir}/libetonyek-0.1.9/COPYING %{buildroot}/usr/share/package-licenses/libetonyek/9744cedce099f727b327cd9913a1fdc58a7f5599
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/key2raw
/usr/bin/key2text
/usr/bin/key2xhtml
/usr/bin/numbers2csv
/usr/bin/numbers2raw
/usr/bin/numbers2text
/usr/bin/pages2html
/usr/bin/pages2raw
/usr/bin/pages2text

%files dev
%defattr(-,root,root,-)
/usr/include/libetonyek-0.1/libetonyek/EtonyekDocument.h
/usr/include/libetonyek-0.1/libetonyek/libetonyek.h
/usr/lib64/libetonyek-0.1.so
/usr/lib64/pkgconfig/libetonyek-0.1.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libetonyek/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libetonyek-0.1.so.1
/usr/lib64/libetonyek-0.1.so.1.0.9

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libetonyek/9744cedce099f727b327cd9913a1fdc58a7f5599
