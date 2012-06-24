#
# Conditional build:
%bcond_without	fpx	# without FlashPIX module (which uses fpx library)
%bcond_with	gs	# with PostScript support through ghostscript library (warning: breaks jpeg!)
%bcond_without	jasper	# without JPEG2000 module (which uses jasper library)
%bcond_without	cxx	# without Magick++
#
%include	/usr/lib/rpm/macros.perl
%define		ver 6.1.8
%define		pver	9
%define		QuantumDepth	16
Summary:	Image display, conversion, and manipulation under X
Summary(de):	Darstellen, Konvertieren und Bearbeiten von Grafiken unter X
Summary(es):	Exhibidor, convertidor y manipulador de im�genes bajo X
Summary(fr):	Visualisation, conversion, et manipulation d'images sous X
Summary(pl):	Narz�dzie do wy�wietlania, konwersji i manipulacji grafikami
Summary(pt_BR):	Exibidor, conversor e manipulador de imagens sob X
Summary(ru):	��������, ���������������, ��������� ����������� ��� X Window
Summary(tr):	X alt�nda resim g�sterme, �evirme ve de�i�iklik yapma
Summary(uk):	��������, ������������� �� ������� ��������� Ц� X Window
Name:		ImageMagick
Version:	%{ver}%{?pver:.%{pver}}
Release:	1
Epoch:		1
License:	Apache-like
Group:		X11/Applications/Graphics
Source0:	http://www.imagemagick.org/download/%{name}-%{ver}-%{pver}.tar.gz
# Source0-md5:	d741987e6ce0bbd413c0d3fbce49caaa
#Source0:	http://dl.sourceforge.net/imagemagick/%{name}-%{ver}.tar.bz2
Patch0:		%{name}-libpath.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-system-libltdl.patch
Patch3:		%{name}-fpx.c.patch
Patch4:		%{name}-free.patch
URL:		http://www.imagemagick.org/
BuildRequires:	XFree86-DPS-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	bzip2-devel >= 1.0.1
BuildRequires:	expat-devel >= 1.95.7
BuildRequires:	freetype-devel >= 2.0.2-2
BuildRequires:	gd-devel >= 2.0.15
%{?with_gs:BuildRequires:	ghostscript-devel}
BuildRequires:	graphviz-devel >= 1.12
%{?with_jasper:BuildRequires:	jasper-devel >= 1.700.5}
BuildRequires:	jbigkit-devel
BuildRequires:	lcms-devel
%{?with_fpx:BuildRequires:	libfpx-devel >= 1.2.0.4-3}
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libwmf-devel >= 2:0.2.2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# only checked for, but only supplied scripts/txt2html is used
#BuildRequires:	txt2html
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	ImageMagick-coder-mpeg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# we don't want "-s" here, because it would be added to `Magick*-config --ldflags`
%define		rpmldflags	%{nil}
%define		modulesdir	%{_libdir}/ImageMagick-%{ver}/modules-Q%{QuantumDepth}

%description
ImageMagick is an image display, conversion, and manipulation tool. It
runs under X Window. It is very powerful in terms of it's ability to
allow the user to edit images. It can handle many different formats as
well.

%description -l de
ImageMagick ist ein Tool zur Bildanzeige, -konvertierung und
manipulation, -das unter X-Window l�uft. Es ist enorm leitungsf�hig
in Bezug auf die Grafikmanipulationsfunktionen, die es dem Anwender
bietet, und auf die Vielfalt der unterst�tzten Formate.

%description -l es
ImageMagick es una herramienta para manipular, convertir y exhibir
im�genes, que funciona bajo X Window. Es una herramienta potente que
permite editar im�genes, pudiendo manipular varios formatos
diferentes.

%description -l fr
ImageMagick est un outil d'affichage, de conversion et de manipulation
d'images. Il tourne sous X Window et est tr�s puissant en termes de
capacit� d'�dition des images. Il peut aussi g�rer de nombreux formats
diff�rents.

%description -l pl
ImageMagick jest narz�dziem do manipulacji, konwersji i wy�wietlania.
W sk�ad pakietu wchodz� zar�wno narz�dzia X Window jak i do u�ywania z
linii polece� umo�liwiaj�ce edycj� plik�w graficznych. Narz�dzia z
pakietu ImageMagick potrafi� obs�u�y� wiele r�nych format�w
graficznych.

%description -l pt_BR
ImageMagick � uma ferramenta para manipular, converter e exibir
imagens, que funciona sob o X Window. � uma ferramenta poderosa que
permite editar imagens, podendo tratar v�rios formatos diferentes.

