%define pkgname consolamono

Summary:	Consola Mono Book typeface
Name:		fonts-ttf-consolamono
Version:	20110922
Release:	1
License:	OFL
Group:		System/Fonts/True type
URL:		http://openfontlibrary.org/font/consolamono
Source0:	%{pkgname}.zip
BuildArch:	noarch
BuildRequires:	freetype-tools

%description
Monospaced font Consola Mono.

%prep
%setup -q -n 'Consola Mono'

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/consolamono

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/consolamono
ttmkfdir %{buildroot}%{_xfontdir}/TTF/consolamono -o %{buildroot}%{_xfontdir}/TTF/consolamono/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/consolamono/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/consolamono \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-consolamono:pri=50

%files
%doc *.txt
%dir %{_xfontdir}/TTF/consolamono
%{_xfontdir}/TTF/consolamono/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/consolamono/fonts.dir
%{_xfontdir}/TTF/consolamono/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-consolamono:pri=50


%changelog
* Wed Dec 14 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 20110922-1
+ Revision: 741114
- imported package fonts-ttf-consolamono

