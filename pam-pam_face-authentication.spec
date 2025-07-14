Summary:	This is Pluggable Authentication Module for Face based Authentication
Summary(pl.UTF-8):	Modularny system uwierzytelniania PAM opearty o weryfikację twarzy.
Name:		pam-pam_face-authentication
Version:	0.3
Release:	0.2
License:	GPL
Group:		Applications/System
URL:		http://www.pam-face-authentication.org
Source0:	http://pam-face-authentication.googlecode.com/files/pam-face-authentication-%{version}.tar.gz
# Source0-md5:	5ef71bcf4bdebd2ee7216387ef17fc27
Patch0:		cmake.patch
BuildRequires:	cmake >= 2.6
BuildRequires:	gsl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	opencv-devel
BuildRequires:	pam-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Pluggable Authentication Module for Face based Authentication.

%description -l pl.UTF-8
Modularny system uwierzytelniania PAM opearty o weryfikację twarzy.

%prep
%setup -q -n pam-face-authentication-%{version}
%patch -P0 -p1

# use cmake file provided by opencv-devel
rm cmake/modules/FindOpenCV.cmake

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# wtf?
mv $RPM_BUILD_ROOT{%{_prefix}/kde/4/bin,%{_bindir}}/xwindowFaceAuth

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS README
%attr(755,root,root) /%{_lib}/security/pam_face_authentication.so
%attr(755,root,root) %{_bindir}/qt-facetrainer
%attr(755,root,root) %{_bindir}/xwindowFaceAuth
%{_desktopdir}/qt-facetrainer.desktop
%{_datadir}/haarcascade.xml
%{_datadir}/haarcascade_eye.xml
%{_datadir}/haarcascade_eye_tree_eyeglasses.xml
%{_datadir}/haarcascade_nose.xml
%{_iconsdir}/pfa-logo.png