%description -l ru
ImageMagick - ��� ������� ��� ���������, ��������������� � ���������
�����������. ��� �������� ��� X Window. ImageMagick �������������
������������ ������� ����������� �� ��������� ����������� � �����
������������� ��������.

%description -l tr
ImageMagick bir resim g�sterme, �evirme ve de�i�iklik yapma
program�d�r. X Window pencereleme sistemi alt�nda �al���r. Kullan�c�ya
resimler �zerinde de�i�iklik yapma a��s�ndan pek �ok olanak sunar. Bir
�ok resim bi�imini rahatl�kla kullanabilir.

%description -l uk
ImageMagick - �� ���̦�� ��� ���������, ������������� �� �������
���������. ���� ������ Ц� X Window. ImageMagick ��� �����������
����˦ ��������Ԧ �� �����æ ��������� � Ҧ�����Φ���� ��������.

%package doc
Summary:	ImageMagick documentation
Summary(pl):	Dokumentacja do ImageMagick
Group:		Documentation

%description doc
Documentation for ImageMagick.

%description doc -l pl
Dokumentacja do ImageMagick.

%package libs
Summary:	ImageMagick libraries
Summary(pl):	Biblioteki ImageMagick
Summary(pt_BR):	Bibliotecas din�micas do ImageMagick
Group:		X11/Libraries

%description libs
ImageMagick libraries.

%description libs -l pl
Biblioteki ImageMagick.

%description libs -l pt_BR
Bibliotecas din�micas do ImageMagick.

%package devel
Summary:	Libraries and header files for ImageMagick development
Summary(es):	Biblioteca est�tica y archivos de inclusi�n para desarrollo con libMagick
Summary(pl):	Biblioteki i pliki nag��wkowe dla ImageMagick
Summary(pt_BR):	Biblioteca e arquivos de inclus�o para desenvolvimento com libMagick
Summary(ru):	������ � ���������� ��� ���������������� � ImageMagick
Summary(uk):	������ �� ¦�̦����� ��� ������������� � ImageMagick
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	XFree86-devel
Requires:	bzip2-devel
Requires:	freetype-devel
Requires:	lcms-devel
Requires:	libltdl-devel
Requires:	libjpeg-devel
Requires:	libtiff-devel
Requires:	zlib-devel

%description devel
This is the ImageMagick development package. It includes header files
for use in developing your own applications that make use of the
ImageMagick code and/or APIs.

%description devel -l de
Dies ist das ImageMagick-Entwicklerpaket. Es enth�lt Header-Dateien
zum Entwickeln von Anwendungen, die ImageMagick-Code und/oder -APIs
nutzen.

%description devel -l es
Este es el paquete de desarrollo ImageMagick. Incluye las bibliotecas
y los archivos de inclusi�n para el desarrollo de sus propias
aplicaciones que hacen uso del c�digo ImageMagick y/el APIs.

%description devel -l fr
Paquetage de d�veloppement ImageMagick. Contient les biblioth�ques
statiques et les en-t�tes utilis�s pour cr�er vos propres applications
utilisant le code d'ImageMagick et/ou ses APIs.

%description devel -l pl
Pakiet ten zawieraja pliki potrzebne przy kompilowaniu program�w
wykorzystuj�cych blibliotek� ImageMagick takie jak pliki nag��wkowe i
dokumentacj� niezb�dn� przy pisaniu w�asnych program�w z
wykorzystaniem API jakie udost�pnia ImageMagick.

%description devel -l pt_BR
Este � o pacote de desenvolvimento ImageMagick. Inclui as bibliotecas
e os arquivos de inclus�o para o desenvolvimento de suas pr�prias
aplica��es que fazem uso do c�digo ImageMagick e/ou APIs.

%description devel -l ru
��� ����� ������������ ��� ���������������� � ImageMagick. �� ��������
������ � ���������� ��� ������������� � ����������, ������� ����������
��� ��� API ImageMagick.

%description devel -l tr
Bu paket, ImageMagick uygulama aray�z�n� kullanan programlar
geli�tirmek i�in gereken ba�l�k dosyalar�n� ve kitapl�klar� i�erir.

%description devel -l uk
�� ����� ��� ������������� � ImageMagick. ��� ͦ����� ������ ��
¦�̦����� ��� ������������ � ���������, �� �������������� ��� ��� API
ImageMagick.

%package static
Summary:	ImageMagick static libraries
Summary(pl):	Biblioteki statyczne ImageMagick
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com libMagick
Summary(ru):	����������� ���������� ��� ���������������� � ImageMagick
Summary(uk):	������Φ ¦�̦����� ��� ������������� � ImageMagick
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
ImageMagick static libraries.

