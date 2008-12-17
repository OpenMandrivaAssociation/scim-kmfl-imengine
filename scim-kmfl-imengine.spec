%define src_name	scim_kmfl_imengine

%define scim_version	1.4.0
%define libkmfl_version	%{version}

Name:		scim-kmfl-imengine
Summary:	SCIM IM engine module for KMFL
Version:	0.9.7
Release:	%mkrel 1
Group:		System/Internationalization
License:	GPLv2+
URL:		http://kmfl.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/kmfl/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	scim >= %{scim_version}
BuildRequires:	libkmfl-devel >= %{libkmfl_version}
BuildRequires:	scim-devel >= %{scim_version}
BuildRequires:	libltdl-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	libxkbfile-devel 
Obsoletes:	%{mklibname scim-kmfl-imengine 0}

%description
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
rm -rf %{buildroot}
%makeinstall_std

# remove unnecessary files
rm -f %{buildroot}/%{_libdir}/scim-1.0/1.2.0/*/*.{a,la}

# remove documents (AUTHORS, COPYING etc.)
# they should be installed by %doc
rm -rf %{buildroot}/%{_prefix}/doc/

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%{_libdir}/scim-1.0/%{scim_version}/IMEngine/*
%{_libdir}/scim-1.0/%{scim_version}/SetupUI/*
%{_datadir}/scim/kmfl/icons/default.png

