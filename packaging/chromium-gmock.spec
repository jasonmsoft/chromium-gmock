
Name:           chromium-gmock
Version:        0.1
Release:        0
Summary:        gmock third-party for Chromium
License:        Apache-2.0
Group:          Development/Tools
Url:            http://code.google.com/p/googlemock/

Source0:        %name-%version.tar.xz
Source1:        %name.manifest

%description
Google's framework for writing and using C++ mock classes on a variety of platforms. It can help you derive better designs of your system and write better tests. (PATCHED BY CHROMIUM)

%prep
%setup -q
cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_datadir}/chromium/testing/gmock
cp -dr --no-preserve=ownership * %{buildroot}%{_datadir}/chromium/testing/gmock
rm -rf %{buildroot}%{_datadir}/chromium/testing/gmock/.git
rm -f %{buildroot}%{_datadir}/chromium/testing/gmock/.gitignore

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license LICENSE
%{_datadir}/chromium/testing/gmock/*

%changelog
