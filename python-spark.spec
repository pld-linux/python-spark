
%define 	module	spark

Summary:	Scanning, Parsing, and Rewriting Kit
Name:		python-%{module}
Version:	0.6.1
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://pages.cpsc.ucalgary.ca/~aycock/spark/%{module}-%{version}.tar.gz
# Source0-md5:	6c056b261782c51f53ceccbf86c08749
#Patch0:		%{name}-lib64.patch
URL:		http://pages.cpsc.ucalgary.ca/~aycock/spark/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SPARK stands for the Scanning, Parsing, and Rewriting Kit. It formerly had
no name, and was referred to as the "little language framework."

%prep
%setup -q	-n %{module}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{py_sitescriptdir}
install spark.py $RPM_BUILD_ROOT%{py_sitescriptdir}

# kill links to spark module
find examples -name spark.py

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* examples
%{py_sitescriptdir}/spark.py[co]
