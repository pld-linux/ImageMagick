#
# Conditional build:
%bcond_without	djvu		# without DJVU module
%bcond_without	fpx		# without FlashPIX module (which uses fpx library)
%bcond_without	graphviz	# without Graphviz support
%bcond_with	gs		# with PostScript support through ghostscript library (warning: breaks jpeg!)
%bcond_without	jasper		# without JPEG2000 module (which uses jasper library)
%bcond_without	wmf		# without WMF module (which uses libwmf library)
%bcond_without	cxx		# without Magick++
%bcond_without	exr		# without OpenEXR module
#
%include	/usr/lib/rpm/macros.perl
%define		ver 6.5.2
%define		pver	3
%define		QuantumDepth	16
Summary:	Image display, conversion, and manipulation under X
Summary(de.UTF-8):	Darstellen, Konvertieren und Bearbeiten von Grafiken unter X
Summary(es.UTF-8):	Exhibidor, convertidor y manipulador de imágenes bajo X
Summary(fr.UTF-8):	Visualisation, conversion, et manipulation d'images sous X
Summary(pl.UTF-8):	Narzędzie do wyświetlania, konwersji i manipulacji grafikami
Summary(pt_BR.UTF-8):	Exibidor, conversor e manipulador de imagens sob X
Summary(ru.UTF-8):	Просмотр, конвертирование, обработка изображений под X Window
Summary(tr.UTF-8):	X altında resim gösterme, çevirme ve değişiklik yapma
Summary(uk.UTF-8):	Перегляд, конвертування та обробка зображень під X Window
Name:		ImageMagick
Version:	%{ver}%{?pver:.%{pver}}
Release:	1
Epoch:		1
License:	Apache-like
Group:		X11/Applications/Graphics
Source0:	http://www.imagemagick.org/download/%{name}-%{ver}-%{pver}.tar.bz2
# Source0-md5:	e40950e40574d823dbe13542f7a537c0
#Source0:	http://dl.sourceforge.net/imagemagick/%{name}-%{ver}.tar.bz2
Patch0:		%{name}-ac.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-libpath.patch
Patch3:		%{name}-ldflags.patch
URL:		http://www.imagemagick.org/
BuildRequires:	OpenEXR-devel
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.9
BuildRequires:	bzip2-devel >= 1.0.1
%{?with_djvu:BuildRequires:	djvulibre-devel}
BuildRequires:	expat-devel >= 1.95.7
BuildRequires:	freetype-devel >= 2.0.2-2
BuildRequires:	gd-devel >= 2.0.15
%{?with_gs:BuildRequires:	ghostscript-devel}
%{?with_graphviz:BuildRequires:	graphviz-devel >= 2.6}
%{?with_jasper:BuildRequires:	jasper-devel >= 1.700.5}
BuildRequires:	jbigkit-devel
BuildRequires:	lcms-devel
%{?with_fpx:BuildRequires:	libfpx-devel >= 1.2.0.4-3}
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	librsvg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5
%{?with_wmf:BuildRequires:	libwmf-devel >= 2:0.2.2}
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.315
# only checked for, but only supplied scripts/txt2html is used
#BuildRequires:	txt2html
BuildRequires:	xorg-lib-libXext
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	ImageMagick-coder-dps
Obsoletes:	ImageMagick-coder-mpeg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		modulesdir	%{_libdir}/ImageMagick-%{ver}/modules-Q%{QuantumDepth}

%description
ImageMagick is an image display, conversion, and manipulation tool. It
runs under X Window. It is very powerful in terms of it's ability to
allow the user to edit images. It can handle many different formats as
well.

%description -l de.UTF-8
ImageMagick ist ein Tool zur Bildanzeige, -konvertierung und
manipulation, -das unter X-Window läuft. Es ist enorm leitungsfähig in
Bezug auf die Grafikmanipulationsfunktionen, die es dem Anwender
bietet, und auf die Vielfalt der unterstützten Formate.

%description -l es.UTF-8
ImageMagick es una herramienta para manipular, convertir y exhibir
imágenes, que funciona bajo X Window. Es una herramienta potente que
permite editar imágenes, pudiendo manipular varios formatos
diferentes.

