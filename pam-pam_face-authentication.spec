Summary:	This is Pluggable Authentication Module for Face based Authentication
Name:		pam-pam_face-authentication
Version:	0.3
Release:	0.1
License:	GPL
Group:		Applications/System
URL:		http://www.pam-face-authentication.org/
Source0:	http://pam-face-authentication.googlecode.com/files/pam-face-authentication-%{version}.tar.gz
# Source0-md5:	5ef71bcf4bdebd2ee7216387ef17fc27
BuildRequires:	gsl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	opencv-devel
BuildRequires:	pam-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Pluggable Authentication Module for Face based Authentication.

%prep
%setup -q -n pam-face-authentication-%{version}

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS AUTHORS README
