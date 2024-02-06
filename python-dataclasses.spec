# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-dataclasses
Epoch: 100
Version: 0.8
Release: 1%{?dist}
BuildArch: noarch
Summary: PEP 557 Data Classes implementation
License: Apache-2.0
URL: https://github.com/ericvsmith/dataclasses/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This is an implementation of PEP 557, Data Classes. It is a backport for
Python 3.6.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-dataclasses
Summary: PEP 557 Data Classes implementation
Requires: python3
Provides: python3-dataclasses = %{epoch}:%{version}-%{release}
Provides: python3dist(dataclasses) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dataclasses = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dataclasses) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dataclasses = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dataclasses) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-dataclasses
This is an implementation of PEP 557, Data Classes. It is a backport for
Python 3.6.

%files -n python%{python3_version_nodots}-dataclasses
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-dataclasses
Summary: PEP 557 Data Classes implementation
Requires: python3
Provides: python3-dataclasses = %{epoch}:%{version}-%{release}
Provides: python3dist(dataclasses) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dataclasses = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dataclasses) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dataclasses = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dataclasses) = %{epoch}:%{version}-%{release}

%description -n python3-dataclasses
This is an implementation of PEP 557, Data Classes. It is a backport for
Python 3.6.

%files -n python3-dataclasses
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog
