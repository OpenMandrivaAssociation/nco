%define version 3.9.5
%define release %mkrel 1

%define _disable_ld_as_needed 1

# default to 0
%define build_ncocpp %{?_with_ncocpp:1}%{?!_with_ncocpp:0}

%define major 3
%define libname %mklibname %name %major
%define libnamedevel %mklibname %name -d

Summary: Arithmetic and metadata operators for netCDF and HDF4 files
Name: nco
Version: %version
Release: %release
License: GPL
Group: Sciences/Mathematics
Source: ftp://nco.sourceforge.net/pub/nco/nco-%version.tar.gz
Patch0: nco-undefined-functions.patch
URL: http://nco.sourceforge.net
BuildRequires: gcc
BuildRequires: netcdf-devel >= 3.6
BuildRequires: udunits-devel
# we needs c++ in order to build ncap:
BuildRequires: gcc-c++
%if %build_ncocpp
# This package does not exists yet...
BuildRequires: antlr-devel >= 3
%endif
BuildRoot: %_tmppath/%name-%version-root

%description
The netCDF Operators, or NCO, are a suite of programs known as
operators. The operators facilitate manipulation and analysis of
self-describing data stored in the netCDF or HDF4 formats, which are
freely available (http://www.unidata.ucar.edu/packages/netcdf and
http://hdf.ncsa.uiuc.edu, respectively). Each NCO operator (e.g., 
ncks) takes netCDF or HDF4 input file(s), performs an operation (e.g.,
averaging, hyperslabbing, or renaming), and outputs a processed netCDF
file. Although most users of netCDF and HDF data are involved in
scientific research, these data formats, and thus NCO, are generic and
are equally useful in fields like finance. The NCO User's Guide
illustrates NCO use with examples from the field of climate modeling
and analysis. The NCO homepage is http://nco.sourceforge.net.

%package -n %libname
Summary: NCO libraries
Group: System/Libraries
Provides: lib%name = %version-%release

%description -n %libname
The netCDF Operators, or NCO, are a suite of programs known as
operators. The operators facilitate manipulation and analysis of
self-describing data stored in the netCDF or HDF4 formats, which are
freely available (http://www.unidata.ucar.edu/packages/netcdf and
http://hdf.ncsa.uiuc.edu, respectively). Each NCO operator (e.g.,
ncks) takes netCDF or HDF4 input file(s), performs an operation (e.g.,
averaging, hyperslabbing, or renaming), and outputs a processed netCDF
file. Although most users of netCDF and HDF data are involved in
scientific research, these data formats, and thus NCO, are generic and
are equally useful in fields like finance. The NCO User's Guide
illustrates NCO use with examples from the field of climate modeling
and analysis. The NCO homepage is http://nco.sourceforge.net.

This package contains libraries from NCO.

%package -n %libnamedevel
Summary: Development files from NCO
Group: Development/Other
Provides: lib%name-devel = %version-%release
Provides: %name-devel = %version-%release
Requires: %libname = %version-%release
Obsoletes: %mklibname -d %name 3

%description -n %libnamedevel
The netCDF Operators, or NCO, are a suite of programs known as
operators. The operators facilitate manipulation and analysis of
self-describing data stored in the netCDF or HDF4 formats, which are
freely available (http://www.unidata.ucar.edu/packages/netcdf and
http://hdf.ncsa.uiuc.edu, respectively). Each NCO operator (e.g.,
ncks) takes netCDF or HDF4 input file(s), performs an operation (e.g.,
averaging, hyperslabbing, or renaming), and outputs a processed netCDF
file. Although most users of netCDF and HDF data are involved in
scientific research, these data formats, and thus NCO, are generic and
are equally useful in fields like finance. The NCO User's Guide
illustrates NCO use with examples from the field of climate modeling
and analysis. The NCO homepage is http://nco.sourceforge.net.

This package contains files need to build application using NCO library.

%prep
%setup -q 
%patch0 -p0 -b .undef-functions

%build
%configure2_5x \
%if %build_ncocpp
    --enable-nco_cplusplus --enable-ncoxx
%else
    --disable-nco_cplusplus --disable-ncoxx
%endif

%make CPPFLAGS="%optflags -fPIC -I %_includedir/netcdf-3" \
    CCFLAGS="%optflags -fPIC -I %_includedir/netcdf-3"

%install
%makeinstall

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files
%defattr(-, root, root, -)
%doc doc/*
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/*

%files -n %libname
%defattr(-, root, root, -)
%doc doc/*
%{_libdir}/libnco-%version.so
%if %build_ncocpp
%{_libdir}/libnco_c++-%version.so
%endif

%files -n %libnamedevel
%defattr(-, root, root, -)
%doc doc/*
%if %build_ncocpp
%{_includedir}/*.hh
%{_libdir}/libnco_c++.so
%{_libdir}/libnco_c++.la
%{_libdir}/libnco_c++.a
%endif
%{_libdir}/libnco.a
%{_libdir}/libnco.la
%{_libdir}/libnco.so

%clean
[ %buildroot != '/' ] && rm -fr %buildroot
