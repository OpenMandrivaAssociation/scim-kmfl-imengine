%define version		0.9.6
%define release		%mkrel 1
%define src_name	scim_kmfl_imengine

%define scim_version	1.4.0
%define libkmfl_version	0.5

%define major		0
%define libname_orig	lib%{name}
%define libname		%mklibname %{name} %{major}

Name:		scim-kmfl-imengine
Summary:	Scim-kmfl-imengine is an SCIM IM engine module for KMFL
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPLv2+
URL:		http://kmfl.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/kmfl/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	%{libname} = %{version}-%{release}
Requires:	libkmfl >= %{libkmfl_version}
Requires:	scim >= %{scim_version}
BuildRequires:	libkmfl-devel >= %{libkmfl_version}
BuildRequires:	scim-devel >= %{scim_version}
BuildRequires:	libltdl-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libxkbfile-devel 

%description
KMFL is a keyboarding input method which aims to bring Tavultesoft
Keyman functionality to Linux.

scim-kmfl-imengine is one of three parts of the KMFL project. It is a 
SCIM input method engine. The other two parts are libkmfl and
kmflcomp.

%package -n	%{libname}
Summary:	Scim-kmfl-imengine library
Group:		System/Internationalization
Provides:	%{libname_orig} = %{version}-%{release}

%description -n %{libname}
KMFL is a keyboarding input method which aims to bring Tavultesoft
Keyman functionality to Linux.

scim-kmfl-imengine is one of three parts of the KMFL project. It is a 
SCIM input method engine. The other two parts are libkmfl and
kmflcomp.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unnecessary files
rm -f %{buildroot}/%{_libdir}/scim-1.0/1.2.0/*/*.{a,la}

# remove documents (AUTHORS, COPYING etc.)
# they should be installed by %doc
rm -rf %{buildroot}/%{_prefix}/doc/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%{_libdir}/scim-1.0/%{scim_version}/IMEngine/*
%{_libdir}/scim-1.0/%{scim_version}/SetupUI/*