#
# Conditional build:
# _without_fpx		- without FlashPIX module (which uses fpx library)
# _with_gs		- with PostScript support through ghostscript library (warning: breaks jpeg!)
# _without_jasper	- without JPEG2000 module (which uses jasper library)
# _without_cxx          - without Magick++
#
%include	/usr/lib/rpm/macros.perl
%define		ver 5.5.3
%define		pver	2
Summary:	Image display, conversion, and manipulation under X
Summary(de):	Darstellen, Konvertieren und Bearbeiten von Grafiken unter X
Summary(es):	Exhibidor, convertidor y manipulador de imАgenes bajo X
Summary(fr):	Visualisation, conversion, et manipulation d'images sous X
Summary(pl):	NarzЙdzie do wy╤wietlania, konwersji i manipulacji grafikami
Summary(pt_BR):	Exibidor, conversor e manipulador de imagens sob X
Summary(ru):	Просмотр, конвертирование, обработка изображений под X Windows
Summary(tr):	X altЩnda resim gЖsterme, Гevirme ve deПiЧiklik yapma
Summary(uk):	Перегляд, конвертування та обробка зображень п╕д X Windows
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
Patch3:		%{name}-system-libltdl.patch
Patch4:		%{name}-dps.patch
URL:		http://www.imagemagick.org/
BuildRequires:	XFree86-DPS-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake >= 1.7
BuildRequires:	bzip2-devel >= 1.0.1
%{!?_without_fpx:BuildRequires:	libfpx-devel >= 1.2.0.4-2}
BuildRequires:	freetype-devel >= 2.0.2-2
%{?_with_gs:BuildRequires:	ghostscript-devel}
%{!?_without_jasper:BuildRequires:	jasper-devel}
BuildRequires:	jbigkit-devel
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libplot-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.4e-0.20021218.3
BuildRequires:	libwmf-devel >= 0.2.2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-18
Requires:	%{name}-libs = %{version}
Obsoletes:	%{name}-coder-mpeg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ImageMagick is an image display, conversion, and manipulation tool. It
runs under X windows. It is very powerful in terms of it's ability to
allow the user to edit images. It can handle many different formats as
well.

%description -l de
ImageMagick ist ein Tool zur Bildanzeige, -konvertierung und
manipulation, -das unter X-Windows lДuft. Es ist enorm leitungsfДhig
in Bezug auf die Grafikmanipulationsfunktionen, die es dem Anwender
bietet, und auf die Vielfalt der unterstЭtzten Formate.

%description -l es
ImageMagick es una herramienta para manipular, convertir y exhibir
imАgenes, que funciona bajo X Window. Es una herramienta potente que
permite editar imАgenes, pudiendo manipular varios formatos
diferentes.

%description -l fr
ImageMagick est un outil d'affichage, de conversion et de manipulation
d'images. Il tourne sous X Window et est trХs puissant en termes de
capacitИ d'Иdition des images. Il peut aussi gИrer de nombreux formats
diffИrents.

%description -l pl
ImageMagick jest narzЙdziem do manipulacji, konwersji i wy╤wietlania.
W skЁad pakietu wchodz╠ zarСwno narzЙdzia X Window jak i do u©ywania z
linii poleceЯ umo©liwiaj╠ce edycjЙ plikСw graficznych. NarzЙdzia z
pakietu ImageMagick potrafi╠ obsЁu©yФ wiele rС©nych formatСw
graficznych.

%description -l pt_BR
ImageMagick И uma ferramenta para manipular, converter e exibir
imagens, que funciona sob o X Window. и uma ferramenta poderosa que
permite editar imagens, podendo tratar vАrios formatos diferentes.

%description -l ru
ImageMagick - это утилита для просмотра, конвертирования и обработки
изображений. Она работает под X Windows. ImageMagick предоставляет
пользователю широкие возможности по обработке изображений в самых
разнообразных форматах.

