%define version 3.1.8
%define release %mkrel 2

%define major 3
%define libname %mklibname %name %major

Summary: Arithmetic and metadata operators for netCDF and HDF4 files
Name: nco
Version: %version
Release: %release
License: GPL
Group: Sciences/Mathematics
Source: ftp://nco.sourceforge.net/pub/nco/nco-%version.tar.bz2
URL: http://nco.sourceforge.net
BuildRequires: gcc gcc-c++ 
BuildRequires: netcdf-devel >= 3.6
BuildRequires: udunits-devel
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

%package -n %libname-devel
Summary: Development files from NCO
Group: Development/Other
Provides: lib%name-devel = %version-%release
Provides: %name-devel = %version-%release
Requires: %libname = %version-%release

%description -n %libname-devel
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

%build
export CFLAGS="%optflags -fPIC"
%configure2_5x
%make CPPFLAGS="%optflags -fPIC" CCFLAGS="%optflags -fPIC"

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
%{_libdir}/libnco_c++-%version.so

%files -n %libname-devel
%defattr(-, root, root, -)
%doc doc/*
%{_includedir}/*.hh
%{_libdir}/libnco.a
%{_libdir}/libnco.la
%{_libdir}/libnco.so
%{_libdir}/libnco_c++.so
%{_libdir}/libnco_c++.la
%{_libdir}/libnco_c++.a

%clean
[ %buildroot != '/' ] && rm -fr %buildroot