%description -l fr.UTF-8
ImageMagick est un outil d'affichage, de conversion et de manipulation
d'images. Il tourne sous X Window et est très puissant en termes de
capacité d'édition des images. Il peut aussi gérer de nombreux formats
différents.

%description -l pl.UTF-8
ImageMagick jest narzędziem do manipulacji, konwersji i wyświetlania.
W skład pakietu wchodzą zarówno narzędzia X Window jak i do używania z
linii poleceń umożliwiające edycję plików graficznych. Narzędzia z
pakietu ImageMagick potrafią obsłużyć wiele różnych formatów
graficznych.

%description -l pt_BR.UTF-8
ImageMagick é uma ferramenta para manipular, converter e exibir
imagens, que funciona sob o X Window. É uma ferramenta poderosa que
permite editar imagens, podendo tratar vários formatos diferentes.

%description -l ru.UTF-8
ImageMagick - это утилита для просмотра, конвертирования и обработки
изображений. Она работает под X Window. ImageMagick предоставляет
пользователю широкие возможности по обработке изображений в самых
разнообразных форматах.

%description -l tr.UTF-8
ImageMagick bir resim gösterme, çevirme ve değişiklik yapma
programıdır. X Window pencereleme sistemi altında çalışır. Kullanıcıya
resimler üzerinde değişiklik yapma açısından pek çok olanak sunar. Bir
çok resim biçimini rahatlıkla kullanabilir.

%description -l uk.UTF-8
ImageMagick - це утиліта для перегляду, конвертування та обробки
зображень. Вона працює під X Window. ImageMagick дає користувачу
широкі можливості по обробці зображень в різноманітних форматах.

%package doc
Summary:	ImageMagick documentation
Summary(pl.UTF-8):	Dokumentacja do ImageMagick
Group:		Documentation

%description doc
Documentation for ImageMagick.

%description doc -l pl.UTF-8
Dokumentacja do ImageMagick.

%package libs
Summary:	ImageMagick libraries
Summary(pl.UTF-8):	Biblioteki ImageMagick
Summary(pt_BR.UTF-8):	Bibliotecas dinâmicas do ImageMagick
Group:		X11/Libraries

%description libs
ImageMagick libraries.

%description libs -l pl.UTF-8
Biblioteki ImageMagick.

%description libs -l pt_BR.UTF-8
Bibliotecas dinâmicas do ImageMagick.

%package devel
Summary:	Libraries and header files for ImageMagick development
Summary(es.UTF-8):	Biblioteca estática y archivos de inclusión para desarrollo con libMagick
Summary(pl.UTF-8):	Biblioteki i pliki nagłówkowe dla ImageMagick
Summary(pt_BR.UTF-8):	Biblioteca e arquivos de inclusão para desenvolvimento com libMagick
Summary(ru.UTF-8):	Хедеры и библиотеки для программирования с ImageMagick
Summary(uk.UTF-8):	Хедери та бібліотеки для програмування з ImageMagick
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	bzip2-devel
Requires:	freetype-devel
Requires:	lcms-devel
Requires:	libjpeg-devel
Requires:	libltdl-devel
Requires:	libtiff-devel
Requires:	xorg-lib-libXext-devel
Requires:	zlib-devel

%description devel
This is the ImageMagick development package. It includes header files
for use in developing your own applications that make use of the
ImageMagick code and/or APIs.

%description devel -l de.UTF-8
Dies ist das ImageMagick-Entwicklerpaket. Es enthält Header-Dateien
zum Entwickeln von Anwendungen, die ImageMagick-Code und/oder -APIs
nutzen.

%description devel -l es.UTF-8
Este es el paquete de desarrollo ImageMagick. Incluye las bibliotecas
y los archivos de inclusión para el desarrollo de sus propias
aplicaciones que hacen uso del código ImageMagick y/el APIs.

