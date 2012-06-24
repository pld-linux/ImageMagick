#
# Conditional build:
# _without_fpx		- without FlashPIX module (which uses fpx library)
# _with_gs		- with PostScript support through ghostscript library (warning: breaks jpeg!)
# _without_hdf		- without HDF module (which uses hdf library)
# _without_jasper	- without JPEG2000 module (which uses jasper library)
#
%include	/usr/lib/rpm/macros.perl
%define		ver 5.5.1
%define		pver	4
Summary:	Image display, conversion, and manipulation under X
Summary(de):	Darstellen, Konvertieren und Bearbeiten von Grafiken unter X
Summary(es):	Exhibidor, convertidor y manipulador de im�genes bajo X
Summary(fr):	Visualisation, conversion, et manipulation d'images sous X
Summary(pl):	Narz�dzie do wy�wietlania, konwersji i manipulacji grafikami
Summary(pt_BR):	Exibidor, conversor e manipulador de imagens sob X
Summary(ru):	��������, ���������������, ��������� ����������� ��� X Windows
Summary(tr):	X alt�nda resim g�sterme, �evirme ve de�i�iklik yapma
Summary(uk):	��������, ������������� �� ������� ��������� Ц� X Windows
Name:		ImageMagick
Version:	%{ver}%{?pver:.%{pver}}
Release:	1
Epoch:		1
License:	Freeware
Group:		X11/Applications/Graphics
Source0:	http://imagemagick.sourceforge.net/http/%{name}-%{ver}%{?pver:-%{pver}}.tar.bz2
Patch0:		%{name}-libpath.patch
Patch1:		%{name}-perlpaths.patch
Patch2:		%{name}-ac.patch
URL:		http://www.imagemagick.org/
BuildRequires:	XFree86-DPS-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7
BuildRequires:	bzip2-devel >= 1.0.1
%{!?_without_fpx:BuildRequires:	fpx-devel}
BuildRequires:	freetype-devel >= 2.0.2-2
%{?_with_gs:BuildRequires:	ghostscript-devel}
%{!?_without_hdf:BuildRequires:	hdf-devel}
%{!?_without_jasper:BuildRequires:	jasper-devel}
BuildRequires:	jbigkit-devel
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libplot-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libwmf-devel >= 0.2.2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	mpeg2dec-devel
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-18
Requires:	%{name}-libs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_includedir	%{_prefix}/include/X11
%define		_perlmandir	/usr/share/man

%description
ImageMagick is an image display, conversion, and manipulation tool. It
runs under X windows. It is very powerful in terms of it's ability to
allow the user to edit images. It can handle many different formats as
well.

%description -l de
ImageMagick ist ein Tool zur Bildanzeige, -konvertierung und
manipulation, -das unter X-Windows l�uft. Es ist enorm leitungsf�hig
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
�����������. ��� �������� ��� X Windows. ImageMagick �������������
������������ ������� ����������� �� ��������� ����������� � �����
������������� ��������.

%description -l tr
ImageMagick bir resim g�sterme, �evirme ve de�i�iklik yapma
program�d�r. X Window pencereleme sistemi alt�nda �al���r. Kullan�c�ya
resimler �zerinde de�i�iklik yapma a��s�ndan pek �ok olanak sunar. Bir
�ok resim bi�imini rahatl�kla kullanabilir.

%description -l uk
ImageMagick - �� ���̦�� ��� ���������, ������������� �� �������
���������. ���� ������ Ц� X Windows. ImageMagick ��� �����������
����˦ ��������Ԧ �� �����æ ��������� � Ҧ�����Φ���� ��������.

%package devel
Summary:	Libraries and header files for ImageMagick development
Summary(es):	Biblioteca est�tica y archivos de inclusi�n para desarrollo con libMagick
Summary(pl):	Biblioteki i pliki nag��wkowe dla ImageMagick
Summary(pt_BR):	Biblioteca e arquivos de inclus�o para desenvolvimento com libMagick
Summary(ru):	������ � ���������� ��� ���������������� � ImageMagick
Summary(uk):	������ �� ¦�̦����� ��� ������������� � ImageMagick
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	XFree86-devel
Requires:	freetype-devel
Requires:	lcms-devel
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
Summary(es):	Static libraries for libMagick development
Summary(pl):	Biblioteki statyczne ImageMagick
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com libMagick
Summary(ru):	����������� ���������� ��� ���������������� � ImageMagick
Summary(uk):	������Φ ¦�̦����� ��� ������������� � ImageMagick
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
ImageMagick static libraries.

