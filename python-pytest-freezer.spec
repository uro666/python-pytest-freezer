%define module pytest-freezer
%define oname pytest_freezer
# disable test on abf
%bcond_with test

Name:		python-pytest-freezer
Version:	0.4.9
Release:	1
Summary:	Pytest plugin providing a fixture interface for spulec/freezegun
URL:		https://pypi.org/project/pytest-freezer/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-freezer/%{oname}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(flit-core) >= 3.2
BuildRequires:	python%{pyver}dist(freezegun) >= 1.1
BuildRequires:	python%{pyver}dist(pip)
%if %{with test}
BuildRequires:	python%{pyver}dist(pytest) >= 3.6
%endif
Requires:	python%{pyver}dist(freezegun) >= 1.1
Requires:	python%{pyver}dist(pytest) >= 3.6


%description
Pytest plugin providing a fixture interface for spulec/freezegun

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%py_build

%install
%py3_install

%if %{with test}
%check
pip install -e .[test]
pytest -v tests/
%endif

%files
%{py_sitedir}/%{oname}.py
%{py_sitedir}/__pycache__/%{oname}*.pyc
%{py_sitedir}/%{oname}-%{version}.dist-info
%license LICENSE
%doc README.md