%description devel -l fr.UTF-8
Paquetage de développement ImageMagick. Contient les bibliothèques
statiques et les en-têtes utilisés pour créer vos propres applications
utilisant le code d'ImageMagick et/ou ses APIs.

%description devel -l pl.UTF-8
Pakiet ten zawieraja pliki potrzebne przy kompilowaniu programów
wykorzystujących blibliotekę ImageMagick takie jak pliki nagłówkowe i
dokumentację niezbędną przy pisaniu własnych programów z
wykorzystaniem API jakie udostępnia ImageMagick.

%description devel -l pt_BR.UTF-8
Este é o pacote de desenvolvimento ImageMagick. Inclui as bibliotecas
e os arquivos de inclusão para o desenvolvimento de suas próprias
aplicações que fazem uso do código ImageMagick e/ou APIs.

%description devel -l ru.UTF-8
Это пакет разработчика для программирования с ImageMagick. Он включает
хедеры и библиотеки для использования в программах, которые используют
код или API ImageMagick.

%description devel -l tr.UTF-8
Bu paket, ImageMagick uygulama arayüzünü kullanan programlar
geliştirmek için gereken başlık dosyalarını ve kitaplıkları içerir.

%description devel -l uk.UTF-8
Це пакет для програмування з ImageMagick. Він містить хедери та
бібліотеки для використання в програмах, що використовують код або API
ImageMagick.

%package static
Summary:	ImageMagick static libraries
Summary(pl.UTF-8):	Biblioteki statyczne ImageMagick
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libMagick
Summary(ru.UTF-8):	Статические библиотеки для программирования с ImageMagick
Summary(uk.UTF-8):	Статичні бібліотеки для програмування з ImageMagick
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
ImageMagick static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne ImageMagick.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libMagick.

%description static -l ru.UTF-8
Это отдельный пакет со статическими библиотеками, которые больше не
входят в ImageMagick-devel.

%description static -l uk.UTF-8
Це окремий пакет зі статичними бібліотеками, які більше не входять до
складу ImageMagick-devel.

%package perl
Summary:	Libraries and modules for access to ImageMagick from Perl
Summary(pl.UTF-8):	Biblioteki i moduły Perla dla ImageMagick
Summary(pt_BR.UTF-8):	Módulo perl para uso com o ImageMagick
Summary(ru.UTF-8):	Библиотеки и модули для доступа к ImageMagick из perl
Summary(uk.UTF-8):	Бібліотеки та модулі для доступу до ImageMagick з Perl
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	perl-dirs

%description perl
This is the ImageMagick Perl support package. It perl modules and
support files for access to ImageMagick library from perl without
unuseful forking or such.

%description perl -l pl.UTF-8
Biblioteki i moduły umożliwiające korzystanie z ImageMagick z poziomu
Perla.

%description perl -l pt_BR.UTF-8
Este pacote fornece um módulo perl para acessar funções do ImageMagick
em scripts Perl.

%description perl -l ru.UTF-8
Это пакет ImageMagick для поддержки perl. Он включает модули perl и
вспомогательные файлы для доступа к библиотеке ImageMagick из Perl.

%description perl -l uk.UTF-8
Це пакет ImageMagick для підтримки Perl. Він містить модулі Perl та
додаткові файли для доступу до бібліотеки ImageMagick з Perl.

