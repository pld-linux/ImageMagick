%include	/usr/lib/rpm/macros.perl
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

%package devel
Summary:	Libraries and header files for ImageMagick development
Summary(es):	Biblioteca estАtica y archivos de inclusiСn para desarrollo con libMagick
Summary(pl):	Biblioteki i pliki nagЁСwkowe dla ImageMagick
Summary(pt_BR):	Biblioteca e arquivos de inclusЦo para desenvolvimento com libMagick
Summary(ru):	Хедеры и библиотеки для программирования с ImageMagick
Summary(uk):	Хедери та б╕бл╕отеки для програмування з ImageMagick
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
Summary(es):	Static libraries for libMagick development
Summary(pl):	Biblioteki statyczne ImageMagick
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com libMagick
Summary(ru):	Статические библиотеки для программирования с ImageMagick
Summary(uk):	Статичн╕ б╕бл╕отеки для програмування з ImageMagick
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
ImageMagick static libraries.

%description static -l es
Static libraries for libMagick development.

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
Summary(es):	Perl Module to use ImageMagick
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

%description perl -l es
This packages provides a perl module to access ImagickMagick functions
from perl scripts.

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

%package libs
Summary:	ImageMagick libraries
Summary(es):	ImageMagick dynamic libraries
Summary(pl):	Biblioteki ImageMagick
Summary(pt_BR):	Bibliotecas dinБmicas do ImageMagick
Group:		X11/Libraries

%description libs
ImageMagick libraries.

%description libs -l es
ImageMagick dynamic libraries.

%description libs -l pl
Biblioteki ImageMagick.

%description libs -l pt_BR
Bibliotecas dinБmicas do ImageMagick.

%package c++
Summary:	ImageMagick Magick++ library
Summary(es):	ImageMagick dynamic libraries
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

%description c++ -l es
ImageMagick C++ dynamic libraries.

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
Summary(es):	Static libraries for libMagick development
Summary(pl):	Interfejs C++ do ImageMagick - biblioteka statyczna
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com libMagick
Summary(ru):	Статические библиотеки C++ для программирования с ImageMagick
Summary(uk):	Статичн╕ б╕бл╕отеки C++ для програмування з ImageMagick
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
Bibliotecas estАticas para desenvolvimento com libMagick++

%description c++-static -l ru
Это отдельный пакет со статическими библиотеками, которые больше не
входят в ImageMagick-c++-devel.

%description c++-static -l uk
Це окремий пакет з╕ статичними б╕бл╕отеками, як╕ б╕льше не входять до
складу ImageMagick-c++-devel.

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
