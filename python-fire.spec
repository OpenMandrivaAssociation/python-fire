Name:           python-fire
Version:        0.7.0
Release:        1
Summary:        A library for automatically generating command line interfaces
License:        Apache-2.0
URL:            https://github.com/google/python-fire
Source:         https://files.pythonhosted.org/packages/source/f/fire/fire-%{version}.tar.gz

BuildSystem:  python
BuildRequires:  python-setuptools
Requires:       python-termcolor
BuildArch:      noarch

%description
Python Fire is a library for automatically generating command line
interfaces (CLIs) from a Python object.

%files
%license LICENSE
%{python_sitelib}/fire
%{python_sitelib}/fire-*.egg-info
