%define major 0
%define libname %mklibname %name %major
%define develname %mklibname %name -d


Name:		prison
Group:		Development/C++
Summary:	Prison is a Qt based barcode abstraction layer/library
Version:	0.0.0
Release:	%mkrel 1
URL:		https://projects.kde.org/projects/kdesupport/prison
License: 	GPLv2
# Use git repo or create tarball wget -c http://anongit.kde.org/prison/%name-latest.tar.gz
Source0:	http://anongit.kde.org/prison/%name.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	qrencode-devel
BuildRequires:	libdmtx-devel

%description
Prison is a Qt based barcode abstraction layer/library and provides uniform access
to generation of barcodes with data.



#-------------------------------------------------------------------------------
%package -n %libname
Group:          System/Libraries
Summary:	Prison library

%description -n %libname
Library for %name.

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libprison.so.%{major}*


#-------------------------------------------------------------------------------
%package -n %develname
Group:		Development/C++
Summary:	Prison development files
Requires:	%libname = %version-%release
Provides:	%{name}-devel = %version-%release

%description -n %develname
Development files for %name.

%files -n %develname
%defattr(-,root,root)
%{_includedir}/%name
%{_libdir}/libprison.so
%{_libdir}/cmake/Prison/PrisonConfig.cmake


#-------------------------------------------------------------------------------
%prep
%setup -qn %name

%build
%cmake_qt4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build


%clean
rm -rf %{buildroot}


