Summary:	A Kmenu replacement
Summary(pl.UTF-8):	Zamiennik menu KDE
Name:		tastymenu
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.notmart.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	1c8c879db84a4fa75b0b83f11022352b
URL:		http://kde-apps.org/content/show.php?content=41866
BuildRequires:	kdebase-devel
BuildRequires:	kdelibs-devel >= 9:%{_kdever}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tasty Menu is a KMenu replacement aiming to provide the maximum
usability, or at least to be a testbed for usability concepts and
ideas for a future KDE menu.

%description -l pl.UTF-8
Tasty Menu to zamiennik standardowego menu KDE, którego założeniem
jest udostępnianie maksymalnej użyteczności lub przynajmniej poletko
testowe dla idei i koncepcji przyszłych wersji menu KDE.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir="%{_kdedocdir}"

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/tastymenu_panelapplet.so
%{_datadir}/config.kcfg/tastymenu.kcfg
%{_datadir}/apps/kicker/applets/tastymenu.desktop
