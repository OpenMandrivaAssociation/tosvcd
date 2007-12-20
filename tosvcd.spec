%define name	tosvcd
%define version	0.9
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	Makes (super) video CD's from digital video recorder files
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://muse.seh.de/tosvcd/
License:	GPL
Group:		Video
Requires:	mjpegtools vcdimager cdrdao
BuildArch: %ix86

%description
ToSVCD takes one or more recorded VDR files and transcodes them to a SVCD
image file ready for cdrdao to burn.
Features include:
    * synchronises Video/Audio
    * tries to repair demaged streams
    * split output(with help of mpeg2enc)
    * invoke yuvscaler, if input is not 480x576
    * invoke noise filter on request
    * predicts finish time
    * predicts final output size
    * restarts if output size exceeds CD's capacity
    * invoke mplex and vcdimager 

%prep
%setup -q
perl -p -i -e 's|su -c|echo||g' makefile

%build
%make
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp %name $RPM_BUILD_ROOT/%_bindir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_bindir}/%name

