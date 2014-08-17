%bcond_without qt4
%bcond_without qt5

%define major 0
%define qt5major 1
%define libname %mklibname %{name} %{major}
%define qt5libname %mklibname %{name} %{qt5major}
%define devname %mklibname %{name} -d
%define git 20140817

Summary:	Prison is a Qt based barcode abstraction layer/library
Name:		prison
Group:		Development/C++
Version:	1.2.0
Release:	%{?git:0.%{git}.}2
License:	MIT
Url:		https://projects.kde.org/projects/kdesupport/prison
%if %git
# git://anongit.kde.org/prison
Source0:	%{name}-%{git}.tar.xz
%else
Source0:	ftp://ftp.kde.org/pub/kde/stable/prison/1.1/src/%{name}-%{version}.tar.xz
%endif
Patch0:		prison-1.2.0-qt5-compile.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(libqrencode)
BuildRequires:	pkgconfig(libdmtx)
%if %{with qt4}
BuildRequires:	qt4-devel
%endif
%if %{with qt5}
BuildRequires:	cmake(ECM)
BuildRequires:	qt5-devel
%endif

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

%if %{with qt4}
%files -n %{libname}
%{_libdir}/libprison.so.%{major}*
%endif

%package -n %{qt5libname}
Summary:	Prison library for Qt 5.x
Group:		System/Libraries

%description -n %{qt5libname}
Library for %{name} for Qt 5.x.

Prison is a Qt based barcode abstraction layer/library and provides
uniform access to generation of barcodes with data.

%if %{with qt5}
%files -n %{qt5libname}
%{_libdir}/libprison.so.%{qt5major}*
%endif

%package -n %{devname}
Summary:	Prison development files
Group:		Development/C++
%if %{with qt5}
Requires:	%{qt5libname} = %{EVRD}
%else
Requires:	%{libname} = %{EVRD}
%endif
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
%if %{with qt4}
%cmake_qt4
%make
cd ..
mv build build4
%endif
%if %{with qt5}
%cmake -DQT5_BUILD:BOOL=ON
%make
cd ..
mv build build5
%endif

%install
%if %{with qt4}
ln -s build4 build
%makeinstall_std -C build
%endif

%if %{with qt5}
rm build ; ln -s build5 build
%makeinstall_std -C build
%endif
