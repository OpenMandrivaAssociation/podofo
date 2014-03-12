%define major 0.9.1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Tools and libraries to work with the PDF file format
Name:		podofo
Version:	0.9.2
Release:	6
Group:		Publishing
License:	GPL and LGPL
Url:		http://podofo.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(libidn)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)

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

%files
%doc COPYING
%{_bindir}/%{name}*
%doc %{_mandir}/man1/%{name}*.1*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Runtime library for %{name}
Group:		System/Libraries
License:	LGPLv2+
# We had wrong major used for library package
Obsoletes:	%{_lib}podofo0 < 0.9.2
Conflicts:	%{_lib}podofo0 < 0.9.2

%description -n %{libname}
Runtime library for %{name}.

%files -n %{libname}
%doc AUTHORS COPYING.LIB ChangeLog FAQ.html README.html TODO
%{_libdir}/libpodofo.so.%{major}*

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

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake -DPODOFO_BUILD_SHARED=1 \
%ifarch x86_64
-DWANT_LIB64=1
%endif

%make

# build the docs
doxygen ../

%install
%makeinstall_std -C build

