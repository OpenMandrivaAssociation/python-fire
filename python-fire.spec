Name:           python-fire
Version:        0.7.1
Release:        2
Summary:        A library for automatically generating command line interfaces
License:        Apache-2.0
Group:          Development/Python
URL:            https://github.com/google/python-fire
Source:         https://files.pythonhosted.org/packages/source/f/fire/fire-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python%{pyver}dist(termcolor)
BuildArch:	noarch

%description
Python Fire is a library for automatically generating command line
interfaces (CLIs) from a Python object.

%files
%license LICENSE
%{python_sitelib}/fire
%{python_sitelib}/fire-%{version}.dist-info