%description static -l pl
Biblioteki statyczne ImageMagick.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com libMagick.

%description static -l ru
��� ��������� ����� �� ������������ ������������, ������� ������ ��
������ � ImageMagick-devel.

%description static -l uk
�� ������� ����� ڦ ���������� ¦�̦�������, �˦ ¦���� �� ������� ��
������ ImageMagick-devel.

%package perl
Summary:	Libraries and modules for access to ImageMagick from Perl
Summary(pl):	Biblioteki i modu�y Perla dla ImageMagick
Summary(pt_BR):	M�dulo perl para uso com o ImageMagick
Summary(ru):	���������� � ������ ��� ������� � ImageMagick �� perl
Summary(uk):	��̦����� �� ����̦ ��� ������� �� ImageMagick � Perl
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description perl
This is the ImageMagick Perl support package. It perl modules and
support files for access to ImageMagick library from perl without
unuseful forking or such.

%description perl -l pl
Biblioteki i modu�y umo�liwiaj�ce korzystanie z ImageMagick z poziomu
Perla.

%description perl -l pt_BR
Este pacote fornece um m�dulo perl para acessar fun��es do ImageMagick
em scripts Perl.

%description perl -l ru
��� ����� ImageMagick ��� ��������� perl. �� �������� ������ perl �
��������������� ����� ��� ������� � ���������� ImageMagick �� Perl.

%description perl -l uk
�� ����� ImageMagick ��� Ц������� Perl. ��� ͦ����� ����̦ Perl ��
�������צ ����� ��� ������� �� ¦�̦����� ImageMagick � Perl.