%description static -l es
Static libraries for libMagick development.

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
Summary:	Libraries and modules for access to ImageMagick from perl
Summary(es):	Perl Module to use ImageMagick
Summary(pl):	Biblioteki i modu�y perla dla ImageMagick
Summary(pt_BR):	M�dulo perl para uso com o ImageMagick
Summary(ru):	���������� � ������ ��� ������� � ImageMagick �� perl
Summary(uk):	��̦����� �� ����̦ ��� ������� �� ImageMagick � Perl
Group:		Development/Languages/Perl
Requires:	%{name}-libs = %{version}

%description perl
This is the ImageMagick perl support package. It perl modules and
support files for access to ImageMagick library from perl without
unuseful forking or such.

%description perl -l es
This packages provides a perl module to access ImagickMagick functions
from perl scripts.

%description perl -l pl
Biblioteki i modu�y umo�liwiaj�ce korzystanie z ImageMagick z poziomu
perla.

%description perl -l pt_BR
Este pacote fornece um m�dulo perl para acessar fun��es do ImageMagick
em scripts perl.

%description perl -l ru
��� ����� ImageMagick ��� ��������� perl. �� �������� ������ perl �
��������������� ����� ��� ������� � ���������� ImageMagick �� perl.

%description perl -l uk
�� ����� ImageMagick ��� Ц������� Perl. ��� ͦ����� ����̦ Perl ��
�������צ ����� ��� ������� �� ¦�̦����� ImageMagick � Perl.

%package libs
Summary:	ImageMagick libraries
Summary(es):	ImageMagick dynamic libraries
Summary(pl):	Biblioteki ImageMagick
Summary(pt_BR):	Bibliotecas din�micas do ImageMagick
Group:		X11/Libraries

%description libs
ImageMagick libraries.

%description libs -l es
ImageMagick dynamic libraries.

%description libs -l pl
Biblioteki ImageMagick.

%description libs -l pt_BR
Bibliotecas din�micas do ImageMagick.

%package c++
Summary:	ImageMagick Magick++ library
Summary(es):	ImageMagick dynamic libraries
Summary(pl):	Biblioteka Magick++
Summary(pt_BR):	Bibliotecas din�micas do ImageMagick
Summary(ru):	���������� Magick++ (C++ ��������� ��� ImageMagick'�)
Summary(uk):	��̦����� Magick++ (��������� C++ ��� ImageMagick)
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}

%description c++
This package contains the Magick++ library, a C++ binding to the
ImageMagick graphics manipulation library.

Install ImageMagick-c++ if you want to use any applications that use
Magick++.

%description c++ -l es
ImageMagick C++ dynamic libraries.

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
Requires:	%{name}-c++ = %{version}
Requires:	%{name}-devel = %{version}

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
Summary(es):	Static libraries for libMagick development
Summary(pl):	Interfejs C++ do ImageMagick - biblioteka statyczna
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com libMagick
Summary(ru):	����������� ���������� C++ ��� ���������������� � ImageMagick
Summary(uk):	������Φ ¦�̦����� C++ ��� ������������� � ImageMagick
Group:		X11/Development/Libraries
Requires:	%{name}-c++-devel = %{version}
Requires:	%{name}-devel = %{version}

%description c++-static
C++ bindings for the ImageMagick - static library.

%description c++-static -l es
Static libraries for libMagick++ development

%description c++-static -l pl
Biblioteka Magick++ w wersji statycznej.

%description c++-static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com libMagick++

%description c++-static -l ru
��� ��������� ����� �� ������������ ������������, ������� ������ ��
������ � ImageMagick-c++-devel.

%description c++-static -l uk
�� ������� ����� ڦ ���������� ¦�̦�������, �˦ ¦���� �� ������� ��
������ ImageMagick-c++-devel.

%package coder-dps
Summary: coder-dps
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-dps


%package coder-fpx
Summary: coder-fpx
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-fpx


%package coder-hdf
Summary: coder-hdf
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-hdf


%package coder-jbig
Summary: coder-jbig
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-jbig


%package coder-jpeg
Summary: coder-jpeg
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-jpeg


%package coder-jpeg2
Summary: coder-jpeg2
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-jpeg2


