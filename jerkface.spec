Name:           jerkface
Version:        0.1
Release:        1
Summary:        jerkface adapted from GNU hello for testing package building

License:        GPLv3+
URL:            https://gafusion.github.io/OMFIT-source/
Source0:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

BuildRequires: gettext gcc

Requires(post): info gcc
Requires(preun): info gcc

%description
Calm down, it's just a stupid test

%define __debug_package %{nil}
%prep
%autosetup


%build
%configure
make %{?_smp_mflags}


%install
%make_install
%find_lang %{name}
rm -f %{buildroot}/%{_infodir}/dir
#rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
/sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files -f %{name}.lang
%{_bindir}/jerkface
%{_mandir}/man1/jerkface.1.*
%{_infodir}/jerkface.info.*
#%%license add-license-file-here
%doc jerkface.*



%changelog
* Fri Feb  8 2019 David Eldon <eldond@fusion.gat.com> - 0.1-1
- Initialization

