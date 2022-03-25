#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Cubic-to-quadratic Bezier curve conversion
Summary(pl.UTF-8):	Konwersja krzywych Beziera stopnia trzeciego do drugiego
Name:		python-cu2qu
Version:	1.6.7.post1
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/cu2qu/
Source0:	https://files.pythonhosted.org/packages/source/c/cu2qu/cu2qu-%{version}.zip
# Source0-md5:	6858c0b17180d009765006f0b81b73d3
URL:		https://pypi.org/project/cu2qu/
%if %{with python2}
BuildRequires:	python-Cython
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-defcon >= 0.6.0
# fonttools[ufo]
BuildRequires:	python-fonttools >= 3.32.0
BuildRequires:	python-fs >= 2.2
BuildRequires:	python-pytest >= 2.8
%endif
%endif
%if %{with python3}
BuildRequires:	python3-Cython
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-defcon >= 0.6.0
BuildRequires:	python3-fonttools >= 3.32.0
BuildRequires:	python3-fs >= 2.2
BuildRequires:	python3-pytest >= 2.8
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python-modules >= 1:2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides functions which take in UFO objects (Defcon
Fonts or Robofab RFonts) and converts any cubic curves to quadratic.

%description -l pl.UTF-8
Ta biblioteka udostępnia funkcje przyjmujące obiekty UFO (Font z
biblioteki Defcon albo RFont z Robofab) i konwertujące krzywe
trzeciego stopnia do drugiego.

%package -n python3-cu2qu
Summary:	Cubic-to-quadratic Bezier curve conversion
Summary(pl.UTF-8):	Konwersja krzywych Beziera stopnia trzeciego do drugiego
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-cu2qu
This library provides functions which take in UFO objects (Defcon
Fonts or Robofab RFonts) and converts any cubic curves to quadratic.

%description -n python3-cu2qu -l pl.UTF-8
Ta biblioteka udostępnia funkcje przyjmujące obiekty UFO (Font z
biblioteki Defcon albo RFont z Robofab) i konwertujące krzywe
trzeciego stopnia do drugiego.

%prep
%setup -q -n cu2qu-%{version}

%build
%if %{with python2}
%py_build \
	--with-cython

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/Lib \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build \
	--with-cython

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/Lib \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/cu2qu{,-2}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/cu2qu/*.c

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/cu2qu/*.c
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/cu2qu-2
%dir %{py_sitedir}/cu2qu
%attr(755,root,root) %{py_sitedir}/cu2qu/cu2qu.so
%{py_sitedir}/cu2qu/*.py[co]
%{py_sitedir}/cu2qu-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-cu2qu
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/cu2qu
%dir %{py3_sitedir}/cu2qu
%attr(755,root,root) %{py3_sitedir}/cu2qu/cu2qu.cpython-*.so
%{py3_sitedir}/cu2qu/*.py
%{py3_sitedir}/cu2qu/__pycache__
%{py3_sitedir}/cu2qu-%{version}-py*.egg-info
%endif
