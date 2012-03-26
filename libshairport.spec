%define	major	1
%define	libname	%mklibname shairport %{major}
%define	devname	%mklibname shairport -d

%define	snap	20120111
%define	rel	1

Summary:	Apple RAOP server library
Name:		libshairport
Version:	1.2.1
Release:	%mkrel 0.git%{snap}.%{rel}
License:	MIT
Group:		System/Libraries
URL:		https://github.com/amejia1/libshairport
# git archive --prefix libshairport-20120111/ master | xz > libshairport-20120111.tar.xz
Source:		%{name}-%{snap}.tar.xz
BuildRequires:	openssl-devel
BuildRequires:	libao-devel

%description
This library emulates an AirPort Express for the purpose of streaming
music from iTunes and compatible iPods. It implements a server for the
Apple RAOP protocol.

ShairPort does not support AirPlay v2 (video and photo streaming).

%package -n %{libname}
Summary:	Shared library of libshairport
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n %{libname}
libshairport is an Apple RAOP server library.

This package contains the library needed to run programs dynamically
linked with libshairport.

%package -n %{devname}
Summary:	Headers for libshairport development
Group:		Development/C
Requires:	%{libname} = %{EVRD}
# we are not actually linking against it (just using the headers), so this
# doesn't get added automatically:
Requires:	libao-devel
Provides:	shairport-devel = %{EVRD}

%description -n %{devname}
libshairport is an Apple RAOP server library.

This package contains the headers that are needed to compile
applications that use libshairport.

%prep
%setup -q -n %{name}-%{snap}

%build
autoreconf -fi
%configure2_5x --disable-static
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%doc README
%{_libdir}/*.so
%dir %{_includedir}/shairport
%{_includedir}/shairport/*.h
%{_libdir}/pkgconfig/%{name}.pc
%if %{mdvver} < 201200
%{_libdir}/*.la
%endif

