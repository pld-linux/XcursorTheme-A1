%define		_name A1
Summary:	X11 cursor theme - A1
Summary(pl):	Motyw kursorów dla X11 - A1
Name:		XcursorTheme-%{_name}
Version:	0.3
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/12651-A-1.tar.gz
# Source0-md5:	9eb747663e962463eac4f34b56658165
URL:		http://www.kde-look.org/content/show.php?content=12651
BuildRequires:	XFree86 >= 4.3
BuildArch:	noarch
Requires:	XFree86 >= 4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A blue/white aqua-like cursor theme.

%description -l pl
Bia³o-niebieski aquopodobny motyw kursorów.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}
%{__tar} xfz %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}/
rm -f $RPM_BUILD_ROOT%{_iconsdir}/README
echo "[Icon Theme]" > $RPM_BUILD_ROOT%{_iconsdir}/A-1/index.theme
echo "Name = A-1" >> $RPM_BUILD_ROOT%{_iconsdir}/A-1/index.theme
echo "Comment = A blue/white aqua-like cursor theme." >> $RPM_BUILD_ROOT%{_iconsdir}/A-1/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/A-1
