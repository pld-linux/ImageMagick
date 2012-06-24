%include	/usr/lib/rpm/macros.perl
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
Version:	5.4.5
Release:	1
Epoch:		1
License:	Freeware
Group:		X11/Applications/Graphics
Source0:	http://imagemagick.sourceforge.net/http/%{name}-%{version}.tar.bz2
Patch0:		%{name}-libpath.patch
Patch1:		%{name}-perlpaths.patch
URL:		http://www.imagemagick.org/
BuildRequires:	XFree86-DPS-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake >= 1.4d
BuildRequires:	bzip2-devel >= 1.0.1
BuildRequires:	freetype-devel >= 2.0.2-2
BuildRequires:	jbigkit-devel
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
#BuildRequires:	fpx-devel
#BuildRequires:	hdf5-devel
#BuildRequires:	jasper-devel
#BuildRequires:	lcms-devel
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
Requires:	expat-devel
Requires:	freetype-devel
Requires:	jbigkit-devel
Requires:	libjpeg-devel
Requires:	libplot-devel
Requires:	libwmf-devel
Requires:	libxml2-devel
Requires:	mpeg2dec-devel
Requires:	XFree86-DPS-devel
Requires:	libtiff-devel
Requires:	libpng-devel
Requires:	XFree86-devel
Requires:	bzip2-devel

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

%prep
%setup  -q
%patch0 -p1
%patch1 -p0

# fix lcms.h include path
perl -pi -e 's@lcms/lcms\.h@lcms.h@' magick/transform.c
perl -pi -e 's@lcms/lcms\.h@lcms.h@' configure.ac

%build
rm -f missing
libtoolize --copy --force
aclocal
%{__autoconf}
%{__automake}
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
%configure \
	CPPFLAGS="$CPPFLAGS" \
	--enable-shared \
	--enable-lzw \
	--enable-16bit-pixel \
	--with-perl \
	--with-ttf \
	--with-x \
	--with-hdf \
	--with-threads \
	--with-magick_plus_plus

%{__make} 
%{__make} -C Magick++

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-perl

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

install PerlMagick/demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-perl

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post   c++ -p /sbin/ldconfig
%postun c++ -p /sbin/ldconfig

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libMagick.so.*.*

%files
%defattr(644,root,root,755)
%dir %{_datadir}/ImageMagick
%{_datadir}/ImageMagick/*.mgk
%dir %{_libdir}/ImageMagick
%{_libdir}/ImageMagick/*.mgk

%attr(755,root,root) %{_bindir}/animate
#%attr(755,root,root) %{_bindir}/cgimagick
%attr(755,root,root) %{_bindir}/composite
%attr(755,root,root) %{_bindir}/convert
%attr(755,root,root) %{_bindir}/display
%attr(755,root,root) %{_bindir}/identify
%attr(755,root,root) %{_bindir}/import
#%attr(755,root,root) %{_bindir}/iptcutil
%attr(755,root,root) %{_bindir}/mogrify
%attr(755,root,root) %{_bindir}/montage

%{_mandir}/man1/[Iacdim]*

%files devel
%defattr(644,root,root,755)
%doc images www ImageMagick.html README.txt

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

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libMagick++.so.*.*

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
