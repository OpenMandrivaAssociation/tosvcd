%define name	tosvcd
%define version	0.9
%define release %mkrel 7

Name: 	 	%{name}
Summary: 	Makes (super) video CD's from digital video recorder files
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://muse.seh.de/tosvcd/
License:	GPL
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	mjpegtools vcdimager cdrdao
ExclusiveArch: %ix86

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



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.9-7mdv2010.0
+ Revision: 434405
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9-6mdv2009.0
+ Revision: 261631
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9-5mdv2009.0
+ Revision: 254693
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.9-3mdv2008.1
+ Revision: 135863
- use ExclusiveArch instead
- BuildArch: %%ix86
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import tosvcd


* Sun Jun 6 2004 Austin Acton <austin@mandrake.org> 0.9-2mdk
- rebuild

* Wed Jun 4 2003 Austin Acton <aacton@yorku.ca> 0.9-1mdk
- initial package
