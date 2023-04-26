%global octpkg json

# (mandian)
# NOTE this package is obsolete because this code is now merged in octave >=7

# FIXME: it's like rapidjson upstreamer has not release a new
#        version since 2015 so packaged version is too old
%global rapidjson_commit 8261c1ddf43f10de00fd8c9a67811d1486b2c784

Summary:	JSON support by Matlab compatible (jsondecode / jsonencode) functions
Name:		octave-json
Version:	1.5.0
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/json/
Url:		https://github.com/gnu-octave/pkg-json/
Source0:	https://github.com/gnu-octave/pkg-json/archive/v%{version}/json-%{version}.tar.gz
Source1:	https://github.com/Tencent/rapidjson/archive/%{rapidjson_commit}/rapidjson-%{rapidjson_commit}.zip
Patch0:		%{name}-1.5.0-unbundle_rapidjson.patch

BuildRequires:  octave-devel >= 5.1.0
BuildRequires:  octave-devel < 7.0.0
BuildRequires:	pkgconfig(RapidJSON)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
JSON support by Matlab compatible (jsondecode / jsonencode) functions.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n pkg-%{octpkg}-%{version} -a1

mv rapidjson-%{rapidjson_commit} src/rapidjson

# remove backup files
find . -name \*~ -delete

%build
export CXXFLAGS="%{optflags} -std=c++11"
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

