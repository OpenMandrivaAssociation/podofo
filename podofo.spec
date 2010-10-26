%define	major	0
%define libname	%mklibname %{name} %{major}
%define	develname	%mklibname	%{name} -d	
%define badlibname	%mklibname lib%{name} %{major}
%define	baddevelname	%mklibname	lib%{name} -d

Name:		podofo
Version:	0.8.4
Release:	%mkrel 1
Summary:	Tools and libraries to work with the PDF file format
Group:		Publishing
License:	GPL and LGPL
URL:		http://podofo.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:	cmake 
BuildRequires:	zlib-devel 
BuildRequires:	jpeg-devel 
BuildRequires:	tiff-devel 
BuildRequires:	freetype-devel 
BuildRequires:	fontconfig-devel
BuildRequires:	cppunit-devel 
BuildRequires:	lua-devel 
BuildRequires:	doxygen


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


%package -n %{libname}
Summary:	Runtime library for %{name}
Group:		System/Libraries
License:	LGPLv2+
Obsoletes:	%{badlibname} < %{version}-%{release}

%description -n %{libname}
Runtime library for %{name}.


%package -n 	%{develname}
Summary:	Development files for %{name} library
Group:		Development/C
License:	LGPLv2+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{baddevelname} < %{version}-%{release}

%description -n %{develname}
Development files and documentation for the %{name} library.


%prep
%setup -q

%build
%cmake -DPODOFO_BUILD_SHARED=1 \
%ifarch x86_64 
-DWANT_LIB64=1 \
%endif
..

%make 

# build the docs
doxygen ../

# set timestamps on generated files to some constant
#find ../doc/html -exec touch -r %{Source0} {} \;


%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/%{name}*

%files -n %{libname}
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LIB ChangeLog FAQ.html README.html TODO
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%doc doc/html
%{_includedir}/%{name}
%{_libdir}/*.so
