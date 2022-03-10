%global octpkg json

# FIXME: it's like rapidjson upstreamer has not release a new
#        version since 2015 so packaged version is too old
%global rapidjson_commit 8261c1ddf43f10de00fd8c9a67811d1486b2c784

Summary:	JSON support by Matlab compatible (jsondecode / jsonencode) functions.
Name:		octave-%{octpkg}
Version:	1.5.0
Release:	1
Source0:	%{url}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
Source1:	https://github.com/Tencent/rapidjson/archive/%{rapidjson_commit}/rapidjson-%{rapidjson_commit}.zip
Patch0:		%{name}-1.5.0-unbundle_rapidjson.patch
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://github.com/gnu-octave/pkg-%{octpkg}/

BuildRequires:	octave-devel >= 5.1.0
BuildRequires:	pkgconfig(RapidJSON)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
JSON support by Matlab compatible (jsondecode / jsonencode) functions.

%files
%license COPYING
#doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n pkg-%{octpkg}-%{version} -a1

mv rapidjson-%{rapidjson_commit} src/rapidjson

# remove backup files
find . -name \*~ -delete
#exit 1
%build
CXXFLAGS="%{optflags} -std=c++11"
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

