Name:           hyphen
Summary:        Hyphenation library to use converted TeX hyphenation patterns
Version:        2.8.8
Release:        1
Group:          Graphics & UI Framework/Utilities
License:        MPL-1.1+ or LGPL-2.1+ or GPL-2.0+
Url:            http://hunspell.sourceforge.net
Source0:        http://sourceforge.net/projects/hunspell/files/Hyphen/2.8/hyphen-%{version}.tar.gz
Source1001:     packaging/hyphen.manifest
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Hyphenation library to use converted TeX hyphenation patterns.

%package -n libhyphen
Summary:        Hyphenation Library
Group:          Development/Libraries

%description -n libhyphen
Hyphenation Library.

%package tools
Summary:        Hyphenatione development tools
Group:          Development/Libraries
Requires:       libhyphen = %{version}
Requires:       pkgconfig

%description tools
Hyphenatione development tools.

%package devel
Summary:        Hyphenatione development libraries and header files
Group:          Development/Libraries
Requires:       libhyphen = %{version}
Requires:       zlib-devel
Requires:       pkgconfig

%description devel
Hyphenatione development libraries and header file.

%prep
%setup -q 

%build
cp %{SOURCE1001} .

%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

%makeinstall gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale
mkdir -p %{buildroot}/usr/share/license
cat COPYING COPYING.LGPL > %{buildroot}/usr/share/license/%{name}

# Don't package static a or .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

%post -n libhyphen -p /sbin/ldconfig

%postun -n libhyphen -p /sbin/ldconfig

%files -n libhyphen
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_libdir}/libhyphen.so.*
%{_datadir}/hyphen/hyph_en_US.dic
/usr/share/license/%{name}

%files tools
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_bindir}/substrings.pl

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_libdir}/libhyphen.so
%{_includedir}/*.h