%description -l tr
ImageMagick bir resim gЖsterme, Гevirme ve deПiЧiklik yapma
programЩdЩr. X Window pencereleme sistemi altЩnda ГalЩЧЩr. KullanЩcЩya
resimler Эzerinde deПiЧiklik yapma aГЩsЩndan pek Гok olanak sunar. Bir
Гok resim biГimini rahatlЩkla kullanabilir.

%description -l uk
ImageMagick - це утил╕та для перегляду, конвертування та обробки
зображень. Вона працю╓ п╕д X Windows. ImageMagick да╓ користувачу
широк╕ можливост╕ по обробц╕ зображень в р╕зноман╕тних форматах.

%package libs
Summary:	ImageMagick libraries
Summary(pl):	Biblioteki ImageMagick
Summary(pt_BR):	Bibliotecas dinБmicas do ImageMagick
Group:		X11/Libraries

%description libs
ImageMagick libraries.

%description libs -l pl
Biblioteki ImageMagick.

%description libs -l pt_BR
Bibliotecas dinБmicas do ImageMagick.

%package devel
Summary:	Libraries and header files for ImageMagick development
Summary(es):	Biblioteca estАtica y archivos de inclusiСn para desarrollo con libMagick
Summary(pl):	Biblioteki i pliki nagЁСwkowe dla ImageMagick
Summary(pt_BR):	Biblioteca e arquivos de inclusЦo para desenvolvimento com libMagick
Summary(ru):	Хедеры и библиотеки для программирования с ImageMagick
Summary(uk):	Хедери та б╕бл╕отеки для програмування з ImageMagick
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
Dies ist das ImageMagick-Entwicklerpaket. Es enthДlt Header-Dateien
zum Entwickeln von Anwendungen, die ImageMagick-Code und/oder -APIs
nutzen.

%description devel -l es
Este es el paquete de desarrollo ImageMagick. Incluye las bibliotecas
y los archivos de inclusiСn para el desarrollo de sus propias
aplicaciones que hacen uso del cСdigo ImageMagick y/el APIs.

%description devel -l fr
Paquetage de dИveloppement ImageMagick. Contient les bibliothХques
statiques et les en-tЙtes utilisИs pour crИer vos propres applications
utilisant le code d'ImageMagick et/ou ses APIs.

%description devel -l pl
Pakiet ten zawieraja pliki potrzebne przy kompilowaniu programСw
wykorzystuj╠cych blibliotekЙ ImageMagick takie jak pliki nagЁСwkowe i
dokumentacjЙ niezbЙdn╠ przy pisaniu wЁasnych programСw z
wykorzystaniem API jakie udostЙpnia ImageMagick.

%description devel -l pt_BR
Este И o pacote de desenvolvimento ImageMagick. Inclui as bibliotecas
e os arquivos de inclusЦo para o desenvolvimento de suas prСprias
aplicaГУes que fazem uso do cСdigo ImageMagick e/ou APIs.

%description devel -l ru
Это пакет разработчика для программирования с ImageMagick. Он включает
хедеры и библиотеки для использования в программах, которые используют
код или API ImageMagick.

%description devel -l tr
Bu paket, ImageMagick uygulama arayЭzЭnЭ kullanan programlar
geliЧtirmek iГin gereken baЧlЩk dosyalarЩnЩ ve kitaplЩklarЩ iГerir.

%description devel -l uk
Це пакет для програмування з ImageMagick. В╕н м╕стить хедери та
б╕бл╕отеки для використання в програмах, що використовують код або API
ImageMagick.

%package static
Summary:	ImageMagick static libraries
Summary(pl):	Biblioteki statyczne ImageMagick
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com libMagick
Summary(ru):	Статические библиотеки для программирования с ImageMagick
Summary(uk):	Статичн╕ б╕бл╕отеки для програмування з ImageMagick
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
ImageMagick static libraries.

%description static -l pl
Biblioteki statyczne ImageMagick.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com libMagick.

