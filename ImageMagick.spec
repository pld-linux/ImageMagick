Summary:	Image display, conversion, and manipulation under X
Summary(de):	Darstellen, Konvertieren und Bearbeiten von Grafiken unter X
Summary(fr):	Visualisation, conversion, et manipulation d'images sous X.
Summary(pl):	Narzêdzie do wy¶wietlania, konwersji i manipulacji grafikami
Summary(tr):	X altýnda resim gösterme, çevirme ve deðiþiklik yapma
Name:		ImageMagick
Version:	4.2.8
Release:	2
Copyright:	freeware
Serial:		1
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source:		ftp://ftp.wizards.dupont.com/pub/ImageMagick/%{name}-%{version}.tar.gz
URL:		http://www.wizards.dupont.com/cristy/ImageMagick.html
BuildRequires:	perl => 5.005_61
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	freetype-devel
Requires:	%{name}-libs = %{version}
Buildroot:	/tmp/%{name}-%{version}-root

%description
ImageMagick is an image display, conversion, and manipulation tool. It runs
under X windows. It is very powerful in terms of it's ability to allow the
user to edit images.  It can handle many different formats as well.

%description -l de
ImageMagick ist ein Tool zur Bildanzeige, -konvertierung und manipulation,
-das unter X-Windows läuft. Es ist enorm leitungsfähig in Bezug auf die
Grafikmanipulationsfunktionen, die es dem Anwender bietet, und auf die
Vielfalt der unterstützten Formate.

%description -l fr
ImageMagick est un outil d'affichage, de conversion et de manipulation
d'images. Il tourne sous X Window et est très puissant en termes de capacité
d'édition des images. Il peut aussi gérer de nombreux formats différents.

%description -l pl
ImageMagic jest narzêdziem do manipulacji, konwersji i wy¶wietlania. W sk³ad
pakietu wchodz± zarówno narzêdzia X Window jak i do u¿ywania z linii poleceñ
umo¿liwiaj±ce edycjê plików graficznych. Narzêdzia z pakietu ImageMagic
potrafi± obs³u¿yæ wiele ró¿ncyh formatów graficznych.

%description -l tr
ImageMagick bir resim gösterme, çevirme ve deðiþiklik yapma programýdýr. X
Window pencereleme sistemi altýnda çalýþýr. Kullanýcýya resimler üzerinde
deðiþiklik yapma açýsýndan pek çok olanak sunar. Bir çok resim biçimini
rahatlýkla kullanabilir.

%package devel
Summary:	Libraries and header files for ImageMagick development
Summary(pl):	Biblioteki i pliki nag³ówkowe dla ImageMagick'a
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This is the ImageMagick development package.  It includes the static
libraries and header files for use in developing your own applications that
make use of the ImageMagick code and/or APIs.

%description -l de devel
Dies ist das ImageMagick-Entwicklerpaket. Es enthält die statischen
Libraries und Header-Dateien zum Entwickeln von Anwendungen, die
ImageMagick-Code und/oder -APIs nutzen.

%description -l fr devel
Paquetage de développement ImageMagick. Contient les bibliothèques statiques
et les en-têtes utilisés pour créer vos propres applications utilisant le
code d'ImageMagick et/ou ses APIs.

%description -l pl devel
Pakiet ten zawieraja pliki potrzebne przy kompilowaniu programów
wykorzystuj±cych blibliotekê ImageMagick takie jak pliki nag³ówkowe,
biblioteki statyczne i dokumentacjê niezbêdn± przy pisaniu w³asnych
programów z wykorzystaniem API jakie udostêpnia ImageMagick.

%description -l tr devel
Bu paket, ImageMagick uygulama arayüzünü kullanan programlar geliþtirmek
için gereken baþlýk dosyalarýný ve kitaplýklarý içerir.

%package static
Summary:	ImageMagick static libraries
Summary(pl): 	Biblioteki statyczne ImageMagick
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
ImageMagick static libraries.

%description -l pl devel
Biblioteki statyczne ImageMagick.

%package perl
Summary:	libraries and modules for access to ImageMagick from perl
Summary(pl):	Biblioteki i modu³y perl dla ImageMagick'a
Group:		Development/Languages/Perl  
Group(pl):	Programowanie/Jêzyki/Perl
Requires:	%{name} = %{version}
%requires_eq	perl

%description perl
This is the ImageMagick perl support package.  It perl modules and support
files for access to ImageMagick library from perl without unuseful forking
or such.

%description -l pl perl
Biblioteki i modu³y umo¿liwiaj±ce korzystanie z ImageMagick'a z poziomu
perla. 

%package libs
Summary:        ImageMagick libraries
Summary(pl):    Biblioteki ImageMagick
Group:          X11/Libraries
Group(pl):      X11/Biblioteki

%description libs
ImageMagick libraries.

%description -l pl libs
Biblioteki ImageMagick.

%prep
%setup -q

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure  %{_target_platform} \
	--prefix=/usr/X11R6 \
	--includedir=/usr/X11R6/include/X11 \
	--enable-shared \
	--enable-lzw \
	--enable-16bit-pixel \
	--with-perl \
	--with-ttf \
	--with-x

make 

%install
rm -fr $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{perl_archlib}

make install \
	DESTDIR=$RPM_BUILD_ROOT 

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*
strip --strip-unneeded \
	$RPM_BUILD_ROOT/%{perl_sitearch}/auto/Image/Magick/Magick.so

gzip -9nf $RPM_BUILD_ROOT/usr/{X11R6/share/man/man*/*,share/man/man3/*} \
	README.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*

%files
%defattr(644,root,root,755)
/usr/X11R6/share/ImageMagick

%attr(755,root,root) /usr/X11R6/bin/animate
%attr(755,root,root) /usr/X11R6/bin/combine
%attr(755,root,root) /usr/X11R6/bin/convert
%attr(755,root,root) /usr/X11R6/bin/display
%attr(755,root,root) /usr/X11R6/bin/identify
%attr(755,root,root) /usr/X11R6/bin/import
%attr(755,root,root) /usr/X11R6/bin/mogrify
%attr(755,root,root) /usr/X11R6/bin/montage
%attr(755,root,root) /usr/X11R6/bin/xtp

/usr/X11R6/share/man/man[145]/*

%files devel
%defattr(644,root,root,755)
%doc www ImageMagick.html README.txt.gz

%attr(755,root,root) /usr/X11R6/bin/Magick-config
%attr(755,root,root) /usr/X11R6/lib/lib*.so

/usr/X11R6/include/X11/magick

%files static
%defattr(644,root,root,755)
/usr/X11R6/lib/lib*.a

%files perl
%defattr(644,root,root,755)
%{perl_sitearch}/Image
%dir %{perl_sitearch}/auto/Image
%dir %{perl_sitearch}/auto/Image/Magick
%{perl_sitearch}/auto/Image/Magick/autosplit.ix
%{perl_sitearch}/auto/Image/Magick/Magick.bs
%attr(755,root,root) %{perl_sitearch}/auto/Image/Magick/Magick.so
%{_mandir}/man3/Image::Magick.*
