Summary:	Gnickr! - Flickr! photo manager
Summary(pl.UTF-8):   Gnickr! - zarządca zdjęć Flickr!
Name:		gnickr
Version:	0.0.3
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/gnickr/%{name}-%{version}.tar.gz
# Source0-md5:	e5ef6d0434d692660ead9b16b160e169
URL:		http://gnickr.sourceforge.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-Imaging-devel
BuildRequires:	python-devel
BuildRequires:	python-gnome-devel >= 2.12.3
BuildRequires:	python-pygtk-devel
%pyrequires_eq	python-modules
Requires:	gtk+2 >= 2:2.8.0
Requires:	python-Imaging
Requires:	python-gnome
Requires:	python-pygtk-gtk >= 2:2.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnickr allows you to manage photos on your Flickr site as if they
were local files on your Gnome desktop. It does this by creating
a Flickr virtual filesystem.

%description -l pl.UTF-8
Gnickr umożliwia zarządzanie zdjęciami na stronie Flickr tak, jakby
były lokalnymi plikami na pulpicie GNOME. Robi to poprzez utworzenie
wirtualnego systemu plików Flickr.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnickr.schemas

%preun
%gconf_schema_uninstall gnickr.schemas

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*.py?
%{_libdir}/gnome-vfs-2.0/modules/*.py?
%{_sysconfdir}/gnome-vfs-2.0/modules/flickr.conf
%{_sysconfdir}/gconf/schemas/gnickr.schemas
