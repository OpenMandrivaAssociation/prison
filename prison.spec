%define major 5
%define libname %mklibname KF5Prison %{major}
%define devname %mklibname KF5Prison -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Prison is a Qt based barcode abstraction layer/library
Name:		prison
Group:		Development/C++
Version:	5.78.0
License:	MIT
Url:		https://projects.kde.org/projects/kdesupport/prison
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Release:	1
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	ninja
BuildRequires:	pkgconfig(libqrencode)
BuildRequires:	pkgconfig(libdmtx)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

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
%{_datadir}/qlogging-categories5/prison.categories
%{_datadir}/qlogging-categories5/prison.renamecategories
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
%{_includedir}/KF5/%{name}
%{_includedir}/KF5/%{name}_version.h
%{_libdir}/libKF5Prison.so
%{_libdir}/cmake/KF5Prison
%{_libdir}/qt5/mkspecs/modules/qt_Prison.pri

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