%package coder-miff
Summary: coder-miff
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-miff


%package coder-mpeg
Summary: coder-mpeg
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-mpeg


%package coder-mpr
Summary: coder-mpr
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-mpr


%package coder-pdf
Summary: coder-pdf
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-pdf


%package coder-png
Summary: coder-png
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-png


%package coder-ps2
Summary: coder-ps2
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-ps2


%package coder-svg
Summary: coder-svg
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-svg


%package coder-tiff
Summary: coder-tiff
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-tiff


%package coder-url
Summary: coder-url
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-url


%package coder-wmf
Summary: coder-wmf
Group: X11/Applications/Graphics
Requires: %{name}-%{version}

%description coder-wmf


%prep
%setup  -q -n %{name}-%{ver}
%patch0 -p1
%patch1 -p0
%patch2 -p1

# fix lcms.h include path
perl -pi -e 's@lcms/lcms\.h@lcms.h@' magick/transform.c
perl -pi -e 's@lcms/lcms\.h@lcms.h@' configure.ac

%build
rm -f missing
%{__libtoolize} --ltdl
aclocal -I /usr/share/libtool/libltdl
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/include/g++"
%configure \
	CPPFLAGS="$CPPFLAGS" \
	--enable-16bit-pixel \
	--enable-lzw \
	--enable-shared \
	--with-gs-font-dir=%{_fontsdir}/Type1 \
	%{?_without_fpx:--without-fpx} \
	%{!?_with_gs:--without-gslib} \
	%{!?_without_hdf:--with-hdf} \
	%{?_without_jasper:--without-jp2} \
	--with%{?_without_cxx:out}-magick_plus_plus \
	--with-perl \
	--with-threads \
	--with-ttf \
	--with-modules \
	--with-x

%{__make}
%{!?_without_cxx:%{__make} -C Magick++}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-perl

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgdocdir=%{_defaultdocdir}/%{name}-devel-%{version}/

install PerlMagick/demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-perl
rm -f $RPM_BUILD_ROOT/%{_libdir}/ImageMagick-%{ver}/modules/coders/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%if %{?_without_cxx:0}%{!?_without_cxx:1}
%post   c++ -p /sbin/ldconfig
%postun c++ -p /sbin/ldconfig
%endif

%files libs
%defattr(644,root,root,755)
%doc Copyright.txt
%attr(755,root,root) %{_libdir}/libMagick-%{ver}.so

