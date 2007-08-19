%define name PyCDDB
%define version 0.1.3
%define release 1

Summary: CDDB-Server access from Python
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
BuildArchitectures: noarch
Vendor: Roland Schaeuble <rschaeuble@gmx.ch>
Url: http://pycddb.sourceforge.net

%description
UNKNOWN

%prep
%setup

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
