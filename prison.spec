%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define git 20141220

Summary:	Prison is a Qt based barcode abstraction layer/library
Name:		prison
Group:		Development/C++
Version:	1.2.0
Release:	%{?git:0.%{git}.}3
License:	MIT
Url:		https://projects.kde.org/projects/kdesupport/prison
%if %git
# git://anongit.kde.org/prison
Source0:	%{name}-%{git}.tar.xz
%else
Source0:	ftp://ftp.kde.org/pub/kde/stable/prison/1.1/src/%{name}-%{version}.tar.xz
%endif
BuildRequires:	cmake
BuildRequires:	pkgconfig(libqrencode)
BuildRequires:	pkgconfig(libdmtx)
BuildRequires:	qt4-devel

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
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

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
