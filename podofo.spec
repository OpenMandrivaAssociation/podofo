%define	major	0
%define libname	%mklibname %{name} %{major}
%define	develname	%mklibname	%{name} -d	
%define badlibname	%mklibname lib%{name} %{major}
%define	baddevelname	%mklibname	lib%{name} -d

Name:		podofo
Version:	0.9.1
Release:	2
Summary:	Tools and libraries to work with the PDF file format
Group:		Publishing
License:	GPL and LGPL
URL:		http://podofo.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		podofo-0.9.1-gcc4.7.patch

BuildRequires:	cmake 
BuildRequires:	pkgconfig(zlib)
BuildRequires:	jpeg-devel 
BuildRequires:	tiff-devel 
BuildRequires:	freetype-devel 
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(lua)
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
%patch0 -p0

%build
%cmake -DPODOFO_BUILD_SHARED=1 \
%ifarch x86_64 
-DWANT_LIB64=1 \
%endif
..

%make 

# build the docs
doxygen ../



%install
%makeinstall_std -C build


%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/%{name}*
%doc %{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LIB ChangeLog FAQ.html README.html TODO
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%doc doc/html
%{_includedir}/%{name}
%{_libdir}/*.so


%changelog
* Mon Sep 26 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.9.1-1
+ Revision: 701226
- new version 0.9.1

* Tue Oct 26 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.8.4-1mdv2011.0
+ Revision: 589450
- update to 0.8.4

* Wed Aug 25 2010 Funda Wang <fwang@mandriva.org> 0.8.2-1mdv2011.0
+ Revision: 573150
- new version 0.8.2

* Fri Jul 30 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.8.1-3mdv2011.0
+ Revision: 563233
- add patch from upstream SVN to fix compilation
- update to 0.8.1

* Fri May 28 2010 Juan Luis Baptiste <juancho@mandriva.org> 0.8.0-1mdv2011.0
+ Revision: 546552
- Updated to 0.8.0 and removed patch to fix fprint strings.

* Tue Apr 20 2010 Tomas Kindl <supp@mandriva.org> 0.7.0-2mdv2010.1
+ Revision: 537257
- fix really really bad libname/develname and obsolete it...

* Mon Apr 19 2010 Tomas Kindl <supp@mandriva.org> 0.7.0-1mdv2010.1
+ Revision: 536544
- initial PoDoFo import
- create podofo

