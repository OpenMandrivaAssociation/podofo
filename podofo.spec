%define major 2
%define oldlibname %mklibname %{name} 0.9.7
%define libname %mklibname %{name}
%define devname %mklibname %{name} -d

Summary:	Tools and libraries to work with the PDF file format
Name:		podofo
Version:	0.10.3
Release:	2
Group:		Publishing
License:	GPL and LGPL
Url:		http://podofo.github.io/
Source0:	https://github.com/podofo/podofo/archive/refs/tags/%{version}.tar.gz
Patch0:		podofo-0.10.1-clang16.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	doxygen
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(libidn)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)

%description
PoDoFo is a library to work with the PDF file format. The name comes from
the first letter of PDF (Portable Document Format). A few tools to work
with PDF files are already included in the PoDoFo package.

The PoDoFo library is a free, portable C++ library which includes classes
to parse PDF files and modify their contents into memory. The changes can be
written back to disk easily. The parser can also be used to extract
information from a PDF file (for example the parser could be used in a PDF
viewer). Besides parsing PoDoFo includes also very simple classes to create
your own PDF files. All classes are documented so it is easy to start writing
your own application using PoDoFo.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Runtime library for %{name}
Group:		System/Libraries
License:	LGPLv2+
# loads legacy provider which is in openssl
Requires:	openssl
# We had wrong major used for library package
Obsoletes:	%{_lib}podofo0 < 0.9.2
Conflicts:	%{_lib}podofo0 < 0.9.2
%rename %{oldlibname}
# There used to be a podofo binary; that was removed
# in 0.10.x
Obsoletes:	%{name} < %{EVRD}

%description -n %{libname}
Runtime library for %{name}.

%files -n %{libname}
%{_libdir}/libpodofo.so.%{major}*
%{_libdir}/libpodofo.so.%{version}

#----------------------------------------------------------------------------

%package -n 	%{devname}
Summary:	Development files for %{name} library
Group:		Development/C
License:	LGPLv2+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files and documentation for the %{name} library.

%files -n %{devname}
%doc doc/html
%{_includedir}/%{name}
%{_libdir}/libpodofo.so
%{_libdir}/pkgconfig/*.pc
%dir %{_datadir}/podofo
%{_datadir}/podofo/*.cmake

#----------------------------------------------------------------------------

%prep
%autosetup -p1
export CXX='%__cxx -std=c++20'

%cmake \
%if "%{_lib}" == "lib64"
	-DWANT_LIB64=1 \
%endif
	-G Ninja

%build
%ninja_build -C build

# build the docs
doxygen

%install
%ninja_install -C build