%description static -l ru
Это отдельный пакет со статическими библиотеками, которые больше не
входят в ImageMagick-devel.

%description static -l uk
Це окремий пакет з╕ статичними б╕бл╕отеками, як╕ б╕льше не входять до
складу ImageMagick-devel.

%package perl
Summary:	Libraries and modules for access to ImageMagick from perl
Summary(pl):	Biblioteki i moduЁy perla dla ImageMagick
Summary(pt_BR):	MСdulo perl para uso com o ImageMagick
Summary(ru):	Библиотеки и модули для доступа к ImageMagick из perl
Summary(uk):	Б╕бл╕отеки та модул╕ для доступу до ImageMagick з Perl
Group:		Development/Languages/Perl
Requires:	%{name}-libs = %{version}

%description perl
This is the ImageMagick perl support package. It perl modules and
support files for access to ImageMagick library from perl without
unuseful forking or such.

%description perl -l pl
Biblioteki i moduЁy umo©liwiaj╠ce korzystanie z ImageMagick z poziomu
perla.

%description perl -l pt_BR
Este pacote fornece um mСdulo perl para acessar funГУes do ImageMagick
em scripts perl.

%description perl -l ru
Это пакет ImageMagick для поддержки perl. Он включает модули perl и
вспомогательные файлы для доступа к библиотеке ImageMagick из perl.

%description perl -l uk
Це пакет ImageMagick для п╕дтримки Perl. В╕н м╕стить модул╕ Perl та
додатков╕ файли для доступу до б╕бл╕отеки ImageMagick з Perl.

%package c++
Summary:	ImageMagick Magick++ library
Summary(pl):	Biblioteka Magick++
Summary(pt_BR):	Bibliotecas dinБmicas do ImageMagick
Summary(ru):	Библиотека Magick++ (C++ интерфейс для ImageMagick'а)
Summary(uk):	Б╕бл╕отека Magick++ (╕нтерфейс C++ для ImageMagick)
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}

%description c++
This package contains the Magick++ library, a C++ binding to the
ImageMagick graphics manipulation library.

Install ImageMagick-c++ if you want to use any applications that use
Magick++.

%description c++ -l pl
Pakiet zawiera bibliotekЙ Magick++ - interfejs w C++ do biblioteki
ImageMagick. Jest potrzebny do uruchamiania programСw korzystaj╠cych z
Magick++.

%description c++ -l pt_BR
Bibliotecas dinБmicas C++ do ImageMagick.

%description c++ -l ru
Magick++ -- объектно-ориентированная библиотека, представляющая из
себя C++ API для ImageMagick (библиотеки для просмотра,
конвертирования и обработки изображений).

%description c++ -l uk
Magick++ -- об'╓кто-ор╕╓нтована б╕бл╕отека, що явля╓ собою C++ API для
ImageMagick (б╕бл╕отеки для перегляду, конвертування та обробки
зображень).

