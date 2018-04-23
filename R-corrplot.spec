#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-corrplot
Version  : 0.84
Release  : 5
URL      : https://cran.r-project.org/src/contrib/corrplot_0.84.tar.gz
Source0  : https://cran.r-project.org/src/contrib/corrplot_0.84.tar.gz
Summary  : Visualization of a Correlation Matrix
Group    : Development/Tools
License  : GPL-2.0
Requires: R-RColorBrewer
Requires: R-evaluate
Requires: R-markdown
Requires: R-stringi
BuildRequires : R-RColorBrewer
BuildRequires : R-evaluate
BuildRequires : R-markdown
BuildRequires : R-stringi
BuildRequires : clr-R-helpers

%description
It also contains some algorithms to do matrix reordering. In addition,
    corrplot is good at details, including choosing color, text labels,
    color labels, layout, etc.

%prep
%setup -q -c -n corrplot

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523296306

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523296306
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library corrplot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library corrplot
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library corrplot
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library corrplot|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/corrplot/CITATION
/usr/lib64/R/library/corrplot/DESCRIPTION
/usr/lib64/R/library/corrplot/INDEX
/usr/lib64/R/library/corrplot/Meta/Rd.rds
/usr/lib64/R/library/corrplot/Meta/features.rds
/usr/lib64/R/library/corrplot/Meta/hsearch.rds
/usr/lib64/R/library/corrplot/Meta/links.rds
/usr/lib64/R/library/corrplot/Meta/nsInfo.rds
/usr/lib64/R/library/corrplot/Meta/package.rds
/usr/lib64/R/library/corrplot/Meta/vignette.rds
/usr/lib64/R/library/corrplot/NAMESPACE
/usr/lib64/R/library/corrplot/NEWS
/usr/lib64/R/library/corrplot/R/corrplot
/usr/lib64/R/library/corrplot/R/corrplot.rdb
/usr/lib64/R/library/corrplot/R/corrplot.rdx
/usr/lib64/R/library/corrplot/doc/corrplot-intro.R
/usr/lib64/R/library/corrplot/doc/corrplot-intro.Rmd
/usr/lib64/R/library/corrplot/doc/corrplot-intro.html
/usr/lib64/R/library/corrplot/doc/index.html
/usr/lib64/R/library/corrplot/help/AnIndex
/usr/lib64/R/library/corrplot/help/aliases.rds
/usr/lib64/R/library/corrplot/help/corrplot.rdb
/usr/lib64/R/library/corrplot/help/corrplot.rdx
/usr/lib64/R/library/corrplot/help/paths.rds
/usr/lib64/R/library/corrplot/html/00Index.html
/usr/lib64/R/library/corrplot/html/R.css