%package c++
Summary:	ImageMagick Magick++ library
Summary(pl):	Biblioteka Magick++
Summary(pt_BR):	Bibliotecas din�micas do ImageMagick
Summary(ru):	���������� Magick++ (C++ ��������� ��� ImageMagick'�)
Summary(uk):	��̦����� Magick++ (��������� C++ ��� ImageMagick)
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description c++
This package contains the Magick++ library, a C++ binding to the
ImageMagick graphics manipulation library.

Install ImageMagick-c++ if you want to use any applications that use
Magick++.

%description c++ -l pl
Pakiet zawiera bibliotek� Magick++ - interfejs w C++ do biblioteki
ImageMagick. Jest potrzebny do uruchamiania program�w korzystaj�cych z
Magick++.

%description c++ -l pt_BR
Bibliotecas din�micas C++ do ImageMagick.

%description c++ -l ru
Magick++ -- ��������-��������������� ����������, �������������� ��
���� C++ API ��� ImageMagick (���������� ��� ���������,
��������������� � ��������� �����������).

%description c++ -l uk
Magick++ -- ��'����-�Ҧ�������� ¦�̦�����, �� ���Ѥ ����� C++ API ���
ImageMagick (¦�̦����� ��� ���������, ������������� �� �������
���������).

%package c++-devel
Summary:	C++ bindings for the ImageMagick library
Summary(es):	Biblioteca est�tica y archivos de inclusi�n para desarrollo con libMagick++
Summary(pl):	Pliki nag��wkowe z interfejsem C++ do ImageMagick
Summary(pt_BR):	Biblioteca e arquivos de inclus�o para desenvolvimento com libMagick++
Summary(ru):	������ � ���������� ��� ���������� � �������������� Magick++ (C++ ��������� ��� ImageMagick'�)
Summary(uk):	������ �� ¦�̦����� ��� �������� � ������������� Magick++ (���������� C++ ��� ImageMagick)
Group:		X11/Development/Libraries
Requires:	%{name}-c++ = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
ImageMagick-c++-devel contains header files you'll need to develop
ImageMagick applications using the Magick++ C++ bindings. ImageMagick
is an image manipulation program.

If you want to create applications that will use Magick++ code or
APIs, you'll need to install ImageMagick-c++-devel, ImageMagick-devel
and ImageMagick. You don't need to install it if you just want to use
ImageMagick, or if you want to develop/compile applications using the
ImageMagick C interface, however.

%description c++-devel -l es
Este es el paquete de desarrollo ImageMagick. Incluye las bibliotecas
est�ticas y los archivos de inclusi�n para el desarrollo de sus
propias aplicaciones que hacen uso del c�digo ImageMagick y/el APIs.

%description c++-devel -l pl
Pakiet zawiera pliki nag��wkowe potrzebne do kompilowania program�w
korzystaj�cych z Magick++.

%description c++-devel -l pt_BR
Este � o pacote de desenvolvimento libMagick++. Inclui as bibliotecas
e os arquivos de inclus�o para o desenvolvimento de suas pr�prias
aplica��es C++ que fazem uso do c�digo ImageMagick e/ou APIs.

%description c++-devel -l ru
��� ����� ������������ ��� ���������������� � ImageMagick. �� ��������
������ � ���������� ��� ������������� � ����������, ������� ����������
��� ��� API Magick++ (C++ ��������� ��� ImageMagick'�).

%description c++-devel -l uk
�� ����� ��� ������������� � ImageMagick. ��� ͦ����� ������ ��
¦�̦����� ��� ������������ � ���������, �� �������������� ��� ��� API
Magick++ (��������� C++ ��� ImageMagick).

%package c++-static
Summary:	C++ bindings for the ImageMagick - static library
Summary(pl):	Interfejs C++ do ImageMagick - biblioteka statyczna
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com libMagick
Summary(ru):	����������� ���������� C++ ��� ���������������� � ImageMagick
Summary(uk):	������Φ ¦�̦����� C++ ��� ������������� � ImageMagick
Group:		X11/Development/Libraries
Requires:	%{name}-c++-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description c++-static
C++ bindings for the ImageMagick - static library.

%description c++-static -l pl
Biblioteka Magick++ w wersji statycznej.

%description c++-static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com libMagick++.

%description c++-static -l ru
��� ��������� ����� �� ������������ ������������, ������� ������ ��
������ � ImageMagick-c++-devel.

%description c++-static -l uk
�� ������� ����� ڦ ���������� ¦�̦�������, �˦ ¦���� �� ������� ��
������ ImageMagick-c++-devel.

%package coder-dot
Summary:	Coder module for GraphViz DOT files
Summary(pl):	Modu� kodera dla plik�w GraphViz DOT
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-dot
Coder module for GraphViz DOT files.

%description coder-dot -l pl
Modu� kodera dla plik�w GraphViz DOT.

%package coder-dps
Summary:	Coder module for Postscript files using DPS extension
Summary(pl):	Modu� kodera dla plik�w Postscript u�ywaj�cy rozszerzenia DPS
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-dps
Coder module for Postcript files using DPS (Display PostScript)
extension.

%description coder-dps -l pl
Modu� kodera dla plik�w Postscript u�ywaj�cy rozszerzenia DPS (Display
PostScript).

%package coder-fpx
Summary:	Coder module for FlashPIX (FPX) files
Summary(pl):	Modu� kodera dla plik�w FlashPIX (FPX)
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-fpx
Coder module for FlashPIX (FPX) files.

%description coder-fpx -l pl
Modu� kodera dla plik�w FlashPIX (FPX).

%package coder-jbig
Summary:	Coder module for JBIG files
Summary(pl):	Modu� kodera dla plik�w JBIG
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-jbig
Coder module for JBIG files.

%description coder-jbig -l pl
Modu� kodera dla plik�w JBIG.

%package coder-jpeg
Summary:	Coder module for JPEG files
Summary(pl):	Modu� kodera dla plik�w JPEG
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-jpeg
Coder module for JPEG files.

%description coder-jpeg -l pl
Modu� kodera dla plik�w JPEG.

%package coder-jpeg2
Summary:	Coder module for JPEG-2000 (JP2/JPC) files using JasPer library
Summary(pl):	Modu� kodera dla plik�w JPEG-2000 (JP2/JPC) u�ywaj�cy biblioteki JasPer
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-jpeg2
Coder module for JPEG-2000 (JP2/JPC) files using JasPer library.

%description coder-jpeg2 -l pl
Modu� kodera dla plik�w JPEG-2000 (JP2/JPC) u�ywajacy biblioteki
JasPer.

%package coder-miff
Summary:	Coder module for MIFF files
Summary(pl):	Modu� kodera dla plik�w MIFF
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-miff
Coder module for MIFF files.

%description coder-miff -l pl
Modu� kodera dla plik�w MIFF.

%package coder-mpr
Summary:	Coder module for ImageMagick MPR and MSL files
Summary(pl):	Modu� kodera dla plik�w MPR i MSL ImageMagick
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-mpr
Coder module for Magick Persistent Registry (MPR) and Magick Scripting
Language (MSL) files.

%description coder-mpr -l pl
Modu� kodera dla plik�w Magick Persistent Registry (MPR) i Magick
Scripting Language (MSL).

%package coder-pdf
Summary:	Coder module for PDF files
Summary(pl):	Modu� kodera dla plik�w PDF
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-pdf
Coder module for PDF files.

%description coder-pdf -l pl
Modu� kodera dla plik�w PDF.

%package coder-png
Summary:	Coder module for PNG files
Summary(pl):	Modul kodera dla plik�w PNG
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-png
Coder module for PNG files.

%description coder-png -l pl
Modu� kodera dla plik�w PNG.

%package coder-ps2
Summary:	Coder module for Postscript Level II & III (PS2/PS3) files
Summary(pl):	Modu� kodera dla plik�w Postscript Level II i III (PS2/PS3)
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-ps2
Coder module for Postscript Level II & III (PS2/PS3) files.

%description coder-ps2 -l pl
Modu� kodera dla plik�w Postscript Level II i III (PS2/PS3).

%package coder-svg
Summary:	Coder module for SVG (Scalable Vector Graphics) files
Summary(pl):	Modu� kodera dla plik�w SVG (Scalable Vector Graphics)
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-svg
Coder module for SVG (Scalable Vector Graphics) files.

%description coder-svg -l pl
Modu� kodera dla plik�w SVG (Scalable Vector Graphics).

%package coder-tiff
Summary:	Coder module for TIFF files
Summary(pl):	Modu� kodera dla plik�w TIFF
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-tiff
Coder module for TIFF files.

%description coder-tiff -l pl
Modu� kodera dla plik�w TIFF.

%package coder-url
Summary:	Coder module for retrieving files via URL
Summary(pl):	Modu� kodera �ci�gaj�cy pliki o podanym URL
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-url
Coder module for retrieving files via URL.

%description coder-url -l pl
Modu� kodera �ci�gaj�cy pliki o podanym URL.

%package coder-wmf
Summary:	Coder module for WMF files
Summary(pl):	Modu� kodera dla plik�w WMF
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-wmf
Coder module for WMF files.

%description coder-wmf -l pl
Modu� kodera dla plik�w WMF.

%prep
%setup -q -n %{name}-%{ver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

find -type f -exec perl -pi -e 's=!/usr/local/bin/perl=!/usr/bin/perl='  {} \;

# avoid rebuilding (broken paths in scripts/Makefile.am)
touch www/Magick++/NEWS.html www/Magick++/ChangeLog.html

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-fast-install \
	--enable-lzw \
	--enable-shared \
	--disable-ltdl-install \
	--with%{!?with_fpx:out}-fpx \
	--with%{!?with_gs:out}-gslib \
	--with%{!?with_jasper:out}-jp2 \
	--with%{!?with_cxx:out}-magick_plus_plus \
	--with-gs-font-dir=%{_fontsdir}/Type1 \
	--with-modules \
	--with-perl=%{__perl} \
	--with-perl-options="INSTALLDIRS=vendor" \
	--with-quantum-depth=%{QuantumDepth} \
	--with-threads \
	--with-ttf \
	--with-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-perl

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgdocdir=%{_defaultdocdir}/%{name}-devel-%{version}

install PerlMagick/demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-perl
rm -f $RPM_BUILD_ROOT%{modulesdir}/{coders,filters}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post   c++ -p /sbin/ldconfig
%postun c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_libdir}/ImageMagick-%{ver}
%dir %{_libdir}/ImageMagick-%{ver}/config
%{_libdir}/ImageMagick-%{ver}/config/*.xml
%dir %{modulesdir}
%dir %{modulesdir}/coders
%dir %{modulesdir}/filters
%dir %{_datadir}/ImageMagick-%{ver}
%dir %{_datadir}/ImageMagick-%{ver}/config
%{_datadir}/ImageMagick-%{ver}/config/*.xml

# ========= coders without additional deps
%attr(755,root,root) %{modulesdir}/coders/art.so
%{modulesdir}/coders/art.la
%attr(755,root,root) %{modulesdir}/coders/avi.so
%{modulesdir}/coders/avi.la
%attr(755,root,root) %{modulesdir}/coders/avs.so
%{modulesdir}/coders/avs.la
%attr(755,root,root) %{modulesdir}/coders/bmp.so
%{modulesdir}/coders/bmp.la
%attr(755,root,root) %{modulesdir}/coders/caption.so
%{modulesdir}/coders/caption.la
%attr(755,root,root) %{modulesdir}/coders/cin.so
%{modulesdir}/coders/cin.la
%attr(755,root,root) %{modulesdir}/coders/cip.so
%{modulesdir}/coders/cip.la
%attr(755,root,root) %{modulesdir}/coders/clip.so
%{modulesdir}/coders/clip.la
%attr(755,root,root) %{modulesdir}/coders/cmyk.so
%{modulesdir}/coders/cmyk.la
%attr(755,root,root) %{modulesdir}/coders/cut.so
%{modulesdir}/coders/cut.la
%attr(755,root,root) %{modulesdir}/coders/dcm.so
%{modulesdir}/coders/dcm.la
%attr(755,root,root) %{modulesdir}/coders/dib.so
%{modulesdir}/coders/dib.la
%attr(755,root,root) %{modulesdir}/coders/dpx.so
%{modulesdir}/coders/dpx.la
%attr(755,root,root) %{modulesdir}/coders/ept.so
%{modulesdir}/coders/ept.la
%attr(755,root,root) %{modulesdir}/coders/fax.so
%{modulesdir}/coders/fax.la
%attr(755,root,root) %{modulesdir}/coders/fits.so
%{modulesdir}/coders/fits.la
%attr(755,root,root) %{modulesdir}/coders/gif.so
%{modulesdir}/coders/gif.la
%attr(755,root,root) %{modulesdir}/coders/gradient.so
%{modulesdir}/coders/gradient.la
%attr(755,root,root) %{modulesdir}/coders/gray.so
%{modulesdir}/coders/gray.la
%attr(755,root,root) %{modulesdir}/coders/histogram.so
%{modulesdir}/coders/histogram.la
%attr(755,root,root) %{modulesdir}/coders/html.so
%{modulesdir}/coders/html.la
%attr(755,root,root) %{modulesdir}/coders/icon.so
%{modulesdir}/coders/icon.la
%attr(755,root,root) %{modulesdir}/coders/label.so
%{modulesdir}/coders/label.la
%attr(755,root,root) %{modulesdir}/coders/magick.so
%{modulesdir}/coders/magick.la
%attr(755,root,root) %{modulesdir}/coders/map.so
%{modulesdir}/coders/map.la
%attr(755,root,root) %{modulesdir}/coders/mat.so
%{modulesdir}/coders/mat.la
%attr(755,root,root) %{modulesdir}/coders/matte.so
%{modulesdir}/coders/matte.la
%attr(755,root,root) %{modulesdir}/coders/meta.so
%{modulesdir}/coders/meta.la
%attr(755,root,root) %{modulesdir}/coders/mono.so
%{modulesdir}/coders/mono.la
%attr(755,root,root) %{modulesdir}/coders/mpc.so
%{modulesdir}/coders/mpc.la
%attr(755,root,root) %{modulesdir}/coders/mpeg.so
%{modulesdir}/coders/mpeg.la
%attr(755,root,root) %{modulesdir}/coders/mtv.so
%{modulesdir}/coders/mtv.la
%attr(755,root,root) %{modulesdir}/coders/mvg.so
%{modulesdir}/coders/mvg.la
%attr(755,root,root) %{modulesdir}/coders/null.so
%{modulesdir}/coders/null.la
%attr(755,root,root) %{modulesdir}/coders/otb.so
%{modulesdir}/coders/otb.la
%attr(755,root,root) %{modulesdir}/coders/palm.so
%{modulesdir}/coders/palm.la
%attr(755,root,root) %{modulesdir}/coders/pattern.so
%{modulesdir}/coders/pattern.la
%attr(755,root,root) %{modulesdir}/coders/pcd.so
%{modulesdir}/coders/pcd.la
%attr(755,root,root) %{modulesdir}/coders/pcl.so
%{modulesdir}/coders/pcl.la
%attr(755,root,root) %{modulesdir}/coders/pcx.so
%{modulesdir}/coders/pcx.la
%attr(755,root,root) %{modulesdir}/coders/pdb.so
%{modulesdir}/coders/pdb.la
%attr(755,root,root) %{modulesdir}/coders/pict.so
%{modulesdir}/coders/pict.la
%attr(755,root,root) %{modulesdir}/coders/pix.so
%{modulesdir}/coders/pix.la
%attr(755,root,root) %{modulesdir}/coders/plasma.so
%{modulesdir}/coders/plasma.la
%attr(755,root,root) %{modulesdir}/coders/pnm.so
%{modulesdir}/coders/pnm.la
%attr(755,root,root) %{modulesdir}/coders/preview.so
%{modulesdir}/coders/preview.la
%attr(755,root,root) %{modulesdir}/coders/psd.so
%{modulesdir}/coders/psd.la
%attr(755,root,root) %{modulesdir}/coders/ps.so
%{modulesdir}/coders/ps.la
%attr(755,root,root) %{modulesdir}/coders/pwp.so
%{modulesdir}/coders/pwp.la
%attr(755,root,root) %{modulesdir}/coders/raw.so
%{modulesdir}/coders/raw.la
%attr(755,root,root) %{modulesdir}/coders/rgb.so
%{modulesdir}/coders/rgb.la
%attr(755,root,root) %{modulesdir}/coders/rla.so
%{modulesdir}/coders/rla.la
%attr(755,root,root) %{modulesdir}/coders/rle.so
%{modulesdir}/coders/rle.la
%attr(755,root,root) %{modulesdir}/coders/scr.so
%{modulesdir}/coders/scr.la
%attr(755,root,root) %{modulesdir}/coders/sct.so
%{modulesdir}/coders/sct.la
%attr(755,root,root) %{modulesdir}/coders/sfw.so
%{modulesdir}/coders/sfw.la
%attr(755,root,root) %{modulesdir}/coders/sgi.so
%{modulesdir}/coders/sgi.la
%attr(755,root,root) %{modulesdir}/coders/stegano.so
%{modulesdir}/coders/stegano.la
%attr(755,root,root) %{modulesdir}/coders/sun.so
%{modulesdir}/coders/sun.la
%attr(755,root,root) %{modulesdir}/coders/tga.so
%{modulesdir}/coders/tga.la
%attr(755,root,root) %{modulesdir}/coders/tile.so
%{modulesdir}/coders/tile.la
%attr(755,root,root) %{modulesdir}/coders/tim.so
%{modulesdir}/coders/tim.la
%attr(755,root,root) %{modulesdir}/coders/ttf.so
%{modulesdir}/coders/ttf.la
%attr(755,root,root) %{modulesdir}/coders/txt.so
%{modulesdir}/coders/txt.la
%attr(755,root,root) %{modulesdir}/coders/uil.so
%{modulesdir}/coders/uil.la
%attr(755,root,root) %{modulesdir}/coders/uyvy.so
%{modulesdir}/coders/uyvy.la
%attr(755,root,root) %{modulesdir}/coders/vicar.so
%{modulesdir}/coders/vicar.la
%attr(755,root,root) %{modulesdir}/coders/vid.so
%{modulesdir}/coders/vid.la
%attr(755,root,root) %{modulesdir}/coders/viff.so
%{modulesdir}/coders/viff.la
%attr(755,root,root) %{modulesdir}/coders/wbmp.so
%{modulesdir}/coders/wbmp.la
%attr(755,root,root) %{modulesdir}/coders/wpg.so
%{modulesdir}/coders/wpg.la
%attr(755,root,root) %{modulesdir}/coders/xbm.so
%{modulesdir}/coders/xbm.la
%attr(755,root,root) %{modulesdir}/coders/xcf.so
%{modulesdir}/coders/xcf.la
%attr(755,root,root) %{modulesdir}/coders/xc.so
%{modulesdir}/coders/xc.la
%attr(755,root,root) %{modulesdir}/coders/xpm.so
%{modulesdir}/coders/xpm.la
%attr(755,root,root) %{modulesdir}/coders/x.so
%{modulesdir}/coders/x.la
%attr(755,root,root) %{modulesdir}/coders/xwd.so
%{modulesdir}/coders/xwd.la
%attr(755,root,root) %{modulesdir}/coders/ycbcr.so
%{modulesdir}/coders/ycbcr.la
%attr(755,root,root) %{modulesdir}/coders/yuv.so
%{modulesdir}/coders/yuv.la

%attr(755,root,root) %{modulesdir}/filters/analyze.so
%{modulesdir}/filters/analyze.la

%attr(755,root,root) %{_bindir}/animate
%attr(755,root,root) %{_bindir}/compare
%attr(755,root,root) %{_bindir}/composite
%attr(755,root,root) %{_bindir}/convert
%attr(755,root,root) %{_bindir}/conjure
%attr(755,root,root) %{_bindir}/display
%attr(755,root,root) %{_bindir}/identify
%attr(755,root,root) %{_bindir}/import
%attr(755,root,root) %{_bindir}/mogrify
%attr(755,root,root) %{_bindir}/montage

%{_mandir}/man1/[Iacdim]*

%files doc
%defattr(644,root,root,755)
%doc www

%files libs
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS
%attr(755,root,root) %{_libdir}/libMagick.so.*.*.*
%attr(755,root,root) %{_libdir}/libWand.so.*.*.*

%files coder-dot
%defattr(644,root,root,755)
# R: graphviz, gd
%attr(755,root,root) %{modulesdir}/coders/dot.so
%{modulesdir}/coders/dot.la

%files coder-dps
%defattr(644,root,root,755)
# R: XFree86-DPS (libdps.so)
%attr(755,root,root) %{modulesdir}/coders/dps.so
%{modulesdir}/coders/dps.la

%if %{with fpx}
%files coder-fpx
%defattr(644,root,root,755)
# R: fpx
%attr(755,root,root) %{modulesdir}/coders/fpx.so
%{modulesdir}/coders/fpx.la
%endif

%files coder-jbig
%defattr(644,root,root,755)
# R: jbigkit (libjbig.so)
%attr(755,root,root) %{modulesdir}/coders/jbig.so
%{modulesdir}/coders/jbig.la

%files coder-jpeg
%defattr(644,root,root,755)
# R: libjpeg
%attr(755,root,root) %{modulesdir}/coders/jpeg.so
%{modulesdir}/coders/jpeg.la

%if %{with jasper}
%files coder-jpeg2
%defattr(644,root,root,755)
# R: jasper, libjpeg
%attr(755,root,root) %{modulesdir}/coders/jp2.so
%{modulesdir}/coders/jp2.la
%endif

%files coder-miff
%defattr(644,root,root,755)
# R: libjpeg, zlib, libbz2
%attr(755,root,root) %{modulesdir}/coders/miff.so
%{modulesdir}/coders/miff.la

%files coder-mpr
%defattr(644,root,root,755)
# R: libxml2
%attr(755,root,root) %{modulesdir}/coders/mpr.so
%{modulesdir}/coders/mpr.la
%attr(755,root,root) %{modulesdir}/coders/msl.so
%{modulesdir}/coders/msl.la

%files coder-pdf
%defattr(644,root,root,755)
# R: libtiff, libjpeg
%attr(755,root,root) %{modulesdir}/coders/pdf.so
%{modulesdir}/coders/pdf.la

%files coder-png
%defattr(644,root,root,755)
# R: libpng
%attr(755,root,root) %{modulesdir}/coders/png.so
%{modulesdir}/coders/png.la

%files coder-ps2
%defattr(644,root,root,755)
# R: libtiff, libjpeg
%attr(755,root,root) %{modulesdir}/coders/ps2.so
%{modulesdir}/coders/ps2.la
%attr(755,root,root) %{modulesdir}/coders/ps3.so
%{modulesdir}/coders/ps3.la

%files coder-svg
%defattr(644,root,root,755)
# R: libxml2
%attr(755,root,root) %{modulesdir}/coders/svg.so
%{modulesdir}/coders/svg.la

%files coder-tiff
%defattr(644,root,root,755)
# R: libtiff, libjpeg
%attr(755,root,root) %{modulesdir}/coders/tiff.so
%{modulesdir}/coders/tiff.la

%files coder-url
%defattr(644,root,root,755)
# R: libxml2
%attr(755,root,root) %{modulesdir}/coders/url.so
%{modulesdir}/coders/url.la

%files coder-wmf
%defattr(644,root,root,755)
# R: libwmf, expat, libjpeg, libpng
%attr(755,root,root) %{modulesdir}/coders/wmf.so
%{modulesdir}/coders/wmf.la

%files devel
%defattr(644,root,root,755)
%doc %{_defaultdocdir}/%{name}-devel-%{version}
%attr(755,root,root) %{_bindir}/Magick-config
%attr(755,root,root) %{_bindir}/Wand-config
%attr(755,root,root) %{_libdir}/libMagick.so
%attr(755,root,root) %{_libdir}/libWand.so
%{_libdir}/libMagick.la
%{_libdir}/libWand.la
%{_includedir}/magick
%{_includedir}/wand
%{_pkgconfigdir}/ImageMagick.pc
%{_pkgconfigdir}/Wand.pc
%{_mandir}/man[45]/*
%{_mandir}/man1/Magick-config.1*
%{_mandir}/man1/Wand-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libMagick.a
%{_libdir}/libWand.a

%files perl
%defattr(644,root,root,755)
%{perl_vendorarch}/Image
%dir %{perl_vendorarch}/auto/Image
%dir %{perl_vendorarch}/auto/Image/Magick
%{perl_vendorarch}/auto/Image/Magick/autosplit.ix
%{perl_vendorarch}/auto/Image/Magick/Magick.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Image/Magick/Magick.so
%{_mandir}/man3/Image::Magick.*
%{_examplesdir}/%{name}-perl

%if %{with cxx}
%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libMagick++.so.*.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Magick++-config
%{_libdir}/libMagick++.la
%attr(755,root,root) %{_libdir}/libMagick++.so
%{_includedir}/Magick++
%{_includedir}/Magick++.h
%{_pkgconfigdir}/ImageMagick++.pc
%{_mandir}/man1/Magick++-config.1*

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libMagick++.a
%endif
