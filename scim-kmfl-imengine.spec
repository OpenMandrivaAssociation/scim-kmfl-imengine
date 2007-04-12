%define version	0.9
%define release	%mkrel 2
%define src_name	scim_kmfl_imengine

%define scim_version	1.4.0
%define libkmfl_version	0.5

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-kmfl-imengine
Summary:	Scim-kmfl-imengine is an SCIM IMEngine module for KMFL
Version:		%{version}
Release:		%{release}
Group:		System/Internationalization
License:		GPL
URL:			http://kmfl.sourceforge.net/
Source0:		%{src_name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:			%{libname} = %{version}-%{release}
Requires:			libkmfl >= %{libkmfl_version}
Requires:			scim >= %{scim_version}
BuildRequires:		libkmfl-devel >= %{libkmfl_version}
BuildRequires:		scim-devel >= %{scim_version}
BuildRequires:		automake1.8, libltdl-devel
BuildRequires:		perl(XML::Parser)
BuildRequires:          libxkbfile-devel 

%description
Scim-kmfl-imengine is an SCIM IMEngine module for KMFL.
Scim-kmfl-imengine needs binary Tavultesoft Keyman files 
compiled by kmflcomp.


%package -n	%{libname}
Summary:	Scim-kmfl-imengine library
Group:		System/Internationalization
Provides:		%{libname_orig} = %{version}-%{release}

%description -n %{libname}
Scim-kmfl-imengine library.


%prep
%setup -q -n %{src_name}-%{version}
cp /usr/share/automake-1.9/mkinstalldirs .

%build
[[ ! -x configure ]] && ./bootstrap
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
%doc COPYING 
%{_libdir}/scim-1.0/%{scim_version}/IMEngine/*
%{_libdir}/scim-1.0/%{scim_version}/SetupUI/*



