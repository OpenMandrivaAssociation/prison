%define major 5
%define libname %mklibname KF5Prison %{major}
%define devname %mklibname KF5Prison -d
%define git %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Prison is a Qt based barcode abstraction layer/library
Name:		prison
Group:		Development/C++
Version:	5.49.0
License:	MIT
Url:		https://projects.kde.org/projects/kdesupport/prison
%if 0%git
# git://anongit.kde.org/prison
Source0:	%{name}-%{git}.tar.xz
Release:	1.%{git}.1
%else
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Release:	1
%endif
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	ninja
BuildRequires:	pkgconfig(libqrencode)
BuildRequires:	pkgconfig(libdmtx)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)

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
%{_sysconfdir}/xdg/prison.categories
%{_libdir}/libKF5Prison.so.%{major}*
%{_libdir}/qt5/qml/org/kde/prison

%package -n %{devname}
Summary:	Prison development files
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for applications that use %{name}.

%files -n %{devname}
%doc LICENSE
%{_includedir}/KF5/%{name}
%{_includedir}/KF5/%{name}_version.h
%{_libdir}/libKF5Prison.so
%{_libdir}/cmake/KF5Prison
%{_libdir}/qt5/mkspecs/modules/qt_Prison.pri

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
