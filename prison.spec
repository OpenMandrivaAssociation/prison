%define major 0
%define libname %mklibname %name %major
%define develname %mklibname %name -d


Name:		prison
Group:		Development/C++
Summary:	Prison is a Qt based barcode abstraction layer/library
Version:	1.0
Release:	2
License: 	MIT
URL:            https://projects.kde.org/projects/kdesupport/prison
Source0:        ftp://ftp.kde.org/pub/kde/stable/prison/1.0/src/%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	qrencode-devel
BuildRequires:	libdmtx-devel

%description
Prison is a Qt based barcode abstraction layer/library and provides
uniform access to generation of barcodes with data.

#-------------------------------------------------------------------------------
%package -n %libname
Summary:	Prison library
Group:          System/Libraries

%description -n %libname
Library for %name.

Prison is a Qt based barcode abstraction layer/library and provides
uniform access to generation of barcodes with data.

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libprison.so.%{major}*

#-------------------------------------------------------------------------------
%package -n %develname
Summary:	Prison development files
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %develname
Development files for applications that use %{name}.

Prison is a Qt based barcode abstraction layer/library and provides
uniform access to generation of barcodes with data.

%files -n %develname
%defattr(-,root,root)
%doc LICENSE
%{_includedir}/%name
%{_libdir}/libprison.so
%{_libdir}/cmake/Prison

#-------------------------------------------------------------------------------
%prep
%setup -q

%build
%cmake_qt4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build


%clean
rm -rf %{buildroot}




%changelog
* Thu Jun 30 2011 José Melo <ze@mandriva.org> 1.0-1mdv2011.0
+ Revision: 688340
- version 1.0
- fix descriptions and license
- minor fixes

* Thu Apr 28 2011 José Melo <ze@mandriva.org> 0.0.0-1
+ Revision: 660105
- import prison