%files
%defattr(644,root,root,755)
#%dir %{_datadir}/ImageMagick
#%{_datadir}/ImageMagick/*.mgk
%dir %{_libdir}/ImageMagick-%{ver}
%{_libdir}/ImageMagick-%{ver}/*.mgk
%dir %{_libdir}/ImageMagick-%{ver}/modules
%dir %{_libdir}/ImageMagick-%{ver}/modules/coders

# ========= coders without additional deps
%{_libdir}/ImageMagick-%{ver}/modules/coders/art.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/art.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/avi.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/avi.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/avs.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/avs.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/bmp.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/bmp.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/caption.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/caption.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/cmyk.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/cmyk.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/cut.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/cut.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/dcm.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/dcm.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/dib.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/dib.so

%{_libdir}/ImageMagick-%{ver}/modules/coders/dpx.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/dpx.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/ept.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/ept.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/fax.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/fax.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/fits.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/fits.so
# FIXME: test gif coder (this not depend on lib(un)gif ???)
%{_libdir}/ImageMagick-%{ver}/modules/coders/gif.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/gif.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/gradient.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/gradient.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/gray.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/gray.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/histogram.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/histogram.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/html.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/html.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/icon.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/icon.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/label.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/label.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/locale.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/locale.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/logo.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/logo.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/map.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/map.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/mat.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/mat.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/matte.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/matte.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/meta.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/meta.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/mono.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/mono.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/mpc.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/mpc.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/mtv.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/mtv.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/mvg.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/mvg.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/null.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/null.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/otb.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/otb.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/palm.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/palm.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/pcd.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/pcd.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/pcl.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/pcl.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/pcx.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/pcx.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/pdb.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/pdb.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/pict.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/pict.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/pix.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/pix.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/plasma.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/plasma.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/pnm.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/pnm.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/preview.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/preview.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/psd.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/psd.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/ps.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/ps.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/pwp.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/pwp.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/rgb.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/rgb.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/rla.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/rla.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/rle.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/rle.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/sct.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/sct.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/sfw.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/sfw.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/sgi.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/sgi.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/stegano.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/stegano.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/sun.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/sun.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/tga.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/tga.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/tile.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/tile.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/tim.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/tim.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/ttf.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/ttf.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/txt.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/txt.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/uil.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/uil.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/uyvy.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/uyvy.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/vicar.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/vicar.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/vid.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/vid.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/viff.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/viff.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/wbmp.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/wbmp.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/wpg.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/wpg.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/xbm.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/xbm.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/xcf.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/xcf.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/xc.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/xc.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/xpm.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/xpm.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/x.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/x.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/xwd.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/xwd.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/yuv.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/yuv.so

%{_libdir}/ImageMagick-%{ver}/modules/coders/*.mgk

%attr(755,root,root) %{_bindir}/animate
#%attr(755,root,root) %{_bindir}/cgimagick
%attr(755,root,root) %{_bindir}/composite
%attr(755,root,root) %{_bindir}/convert
%attr(755,root,root) %{_bindir}/conjure
%attr(755,root,root) %{_bindir}/display
%attr(755,root,root) %{_bindir}/identify
%attr(755,root,root) %{_bindir}/import
#%attr(755,root,root) %{_bindir}/iptcutil
%attr(755,root,root) %{_bindir}/mogrify
%attr(755,root,root) %{_bindir}/montage

%{_mandir}/man1/[Iacdim]*

%files coder-dps
# R: libdps
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/dps.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/dps.so

%files coder-fpx
# R: fpx
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/fpx.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/fpx.so

%files coder-hdf
# R: hdf, libjpeg
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/hdf.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/hdf.so

%files coder-jbig
# R: libjbig
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/jbig.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/jbig.so

%files coder-jpeg
# R: libjpeg
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/jpeg.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/jpeg.so

%files coder-jpeg2
# R: jasper, libjpeg
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/jp2.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/jp2.so

%files coder-miff
# R: libjpeg, zlib, libbz2
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/miff.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/miff.so

%files coder-mpeg
# R: libmpeg2
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/mpeg.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/mpeg.so

%files coder-mpr
# R: libxml2
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/mpr.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/mpr.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/msl.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/msl.so

%files coder-pdf
# R: libtiff, libjpeg
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/pdf.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/pdf.so

%files coder-png
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/png.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/png.so

%files coder-ps2
# R: libtiff, libjpeg
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/ps2.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/ps2.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/ps3.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/ps3.so

%files coder-svg
# R: libxml2
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/svg.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/svg.so

%files coder-tiff
# R: libtiff, libjpeg
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/tiff.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/tiff.so

%files coder-url
# R: libxml2
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/url.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/url.so

%files coder-wmf
# R: libwmf, libexpat, libjpeg, libpng
%defattr(644,root,root,755)
%{_libdir}/ImageMagick-%{ver}/modules/coders/wmf.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/wmf.so

%files devel
%defattr(644,root,root,755)
#%%doc README.txt
%doc %{_defaultdocdir}/%{name}-devel-%{version}

%attr(755,root,root) %{_bindir}/Magick-config
%attr(755,root,root) %{_libdir}/libMagick.so
%attr(755,root,root) %{_libdir}/libMagick.la
%{_includedir}/magick

%{_mandir}/man[45]/*
%{_mandir}/man1/Magick-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libMagick.a

%files perl
%defattr(644,root,root,755)
%{perl_sitearch}/Image
%dir %{perl_sitearch}/auto/Image
%dir %{perl_sitearch}/auto/Image/Magick
%{perl_sitearch}/auto/Image/Magick/autosplit.ix
%{perl_sitearch}/auto/Image/Magick/Magick.bs
%attr(755,root,root) %{perl_sitearch}/auto/Image/Magick/Magick.so
%{_perlmandir}/man3/Image::Magick.*
%{_examplesdir}/%{name}-perl

%if %{?_without_cxx:0}%{!?_without_cxx:1}
%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libMagick++-%{ver}.so

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Magick++-config
%attr(755,root,root) %{_libdir}/libMagick++.la
%attr(755,root,root) %{_libdir}/libMagick++.so
%{_prefix}/include/Magick++
%{_prefix}/include/Magick++.h
%{_mandir}/man1/Magick++-config.1*

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libMagick++.a
%endif
