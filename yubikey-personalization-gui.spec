Summary:	GUI for Yubikey personalization
Name:		yubikey-personalization-gui
Version:	3.1.25
Release:	1
License:	BSD
URL:		https://developers.yubico.com/yubikey-personalization-gui/
Source0:	https://developers.yubico.com/yubikey-personalization-gui/Releases/%{name}-%{version}.tar.gz
BuildRequires:	imagemagick
BuildRequires:	libyubikey-devel
BuildRequires:	pkgconfig(ykpers-1)
BuildRequires:	qt5-devel

%description
Yubico's YubiKey can be re-programmed with a new AES key. This is a graphical
tool that makes this an easy task.

%files
%license COPYING
%doc NEWS README ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%{qmake_qt5} \
	"CONFIG+=%{vendor}"
%make_build

%install
#make_install -C build

# binary
install -Dpm 0755 build/release/%{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dpm 0644 resources/lin/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# .desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
	resources/lin/%{name}.desktop

# icons
for d in 16 32 48 64 72 128 256
do
	install -dm 755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	convert -background none resources/lin/%{name}.png \
		-scale ${d}x${d} %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
install -pm 0644 resources/lin/%{name}.xpm %{buildroot}/%{_datadir}/pixmaps/


