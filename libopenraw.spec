Name:           libopenraw
Version:        0.0.5
Release:        4.1%{?dist}
Summary:        Decode camera RAW files

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://%{name}.freedesktop.org/wiki
Source0:        http://%{name}.freedesktop.org/download/%{name}-%{version}.tar.gz
Patch0:         libopenraw-0.0.5-includes.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  boost-devel
BuildRequires:  libjpeg-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  chrpath
BuildRequires:  libxml2-devel


%description
libopenraw is an ongoing project to provide a free software
implementation for camera RAW files decoding. One of the main reason is
that dcraw is not suited for easy integration into applications, and
there is a need for an easy to use API to build free software digital
image processing application.


%package        gnome
Summary:        GUI components of %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    gnome 
The %{name}-gnome package contains gui components of %{name}.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        gnome-devel
Summary:        Development files for %{name}-gnome
Group:          Development/Libraries
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       pkgconfig

%description    gnome-devel
The %{name}-gnome-devel package contains libraries and header files for
developing applications that use %{name}-gnome.


%prep
%setup -q
%patch0 -p1 -b .includes


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
chrpath --delete $RPM_BUILD_ROOT/%{_libdir}/libopenrawgnome.so.1.4.0

%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%post gnome -p /sbin/ldconfig
%postun gnome -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO 
%{_libdir}/%{name}.so.*


%files gnome
%defattr(-,root,root,-)
%{_libdir}/%{name}gnome.so.*


%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/%{name}-1.0
%{_includedir}/%{name}-1.0/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}-1.0.pc


%files gnome-devel
%defattr(-,root,root,-)
%{_includedir}/%{name}-1.0/%{name}-gnome
%{_libdir}/%{name}gnome.so
%{_libdir}/pkgconfig/%{name}-gnome-1.0.pc


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.0.5-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Caolán McNamara <caolanm@redhat.com> - 0.0.5-3
- add stdio.h for fopen and friends

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 04 2008 Trond Danielsen <trond.danielsen@gmail.com> - 0.0.5-1
- New upstream version.

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.4-3
- Autorebuild for GCC 4.3

* Wed Jan 30 2008 Trond Danielsen <trond.danielsen@gmail.com> - 0.0.4-2
- Added missing dependency on libxml

* Wed Jan 30 2008 Trond Danielsen <trond.danielsen@gmail.com> - 0.0.4-1
- New upstream version.

* Fri Dec 28 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.0.3-1
- New upstream version.
- Updated license tag.
- Fixed rpath error.

* Thu May 03 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.0.2-5
- Added unowned directory to list of files.
- Changed license from GPL to LGPL.

* Wed May 02 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.0.2-4
- Moved gui components to a separate package.

* Tue May 01 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.0.2-3
- Added missing BuildRequirement.

* Mon Apr 30 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.0.2-2
- Added missing BuildRequirement.

* Sun Apr 29 2007 Trond Danielsen <trond.danielsen@gmail.com> - 0.0.2-1
- Inital version.
