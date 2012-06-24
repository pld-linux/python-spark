
%define 	module	spark

Summary:	Scanning, Parsing, and Rewriting Kit
Summary(pl):	Narz�dzia do skanowania, analizowania i przepisowania
Name:		python-%{module}
Version:	0.6.1
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://pages.cpsc.ucalgary.ca/~aycock/spark/%{module}-%{version}.tar.gz
# Source0-md5:	28c4c3b1031a6a4e4c4bd42726d22b65
URL:		http://pages.cpsc.ucalgary.ca/~aycock/spark/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SPARK stands for the Scanning, Parsing, and Rewriting Kit. It formerly
had no name, and was referred to as the "little language framework."

%description -l pl
SPARK (Scanning, Parsing And Rewriting Kit) to zestaw narz�dzi do
skanowania, analizowania i przepisywania. Poprzednio nie mia� nazwy, a
pisano o nim jako o "ma�ym szkielecie j�zyka" ("little language
framework").

%prep
%setup -q -n %{module}-%{version}

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
