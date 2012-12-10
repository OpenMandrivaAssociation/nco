%define _disable_ld_as_needed 0

# default to 0
%define build_ncocpp %{?_with_ncocpp:1}%{?!_with_ncocpp:0}

%define major 3
%define libname %mklibname %name %major
%define libnamedevel %mklibname %name -d

Summary: Arithmetic and metadata operators for netCDF and HDF4 files
Name: nco
Version: 4.0.8
Release: 2
License: GPL
Group: Sciences/Mathematics
Source0: http://nco.sourceforge.net/src/%{name}-%{version}.tar.gz 
Patch0: nco-undefined-functions.patch
URL: http://nco.sourceforge.net
BuildRequires: netcdf-devel >= 4.1
BuildRequires: udunits-devel
# we needs c++ in order to build ncap:
%if %build_ncocpp
# This package does not exists yet...
BuildRequires: antlr-devel >= 3
%endif

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
Provides: lib%name = %{EVRD}

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
Provides: lib%name-devel = %{EVRD}
Provides: %name-devel = %{EVRD}
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
%patch0 -p1 -b .undef-functions

%build
%configure2_5x \
%if %build_ncocpp
    --enable-nco_cplusplus --enable-ncoxx
%else
    --disable-nco_cplusplus --disable-ncoxx --disable-ncap2
%endif

%make CPPFLAGS="%optflags -fPIC -I %_includedir/netcdf-3" \
    CCFLAGS="%optflags -fPIC -I %_includedir/netcdf-3"

%install
%makeinstall

%files
%doc doc/*
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/*

%files -n %libname
%doc doc/*
%{_libdir}/libnco-%version.so
%if %build_ncocpp
%{_libdir}/libnco_c++-%version.so
%endif

%files -n %libnamedevel
%doc doc/*
%if %build_ncocpp
%{_includedir}/*.hh
%{_libdir}/libnco_c++.so
%{_libdir}/libnco_c++.a
%endif
%{_libdir}/libnco.a
%{_libdir}/libnco.so


%changelog
* Fri Dec 30 2011 Alexander Khrukin <akhrukin@mandriva.org> 4.0.8-1
+ Revision: 748265
- version update 4.0.8

* Fri Aug 13 2010 Emmanuel Andry <eandry@mandriva.org> 4.0.2-1mdv2011.0
+ Revision: 569440
- New version 4.0.2
- set define _disable_ld_as_needed to 0

* Tue Apr 13 2010 Christophe Fergeau <cfergeau@mandriva.com> 4.0.1-1mdv2010.1
+ Revision: 534498
- nco 4.0.1
  - rediff patch0
  - make sure nco++ isn't built
  - make sure we compiled against the newest netcdf

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 3.9.5-3mdv2010.0
+ Revision: 430160
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 3.9.5-2mdv2009.0
+ Revision: 268244
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Jun 05 2008 Olivier Thauvin <nanardon@mandriva.org> 3.9.5-1mdv2009.0
+ Revision: 215201
- 3.9.5
- return back of buildroot to allow backport

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - explain require

* Fri Dec 21 2007 Olivier Thauvin <nanardon@mandriva.org> 3.9.3-1mdv2008.1
+ Revision: 136185
- 3.9.3
- allways requires gcc-c++ to enable build of ncap (Reported by Patrick Brockmann)

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 05 2007 Olivier Thauvin <nanardon@mandriva.org> 3.9.2-1mdv2008.0
+ Revision: 80430
- 3.9.2

* Wed Jun 27 2007 Olivier Thauvin <nanardon@mandriva.org> 3.9.0-1mdv2008.0
+ Revision: 44835
- 3.9.0, disable c++ lib, need last antlr not yet packaged
- apply new devel policy