%package c++
Summary:	ImageMagick Magick++ library
Summary(pl.UTF-8):	Biblioteka Magick++
Summary(pt_BR.UTF-8):	Bibliotecas dinâmicas do ImageMagick
Summary(ru.UTF-8):	Библиотека Magick++ (C++ интерфейс для ImageMagick'а)
Summary(uk.UTF-8):	Бібліотека Magick++ (інтерфейс C++ для ImageMagick)
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description c++
This package contains the Magick++ library, a C++ binding to the
ImageMagick graphics manipulation library.

Install ImageMagick-c++ if you want to use any applications that use
Magick++.

%description c++ -l pl.UTF-8
Pakiet zawiera bibliotekę Magick++ - interfejs w C++ do biblioteki
ImageMagick. Jest potrzebny do uruchamiania programów korzystających z
Magick++.

%description c++ -l pt_BR.UTF-8
Bibliotecas dinâmicas C++ do ImageMagick.

%description c++ -l ru.UTF-8
Magick++ -- объектно-ориентированная библиотека, представляющая из
себя C++ API для ImageMagick (библиотеки для просмотра,
конвертирования и обработки изображений).

%description c++ -l uk.UTF-8
Magick++ -- об'єкто-орієнтована бібліотека, що являє собою C++ API для
ImageMagick (бібліотеки для перегляду, конвертування та обробки
зображень).

%package c++-devel
Summary:	C++ bindings for the ImageMagick library
Summary(es.UTF-8):	Biblioteca estática y archivos de inclusión para desarrollo con libMagick++
Summary(pl.UTF-8):	Pliki nagłówkowe z interfejsem C++ do ImageMagick
Summary(pt_BR.UTF-8):	Biblioteca e arquivos de inclusão para desenvolvimento com libMagick++
Summary(ru.UTF-8):	Хедеры и библиотеки для разработок с использованием Magick++ (C++ интерфейс для ImageMagick'а)
Summary(uk.UTF-8):	Хедери та бібліотеки для розробок з використанням Magick++ (інтерфейсу C++ для ImageMagick)
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

%description c++-devel -l es.UTF-8
Este es el paquete de desarrollo ImageMagick. Incluye las bibliotecas
estáticas y los archivos de inclusión para el desarrollo de sus
propias aplicaciones que hacen uso del código ImageMagick y/el APIs.

%description c++-devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe potrzebne do kompilowania programów
korzystających z Magick++.

%description c++-devel -l pt_BR.UTF-8
Este é o pacote de desenvolvimento libMagick++. Inclui as bibliotecas
e os arquivos de inclusão para o desenvolvimento de suas próprias
aplicações C++ que fazem uso do código ImageMagick e/ou APIs.

%description c++-devel -l ru.UTF-8
Это пакет разработчика для программирования с ImageMagick. Он включает
хедеры и библиотеки для использования в программах, которые используют
код или API Magick++ (C++ интерфейс для ImageMagick'а).

%description c++-devel -l uk.UTF-8
Це пакет для програмування з ImageMagick. Він містить хедери та
бібліотеки для використання в програмах, що використовують код або API
Magick++ (інтерфейс C++ для ImageMagick).

%package c++-static
Summary:	C++ bindings for the ImageMagick - static library
Summary(pl.UTF-8):	Interfejs C++ do ImageMagick - biblioteka statyczna
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libMagick
Summary(ru.UTF-8):	Статические библиотеки C++ для программирования с ImageMagick
Summary(uk.UTF-8):	Статичні бібліотеки C++ для програмування з ImageMagick
Group:		X11/Development/Libraries
Requires:	%{name}-c++-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description c++-static
C++ bindings for the ImageMagick - static library.

%description c++-static -l pl.UTF-8
Biblioteka Magick++ w wersji statycznej.

%description c++-static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libMagick++.

%description c++-static -l ru.UTF-8
Это отдельный пакет со статическими библиотеками, которые больше не
входят в ImageMagick-c++-devel.

%description c++-static -l uk.UTF-8
Це окремий пакет зі статичними бібліотеками, які більше не входять до
складу ImageMagick-c++-devel.

%package coder-djvu
Summary:	Coder module for DJVU files
Summary(pl.UTF-8):	Moduł kodera dla plików DJVU
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-djvu
Coder module for DJVU files.

%description coder-djvu -l pl
Moduł kodera dla plików DJVU.

%package coder-dot
Summary:	Coder module for GraphViz DOT files
Summary(pl.UTF-8):	Moduł kodera dla plików GraphViz DOT
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-dot
Coder module for GraphViz DOT files.

%description coder-dot -l pl.UTF-8
Moduł kodera dla plików GraphViz DOT.

%package coder-exr
Summary:	Coder module for ILM EXR files
Summary(pl.UTF-8):	Moduł kodera dla plików EXR ILM
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-exr
Coder module for ILM EXR files.

%description coder-exr -l pl.UTF-8
Moduł kodera dla plików EXR ILM.

%package coder-fpx
Summary:	Coder module for FlashPIX (FPX) files
Summary(pl.UTF-8):	Moduł kodera dla plików FlashPIX (FPX)
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-fpx
Coder module for FlashPIX (FPX) files.

%description coder-fpx -l pl.UTF-8
Moduł kodera dla plików FlashPIX (FPX).

%package coder-jbig
Summary:	Coder module for JBIG files
Summary(pl.UTF-8):	Moduł kodera dla plików JBIG
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-jbig
Coder module for JBIG files.

%description coder-jbig -l pl.UTF-8
Moduł kodera dla plików JBIG.

%package coder-jpeg
Summary:	Coder module for JPEG files
Summary(pl.UTF-8):	Moduł kodera dla plików JPEG
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-jpeg
Coder module for JPEG files.

%description coder-jpeg -l pl.UTF-8
Moduł kodera dla plików JPEG.

%package coder-jpeg2
Summary:	Coder module for JPEG-2000 (JP2/JPC) files using JasPer library
Summary(pl.UTF-8):	Moduł kodera dla plików JPEG-2000 (JP2/JPC) używający biblioteki JasPer
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-jpeg2
Coder module for JPEG-2000 (JP2/JPC) files using JasPer library.

%description coder-jpeg2 -l pl.UTF-8
Moduł kodera dla plików JPEG-2000 (JP2/JPC) używajacy biblioteki
JasPer.

%package coder-miff
Summary:	Coder module for MIFF files
Summary(pl.UTF-8):	Moduł kodera dla plików MIFF
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-miff
Coder module for MIFF files.

%description coder-miff -l pl.UTF-8
Moduł kodera dla plików MIFF.

%package coder-mpr
Summary:	Coder module for ImageMagick MPR and MSL files
Summary(pl.UTF-8):	Moduł kodera dla plików MPR i MSL ImageMagick
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-mpr
Coder module for Magick Persistent Registry (MPR) and Magick Scripting
Language (MSL) files.

%description coder-mpr -l pl.UTF-8
Moduł kodera dla plików Magick Persistent Registry (MPR) i Magick
Scripting Language (MSL).

%package coder-pdf
Summary:	Coder module for PDF files
Summary(pl.UTF-8):	Moduł kodera dla plików PDF
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	ghostscript

%description coder-pdf
Coder module for PDF files.

%description coder-pdf -l pl.UTF-8
Moduł kodera dla plików PDF.

%package coder-png
Summary:	Coder module for PNG files
Summary(pl.UTF-8):	Modul kodera dla plików PNG
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-png
Coder module for PNG files.

%description coder-png -l pl.UTF-8
Moduł kodera dla plików PNG.

%package coder-ps2
Summary:	Coder module for Postscript Level II & III (PS2/PS3) files
Summary(pl.UTF-8):	Moduł kodera dla plików Postscript Level II i III (PS2/PS3)
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-ps2
Coder module for Postscript Level II & III (PS2/PS3) files.

%description coder-ps2 -l pl.UTF-8
Moduł kodera dla plików Postscript Level II i III (PS2/PS3).

%package coder-svg
Summary:	Coder module for SVG (Scalable Vector Graphics) files
Summary(pl.UTF-8):	Moduł kodera dla plików SVG (Scalable Vector Graphics)
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-svg
Coder module for SVG (Scalable Vector Graphics) files.

%description coder-svg -l pl.UTF-8
Moduł kodera dla plików SVG (Scalable Vector Graphics).

%package coder-tiff
Summary:	Coder module for TIFF files
Summary(pl.UTF-8):	Moduł kodera dla plików TIFF
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-tiff
Coder module for TIFF files.

%description coder-tiff -l pl.UTF-8
Moduł kodera dla plików TIFF.

%package coder-url
Summary:	Coder module for retrieving files via URL
Summary(pl.UTF-8):	Moduł kodera ściągający pliki o podanym URL
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-url
Coder module for retrieving files via URL.

%description coder-url -l pl.UTF-8
Moduł kodera ściągający pliki o podanym URL.

%package coder-wmf
Summary:	Coder module for WMF files
Summary(pl.UTF-8):	Moduł kodera dla plików WMF
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coder-wmf
Coder module for WMF files.

%description coder-wmf -l pl.UTF-8
Moduł kodera dla plików WMF.

%prep
%setup -q -n %{name}-%{ver}-%{pver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__perl} -pi -e 's,lib/graphviz,%{_lib}/graphviz,' configure.ac
find -type f -exec perl -pi -e 's=!/usr/local/bin/perl=!/usr/bin/perl='  {} \;

# avoid rebuilding (broken paths in scripts/Makefile.am)
touch www/Magick++/NEWS.html www/Magick++/ChangeLog.html

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-fast-install \
	--enable-lzw \
	--enable-shared \
	--disable-ltdl-install \
	--without-dps \
	--with%{!?with_graphviz:out}-djvu \
	--with%{!?with_graphviz:out}-dot \
	--with%{!?with_fpx:out}-fpx \
	--with%{!?with_gs:out}-gslib \
	--with%{!?with_jasper:out}-jp2 \
	--with%{!?with_cxx:out}-magick_plus_plus \
	--with%{!?with_wmf:out}-wmf \
	--%{!?with_exr:dis}%{?with_exr:en}able-hdri \
	--with-gs-font-dir=%{_fontsdir}/Type1 \
	--with-modules \
	--with-perl=%{__perl} \
	--with-perl-options="INSTALLDIRS=vendor" \
	--with-quantum-depth=%{QuantumDepth} \
	--with-threads \
	--with-ttf \
	--with-x

%{__make}
%{__perl} -pi -e 's,/%{name}-%{ver}/,/%{name}-doc-%{version}/,' utilities/*.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-perl

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgdocdir=%{_docdir}/%{name}-doc-%{version}

install PerlMagick/demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-perl
rm -f $RPM_BUILD_ROOT%{modulesdir}/{coders,filters}/*.a
rm -f $RPM_BUILD_ROOT%{modulesdir}/coders/dps.{la,so}
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Image/Magick/.packlist
rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{_datadir}/ImageMagick-%{ver}/{ChangeLog,LICENSE,NEWS.txt}

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
%{_datadir}/ImageMagick-%{ver}/config/sRGB.icm

# ========= coders without additional deps
%attr(755,root,root) %{modulesdir}/coders/art.so
%{modulesdir}/coders/art.la
%attr(755,root,root) %{modulesdir}/coders/avi.so
%{modulesdir}/coders/avi.la
%attr(755,root,root) %{modulesdir}/coders/avs.so
%{modulesdir}/coders/avs.la
%attr(755,root,root) %{modulesdir}/coders/bmp.so
%{modulesdir}/coders/bmp.la
%attr(755,root,root) %{modulesdir}/coders/braille.so
%{modulesdir}/coders/braille.la
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
%attr(755,root,root) %{modulesdir}/coders/dds.so
%{modulesdir}/coders/dds.la
%attr(755,root,root) %{modulesdir}/coders/dib.so
%{modulesdir}/coders/dib.la
%attr(755,root,root) %{modulesdir}/coders/dng.so
%{modulesdir}/coders/dng.la
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
%attr(755,root,root) %{modulesdir}/coders/hrz.so
%{modulesdir}/coders/hrz.la
%attr(755,root,root) %{modulesdir}/coders/html.so
%{modulesdir}/coders/html.la
%attr(755,root,root) %{modulesdir}/coders/icon.so
%{modulesdir}/coders/icon.la
%attr(755,root,root) %{modulesdir}/coders/info.so
%{modulesdir}/coders/info.la
%attr(755,root,root) %{modulesdir}/coders/inline.so
%{modulesdir}/coders/inline.la
%attr(755,root,root) %{modulesdir}/coders/ipl.so
%{modulesdir}/coders/ipl.la
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
%attr(755,root,root) %{modulesdir}/coders/thumbnail.so
%{modulesdir}/coders/thumbnail.la
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
%attr(755,root,root) %{modulesdir}/coders/xps.so
%{modulesdir}/coders/xps.la
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
%attr(755,root,root) %{_bindir}/conjure
%attr(755,root,root) %{_bindir}/convert
%attr(755,root,root) %{_bindir}/display
%attr(755,root,root) %{_bindir}/identify
%attr(755,root,root) %{_bindir}/import
%attr(755,root,root) %{_bindir}/mogrify
%attr(755,root,root) %{_bindir}/montage
%attr(755,root,root) %{_bindir}/stream

%{_mandir}/man1/ImageMagick.1*
%{_mandir}/man1/animate.1*
%{_mandir}/man1/compare.1*
%{_mandir}/man1/composite.1*
%{_mandir}/man1/convert.1*
%{_mandir}/man1/conjure.1*
%{_mandir}/man1/display.1*
%{_mandir}/man1/identify.1*
%{_mandir}/man1/import.1*
%{_mandir}/man1/mogrify.1*
%{_mandir}/man1/montage.1*
%{_mandir}/man1/stream.1*

%files doc
%defattr(644,root,root,755)
%doc %{_defaultdocdir}/%{name}-doc-%{version}

%files libs
%defattr(644,root,root,755)
%doc ChangeLog LICENSE
%attr(755,root,root) %{_libdir}/libMagickCore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libMagickCore.so.2
%attr(755,root,root) %{_libdir}/libMagickWand.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libMagickWand.so.2

%if %{with djvu}
%files coder-djvu
%defattr(644,root,root,755)
# R: djvulibre
%attr(755,root,root) %{modulesdir}/coders/djvu.so
%{modulesdir}/coders/djvu.la
%endif

%files coder-dot
%defattr(644,root,root,755)
# R: graphviz, gd
%attr(755,root,root) %{modulesdir}/coders/dot.so
%{modulesdir}/coders/dot.la

%if %{with exr}
%files coder-exr
%defattr(644,root,root,755)
# R: OpenEXR
%attr(755,root,root) %{modulesdir}/coders/exr.so
%{modulesdir}/coders/exr.la
%endif

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
# R: libxml2, librsvg
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

%if %{with wmf}
%files coder-wmf
%defattr(644,root,root,755)
# R: libwmf, expat, libjpeg, libpng
%attr(755,root,root) %{modulesdir}/coders/wmf.so
%{modulesdir}/coders/wmf.la
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Magick-config
%attr(755,root,root) %{_bindir}/MagickCore-config
%attr(755,root,root) %{_bindir}/MagickWand-config
%attr(755,root,root) %{_bindir}/Wand-config
%attr(755,root,root) %{_libdir}/libMagickCore.so
%attr(755,root,root) %{_libdir}/libMagickWand.so
%dir %{_includedir}/ImageMagick
%{_libdir}/libMagickCore.la
%{_libdir}/libMagickWand.la
%{_includedir}/ImageMagick/magick
%{_includedir}/ImageMagick/wand
%{_pkgconfigdir}/ImageMagick.pc
%{_pkgconfigdir}/MagickCore.pc
%{_pkgconfigdir}/MagickWand.pc
%{_pkgconfigdir}/Wand.pc
%{_mandir}/man1/Magick-config.1*
%{_mandir}/man1/MagickCore-config.1*
%{_mandir}/man1/MagickWand-config.1*
%{_mandir}/man1/Wand-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libMagickCore.a
%{_libdir}/libMagickWand.a

%files perl
%defattr(644,root,root,755)
%{perl_vendorarch}/Image/*
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
%attr(755,root,root) %ghost %{_libdir}/libMagick++.so.2

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Magick++-config
%{_libdir}/libMagick++.la
%attr(755,root,root) %{_libdir}/libMagick++.so
%{_includedir}/ImageMagick/Magick++
%{_includedir}/ImageMagick/Magick++.h
%{_pkgconfigdir}/ImageMagick++.pc
%{_pkgconfigdir}/Magick++.pc
%{_mandir}/man1/Magick++-config.1*

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libMagick++.a
%endif
