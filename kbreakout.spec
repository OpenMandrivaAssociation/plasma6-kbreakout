#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	Breakout like game
Name:		kbreakout
Version:	26.08.1
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		https://www.kde.org/applications/games/kbreakout/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kbreakout/-/archive/%{gitbranch}/kbreakout-%{gitbranchd}.tar.bz2#/kbreakout-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kbreakout-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KDEGames6)

Requires: qml(org.kde.games.core)

%rename plasma6-kbreakout

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KBreakout is a Breakout-like game.

Its object is to destroy as many bricks as possible without losing the ball.

%files -f kbreakout.lang
%{_datadir}/qlogging-categories6/kbreakout.categories
%{_bindir}/kbreakout
%{_datadir}/applications/org.kde.kbreakout.desktop
%{_datadir}/kbreakout
%{_datadir}/metainfo/org.kde.kbreakout.appdata.xml
%{_iconsdir}/hicolor/*/apps/kbreakout.*