%package c++-devel
Summary:	C++ bindings for the ImageMagick library
Summary(es):	Biblioteca estАtica y archivos de inclusiСn para desarrollo con libMagick++
Summary(pl):	Pliki nagЁСwkowe z interfejsem C++ do ImageMagick
Summary(pt_BR):	Biblioteca e arquivos de inclusЦo para desenvolvimento com libMagick++
Summary(ru):	Хедеры и библиотеки для разработок с использованием Magick++ (C++ интерфейс для ImageMagick'а)
Summary(uk):	Хедери та б╕бл╕отеки для розробок з використанням Magick++ (╕нтерфейсу C++ для ImageMagick)
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
estАticas y los archivos de inclusiСn para el desarrollo de sus
propias aplicaciones que hacen uso del cСdigo ImageMagick y/el APIs.

%description c++-devel -l pl
Pakiet zawiera pliki nagЁСwkowe potrzebne do kompilowania programСw
korzystaj╠cych z Magick++.

%description c++-devel -l pt_BR
Este И o pacote de desenvolvimento libMagick++. Inclui as bibliotecas
e os arquivos de inclusЦo para o desenvolvimento de suas prСprias
aplicaГУes C++ que fazem uso do cСdigo ImageMagick e/ou APIs.

%description c++-devel -l ru
Это пакет разработчика для программирования с ImageMagick. Он включает
хедеры и библиотеки для использования в программах, которые используют
код или API Magick++ (C++ интерфейс для ImageMagick'а).

%description c++-devel -l uk
Це пакет для програмування з ImageMagick. В╕н м╕стить хедери та
б╕бл╕отеки для використання в програмах, що використовують код або API
Magick++ (╕нтерфейс C++ для ImageMagick).

%package c++-static
Summary:	C++ bindings for the ImageMagick - static library
Summary(pl):	Interfejs C++ do ImageMagick - biblioteka statyczna
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com libMagick
Summary(ru):	Статические библиотеки C++ для программирования с ImageMagick
Summary(uk):	Статичн╕ б╕бл╕отеки C++ для програмування з ImageMagick
Group:		X11/Development/Libraries
Requires:	%{name}-c++-devel = %{version}
Requires:	%{name}-devel = %{version}

%description c++-static
C++ bindings for the ImageMagick - static library.

%description c++-static -l pl
Biblioteka Magick++ w wersji statycznej.

%description c++-static -l pt_BR
Bibliotecas estАticas para desenvolvimento com libMagick++.

%description c++-static -l ru
Это отдельный пакет со статическими библиотеками, которые больше не
входят в ImageMagick-c++-devel.

%description c++-static -l uk
Це окремий пакет з╕ статичними б╕бл╕отеками, як╕ б╕льше не входять до
складу ImageMagick-c++-devel.

%package coder-dps
Summary:	Coder module for Postscript files using DPS extension
Summary(pl):	ModuЁ kodera dla plikСw Postscript u©ywaj╠cy rozszerzenia DPS
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-dps
Coder module for Postcript files using DPS (Display PostScript)
extension.

%description coder-dps -l pl
ModuЁ kodera dla plikСw Postscript u©ywaj╠cy rozszerzenia DPS (Display
PostScript).

%package coder-fpx
Summary:	Coder module for FlashPIX (FPX) files
Summary(pl):	ModuЁ kodera dla plikСw FlashPIX (FPX)
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-fpx
Coder module for FlashPIX (FPX) files.

%description coder-fpx -l pl
ModuЁ kodera dla plikСw FlashPIX (FPX).

%package coder-jbig
Summary:	Coder module for JBIG files
Summary(pl):	ModuЁ kodera dla plikСw JBIG
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-jbig
Coder module for JBIG files.

%description coder-jbig -l pl
ModuЁ kodera dla plikСw JBIG.

%package coder-jpeg
Summary:	Coder module for JPEG files
Summary(pl):	ModuЁ kodera dla plikСw JPEG
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-jpeg
Coder module for JPEG files.

%description coder-jpeg -l pl
ModuЁ kodera dla plikСw JPEG.

%package coder-jpeg2
Summary:	Coder module for JPEG-2000 (JP2/JPC) files using JasPer library
Summary(pl):	ModuЁ kodera dla plikСw JPEG-2000 (JP2/JPC) u©ywaj╠cy biblioteki JasPer
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-jpeg2
Coder module for JPEG-2000 (JP2/JPC) files using JasPer library.

%description coder-jpeg2 -l pl
ModuЁ kodera dla plikСw JPEG-2000 (JP2/JPC) u©ywajacy biblioteki
JasPer.

%package coder-miff
Summary:	Coder module for MIFF files
Summary(pl):	ModuЁ kodera dla plikСw MIFF
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-miff
Coder module for MIFF files.

%description coder-miff -l pl
ModuЁ kodera dla plikСw MIFF.

%package coder-mpeg
Summary:	Coder module for MPEG files
Summary(pl):	ModuЁ kodera dla plikСw MPEG
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-mpeg
Coder module for MPEG files.

%description coder-mpeg -l pl
ModuЁ kodera dla plikСw MPEG.

%package coder-mpr
Summary:	Coder module for ImageMagick MPR and MSL files
Summary(pl):	ModuЁ kodera dla plikСw MPR i MSL ImageMagick
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-mpr
Coder module for Magick Persistent Registry (MPR) and Magick Scripting
Language (MSL) files.

%description coder-mpr -l pl
ModuЁ kodera dla plikСw Magick Persistent Registry (MPR) i Magick
Scripting Language (MSL).

%package coder-pdf
Summary:	Coder module for PDF files
Summary(pl):	ModuЁ kodera dla plikСw PDF
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-pdf
Coder module for PDF files.

%description coder-pdf -l pl
ModuЁ kodera dla plikСw PDF.

%package coder-png
Summary:	Coder module for PNG files
Summary(pl):	Modul kodera dla plikСw PNG
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-png
Coder module for PNG files.

%description coder-png -l pl
ModuЁ kodera dla plikСw PNG.

%package coder-ps2
Summary:	Coder module for Postscript Level II & III (PS2/PS3) files
Summary(pl):	ModuЁ kodera dla plikСw Postscript Level II i III (PS2/PS3)
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-ps2
Coder module for Postscript Level II & III (PS2/PS3) files.

%description coder-ps2 -l pl
ModuЁ kodera dla plikСw Postscript Level II i III (PS2/PS3).

%package coder-svg
Summary:	Coder module for SVG (Scalable Vector Graphics) files
Summary(pl):	ModuЁ kodera dla plikСw SVG (Scalable Vector Graphics)
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-svg
Coder module for SVG (Scalable Vector Graphics) files.

%description coder-svg -l pl
ModuЁ kodera dla plikСw SVG (Scalable Vector Graphics).

%package coder-tiff
Summary:	Coder module for TIFF files
Summary(pl):	ModuЁ kodera dla plikСw TIFF
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-tiff
Coder module for TIFF files.

%description coder-tiff -l pl
ModuЁ kodera dla plikСw TIFF.

%package coder-url
Summary:	Coder module for retrieving files via URL
Summary(pl):	ModuЁ kodera ╤ci╠gaj╠cy pliki o podanym URL
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-url
Coder module for retrieving files via URL.

%description coder-url -l pl
ModuЁ kodera ╤ci╠gaj╠cy pliki o podanym URL.

%package coder-wmf
Summary:	Coder module for WMF files
Summary(pl):	ModuЁ kodera dla plikСw WMF
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description coder-wmf
Coder module for WMF files.

%description coder-wmf -l pl
ModuЁ kodera dla plikСw WMF.

%prep
%setup -q -n %{name}-%{ver}
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I /usr/share/libtool/libltdl
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/include/g++"
%configure \
	CPPFLAGS="$CPPFLAGS" \
	--enable-16bit-pixel \
	--enable-lzw \
	--enable-shared \
	--enable-fast-install \
	--with-gs-font-dir=%{_fontsdir}/Type1 \
	%{?_without_fpx:--without-fpx} \
	%{!?_with_gs:--without-gslib} \
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

%post   c++ -p /sbin/ldconfig
%postun c++ -p /sbin/ldconfig

%files libs
%defattr(644,root,root,755)
%doc Copyright.txt
%attr(755,root,root) %{_libdir}/libMagick-%{ver}.so.*.*

%files
%defattr(644,root,root,755)
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
%{_libdir}/ImageMagick-%{ver}/modules/coders/mpeg.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/mpeg.so
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
%attr(755,root,root) %{_bindir}/composite
%attr(755,root,root) %{_bindir}/convert
%attr(755,root,root) %{_bindir}/conjure
%attr(755,root,root) %{_bindir}/display
%attr(755,root,root) %{_bindir}/identify
%attr(755,root,root) %{_bindir}/import
%attr(755,root,root) %{_bindir}/mogrify
%attr(755,root,root) %{_bindir}/montage

%{_mandir}/man1/[Iacdim]*

%files coder-dps
%defattr(644,root,root,755)
# R: XFree86-DPS (libdps.so)
%{_libdir}/ImageMagick-%{ver}/modules/coders/dps.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/dps.so

%if %{?_without_fpx:0}%{!?_without_fpx:1}
%files coder-fpx
%defattr(644,root,root,755)
# R: fpx
%{_libdir}/ImageMagick-%{ver}/modules/coders/fpx.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/fpx.so
%endif

%files coder-jbig
%defattr(644,root,root,755)
# R: jbigkit (libjbig.so)
%{_libdir}/ImageMagick-%{ver}/modules/coders/jbig.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/jbig.so

%files coder-jpeg
%defattr(644,root,root,755)
# R: libjpeg
%{_libdir}/ImageMagick-%{ver}/modules/coders/jpeg.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/jpeg.so

%if %{?_without_jasper:0}%{!?_without_jasper:1}
%files coder-jpeg2
%defattr(644,root,root,755)
# R: jasper, libjpeg
%{_libdir}/ImageMagick-%{ver}/modules/coders/jp2.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/jp2.so
%endif

%files coder-miff
%defattr(644,root,root,755)
# R: libjpeg, zlib, libbz2
%{_libdir}/ImageMagick-%{ver}/modules/coders/miff.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/miff.so

%files coder-mpr
%defattr(644,root,root,755)
# R: libxml2
%{_libdir}/ImageMagick-%{ver}/modules/coders/mpr.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/mpr.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/msl.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/msl.so

%files coder-pdf
%defattr(644,root,root,755)
# R: libtiff, libjpeg
%{_libdir}/ImageMagick-%{ver}/modules/coders/pdf.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/pdf.so

%files coder-png
%defattr(644,root,root,755)
# R: libpng
%{_libdir}/ImageMagick-%{ver}/modules/coders/png.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/png.so

%files coder-ps2
%defattr(644,root,root,755)
# R: libtiff, libjpeg
%{_libdir}/ImageMagick-%{ver}/modules/coders/ps2.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/ps2.so
%{_libdir}/ImageMagick-%{ver}/modules/coders/ps3.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/ps3.so

%files coder-svg
%defattr(644,root,root,755)
# R: libxml2
%{_libdir}/ImageMagick-%{ver}/modules/coders/svg.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/svg.so

%files coder-tiff
%defattr(644,root,root,755)
# R: libtiff, libjpeg
%{_libdir}/ImageMagick-%{ver}/modules/coders/tiff.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/tiff.so

%files coder-url
%defattr(644,root,root,755)
# R: libxml2
%{_libdir}/ImageMagick-%{ver}/modules/coders/url.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/url.so

%files coder-wmf
%defattr(644,root,root,755)
# R: libwmf, expat, libjpeg, libpng
%{_libdir}/ImageMagick-%{ver}/modules/coders/wmf.la
%attr(755,root,root) %{_libdir}/ImageMagick-%{ver}/modules/coders/wmf.so

%files devel
%defattr(644,root,root,755)
#%%doc README.txt
%doc %{_defaultdocdir}/%{name}-devel-%{version}

%attr(755,root,root) %{_bindir}/Magick-config
%attr(755,root,root) %{_libdir}/libMagick.so
%{_libdir}/libMagick.la
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
%{_mandir}/man3/Image::Magick.*
%{_examplesdir}/%{name}-perl

%if %{?_without_cxx:0}%{!?_without_cxx:1}
%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libMagick++-%{ver}.so.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Magick++-config
%{_libdir}/libMagick++.la
%attr(755,root,root) %{_libdir}/libMagick++.so
%{_prefix}/include/Magick++
%{_prefix}/include/Magick++.h
%{_mandir}/man1/Magick++-config.1*

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libMagick++.a
%endif
