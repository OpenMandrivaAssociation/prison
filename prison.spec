%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d


Summary:	Prison is a Qt based barcode abstraction layer/library
Name:		prison
Group:		Development/C++
Version:	1.1.0
Release:	3
License:	MIT
Url:		https://projects.kde.org/projects/kdesupport/prison
Source0:	ftp://ftp.kde.org/pub/kde/stable/prison/1.1/src/%{name}-%{version}.tar.xz
Patch0:		fix-major-version.patch
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(libqrencode)
BuildRequires:	pkgconfig(libdmtx)

%description
Prison is a Qt based barcode abstraction layer/library and provides
uniform access to generation of barcodes with data.

%package -n %{libname}
Summary:	Prison library
Group:		System/Libraries

%description -n %{libname}
Library for %{name}.

Prison is a Qt based barcode abstraction layer/library and provides
uniform access to generation of barcodes with data.

%files -n %{libname}
%{_libdir}/libprison.so.%{major}*

%package -n %{devname}
Summary:	Prison development files
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for applications that use %{name}.

%files -n %{devname}
%doc LICENSE
%{_includedir}/%{name}
%{_libdir}/libprison.so
%{_libdir}/cmake/Prison

%prep
%setup -q
%apply_patches

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

