Summary:	Image display, conversion, and manipulation under X
Summary(de):	Darstellen, Konvertieren und Bearbeiten von Grafiken unter X
Summary(fr):	Visualisation, conversion, et manipulation d'images sous X.
Summary(pl):	Narzêdzie do wy¶wietlania, konwersji i manipulacji grafikami
Summary(tr):	X altýnda resim gösterme, çevirme ve deðiþiklik yapma
Name:		ImageMagick
Version:	4.1.0
Release:	5
Copyright:	freeware
Serial:		1
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source:		ftp://ftp.wizards.dupont.com/pub/ImageMagick/%{name}-%{version}.tar.gz
URL:		http://www.wizards.dupont.com/cristy/ImageMagick.html
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
umozliwiaj±ce edycjê plików graficznych. Narzêdzia z pakietu ImageMagic
potrafi± obs³u¿yæ wiele ró¿ncyh formatów graficznych.

%description -l tr
ImageMagick bir resim gösterme, çevirme ve deðiþiklik yapma programýdýr. X
Window pencereleme sistemi altýnda çalýþýr. Kullanýcýya resimler üzerinde
deðiþiklik yapma açýsýndan pek çok olanak sunar. Bir çok resim biçimini
rahatlýkla kullanabilir.

%package	devel
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
wykorzystuj±cyh blibliotekê ImageMagick takie ja pliki nag³ówkowe,
biblioteki statyczne i dokumentacjê niezbêdn± przy pisaniu w³asnych
programów z wykorzystaniem API jakie udostêpnia ImageMagick.

%description -l tr devel
Bu paket, ImageMagick uygulama arayüzünü kullanan programlar geliþtirmek
için gereken baþlýk dosyalarýný ve kitaplýklarý içerir.

%package	static
Summary:	ImageMagick static libraries
Summary(pl): 	Biblioteki statyczne ImageMagick
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
ImageMagick static libraries.

%description -l pl devel
Biblioteki statyczne ImageMagick.

%package	perl
Summary:	libraries and modules for access to ImageMagick from perl
Summary(pl):	Biblioteki i modu³y perl dla ImageMagick'a
Group:		Development/Languages/Perl  
Group(pl):	Programowanie/Jêzyki/Perl
Requires:	%{name} = %{version}
Requires:	perl >= 5.005

%description perl
This is the ImageMagick perl support package.  It perl modules and support
files for access to ImageMagick library from perl without unuseful forking
or such.

%description -l pl perl
Biblioteki i modu³y umo¿liwiaj±ce korzystanie z ImageMagick'a z poziomu
perla. 

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
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
install -d $RPM_BUILD_ROOT/usr/{man/man3,lib/perl5/%{buildarch}-linux-thread/5.00502/}

make install DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=$RPM_BUILD_ROOT/usr \
	INSTALLMAN3DIR=$RPM_BUILD_ROOT/usr/man/man3

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*
strip --strip-debug $RPM_BUILD_ROOT/usr/lib/perl5/site_perl/*/*/auto/Image/Magick/Magick.so

gzip -9nf $RPM_BUILD_ROOT/usr/{X11R6/man/man*/*,man/man3/*}

gzip -9nf ImageMagick.html README.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/lib/lib*.so.*.*

#/usr/X11R6/share/ImageMagick

%attr(755,root,root) /usr/X11R6/bin/animate
%attr(755,root,root) /usr/X11R6/bin/combine
%attr(755,root,root) /usr/X11R6/bin/convert
%attr(755,root,root) /usr/X11R6/bin/display
%attr(755,root,root) /usr/X11R6/bin/identify
%attr(755,root,root) /usr/X11R6/bin/import
%attr(755,root,root) /usr/X11R6/bin/mogrify
%attr(755,root,root) /usr/X11R6/bin/montage
%attr(755,root,root) /usr/X11R6/bin/xtp

/usr/X11R6/man/man[145]/*

%files devel
%defattr(644,root,root,755)
%doc www ImageMagick.html.gz README.txt.gz

#%attr(755,root,root) /usr/X11R6/bin/Magick-config
%attr(755,root,root) /usr/X11R6/lib/lib*.so

/usr/X11R6/include/X11/magick

%files static
%attr(644,root,root) /usr/X11R6/lib/lib*.a

%files perl
%defattr(644,root,root,755)
/usr/lib/perl5/site_perl/*/*/Image
%dir /usr/lib/perl5/site_perl/*/*/auto/Image
%dir /usr/lib/perl5/site_perl/*/*/auto/Image/Magick
/usr/lib/perl5/site_perl/*/*/auto/Image/Magick/autosplit.ix
/usr/lib/perl5/site_perl/*/*/auto/Image/Magick/Magick.bs
%attr(755,root,root) /usr/lib/perl5/site_perl/*/*/auto/Image/Magick/Magick.so
/usr/man/man3/Image::Magick.3.gz

%changelog
* Thu Mar 11 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.1.0-5]
- removed man group from man pages,
- "make install" with using DESTDIR,
- changed Group in devel and static,
- downgrade to 4.1.0 - all above versions have buggy conversions tga->gif
  (maybe more).

* Tue Feb  9 1999 Micha³ Kuratczyk <kurkens@polbox.com
  [4.1.8-2d]
- added gzipping documentation
- fixed pl translations
- cosmetic changes

* Sun Jan 24 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.1.8-1d]
- added Group(pl),
- fixed permission on lib*.so* files (must be 755),
- changed Requires for freetype (= 1.2),
- many fixes im pl translations.

* Sat Dec  7 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.1.5-1]
- added gzipping man pages,
- /usr/bin/Magick-config moved to devel,
- added /usr/X11R6/share/ImageMagick/delegates.mgk file to main,
- more man pages on levels 3, 4 and 5,
- added LDFLAGS="-s" in ./configure enviroment.

* Sun Nov  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.1.3-2]
- simplification in perl subpackage,
- man pages in perl subpackage moved to /usr/man/man3,
- build against perl 5.005 (added also "Requires: perl >= 5.005" in perl).

* Sat Aug  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.0.8-1]
- added rest pl translations in subpackages,
- added static subpackage.

* Fri Jul 17 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [4.0.7-2]
- added pl translation,
- build against GNU libc-2.1.

* Sun Jun 14 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.0.7-1]
- added Khimenko Victor <khim@sch57.msk.ru> style modyfication for making
  separated subpackage perl stuff and all my old modyfication which was
  prepared and uploaded to contrib before RH 5.1,
- added "Requires: freetype >= 1.1" for main package.

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 4.0.5

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- updated to 4.0.4
- added BuildRoot

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 3.8.3 to 3.9.1
- removed PNG patch (appears to be fixed)

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>
- build against new libpng

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 20 1997 Michael Fulbright <msf@redhat.com>
- updated to version 3.8.3.
- updated source and url tags.
