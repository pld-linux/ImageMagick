Summary:     image display, conversion, and manipulation under X
Summary(de): Darstellen, Konvertieren und Bearbeiten von Grafiken unter X
Summary(fr): Visualisation, conversion, et manipulation d'images sous X.
Summary(pl): Narz�dzie do wy�wietlania, konwersji i manipulacji grafikami
Summary(tr): X alt�nda resim g�sterme, �evirme ve de�i�iklik yapma
Name:        ImageMagick
Version:     4.0.9
Release:     1
Copyright:   freeware
Group:       X11/Applications/Graphics
Source:      ftp://ftp.wizards.dupont.com/pub/ImageMagick/%{name}-%{version}.tar.gz
URL:         http://www.wizards.dupont.com/cristy/ImageMagick.html
Requires:    freetype >= 1.1
Buildroot:   /tmp/%{name}-%{version}-root

%description
ImageMagick is an image display, conversion, and manipulation tool.
It runs under X windows.  It is very powerful in terms of it's 
ability to allow the user to edit images.  It can handle many 
different formats as well.

%description -l de
ImageMagick ist ein Tool zur Bildanzeige, -konvertierung und 
-manipulation, das unter X-Windows l�uft. Es ist enorm leitungsf�hig 
in Bezug auf die Grafikmanipulationsfunktionen, die es dem Anwender 
bietet, und auf die Vielfalt der unterst�tzten Formate.

%description -l fr
ImageMagick est un outil d'affichage, de conversion et de manipulation
d'images. Il tourne sous X Window et est tr�s puissant en termes
de capacit� d'�dition des images. Il peut aussi g�rer de nombreux
formats diff�rents.

%description -l fr
ImageMagick est un outil d'affichage, de conversion et de manipulation
d'images. Il tourne sous X Window et est tr�s puissant en termes
de capacit� d'�dition des images. Il peut aussi g�rer de nombreux
formats diff�rents.

%description -l pl
ImageMagic jest narz�dziem do manipulacji, konwersji i wy�wietlania.
W skk�ad pakietu wchod�a zar�wno narz�dzia X'ami. Jest to narz�dzie pot�ne ;)
i u�yteczne podczas pracy z wieloma formatami graficznymi.

%description -l tr
ImageMagick bir resim g�sterme, �evirme ve de�i�iklik yapma program�d�r. X
Window pencereleme sistemi alt�nda �al���r. Kullan�c�ya resimler �zerinde
de�i�iklik yapma a��s�ndan pek �ok olanak sunar. Bir �ok resim bi�imini
rahatl�kla kullanabilir.

%package  devel
Summary:     static libraries and header files for ImageMagick development
Summary(pl): Biblioteki statyczne i pliki nag��wkowe dla ImageMagick'a
Group:       X11/Libraries
Requires:    %{name} = %{version}

%description devel
This is the ImageMagick development package.  It includes the static
libraries and header files for use in developing your own applications
that make use of the ImageMagick code and/or APIs.

%description -l de devel
Dies ist das ImageMagick-Entwicklerpaket. Es enth�lt die statischen
Libraries und Header-Dateien zum Entwickeln von Anwendungen,
die ImageMagick-Code und/oder -APIs nutzen.

%description -l fr devel
Paquetage de d�veloppement ImageMagick. Contient les biblioth�ques
statiques et les en-t�tes utilis�s pour cr�er vos propres applications
utilisant le code d'ImageMagick et/ou ses APIs.

%description -l pl devel
Pakiet ten zawieraj�cy pliki potrzebne przy kompilowaniu program�w
wykorzystuj�cyh blibbliotek� ImageMagick takie ja pliki nag�owkowe,
biblioteki statyczne i dokumentacj� niezb�ddn� przy pisaniu w��snych
program�w z wykorzystaniem API jakie udost�pnia ImageMagick.

%description -l tr devel
Bu paket, ImageMagick uygulama aray�z�n� kullanan programlar geli�tirmek
i�in gereken ba�l�k dosyalar�n� ve kitapl�klar� i�erir.

%package  static
Summary:     header files for ImageMagick development
Summary(pl): Pliki nag��wkowe dla ImageMagick'a
Group:       X11/Libraries
Requires:    %{name}-devel = %{version}

%description static
This package contains header files for use in developing your own
applications that make use of the ImageMagick code and/or APIs.

%description -l pl devel
Pakiet ten zawiera pliki nag�owkowe i dokumentacj� niezb�ddn� przy pisaniu
w��snych program�w z wykorzystaniem API jakie udost�pnia ImageMagick.

%package  perl
Summary:     libraries and modules for access to ImageMagick from perl
Summary(pl): Biblioteki i modu�y umo�liwiaj�ce korzystanie z ImageMagick'a z poziomu perl'a
Group:       Development/Libraries/Perl
Requires:    %{name} = %{version}

%description perl
This is the ImageMagick perl support package.  It perl modules and support
files for access to ImageMagick library from perl without unuseful forking
or such.

%description -l pl perl
Biblioteki i modu�y umo�liwiaj�ce korzystanie z ImageMagick'a z poziomu
perla. 

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr \
	--libdir=/usr/X11R6/lib \
	--includedir=/usr/X11R6/include/X11/magick \
	--enable-shared \
	--enable-lzw \
	--enable-16bit-pixel \
	--with-perl \
	--with-x
make 

%install
rm -fr $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/perl5/%{buildarch}-linux/5.00404/
make install \
	prefix=$RPM_BUILD_ROOT/usr \
	PREFIX=$RPM_BUILD_ROOT/usr \
	libdir=$RPM_BUILD_ROOT/usr/X11R6/lib \
	includedir=$RPM_BUILD_ROOT/usr/X11R6/include/X11/magick

strip $RPM_BUILD_ROOT/usr/{X11R6/lib/lib*.so.*.*,bin/*}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README.txt mpeglib.*
/usr/X11R6/lib/lib*.so.*.*
%attr(711, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*

%files devel
%defattr(644, root, root, 755)
%doc www ImageMagick.html
%dir /usr/X11R6/include/X11/magick
/usr/X11R6/include/X11/magick/*.h
/usr/X11R6/lib/lib*.so

%files static
%attr(644, root, root) /usr/X11R6/lib/lib*.a

%files perl
%defattr(644, root, root, 755)
%dir /usr/lib/perl5/site_perl/Image
/usr/lib/perl5/site_perl/Image/Magick.pm
%dir /usr/lib/perl5/site_perl/auto/Image
%dir /usr/lib/perl5/site_perl/auto/Image/Magick
/usr/lib/perl5/site_perl/auto/Image/Magick/autosplit.ix
%dir /usr/lib/perl5/site_perl/%{buildarch}-linux/auto/Image
%dir /usr/lib/perl5/site_perl/%{buildarch}-linux/auto/Image/Magick
/usr/lib/perl5/site_perl/%{buildarch}-linux/auto/Image/Magick/Magick.bs
/usr/lib/perl5/site_perl/%{buildarch}-linux/auto/Image/Magick/Magick.so
%attr(644, root, man) /usr/lib/perl5/man/man3/*

%changelog
* Mon Sep  7 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.0.8-2]
- changed permission on binaries to 711.

* Sat Aug  1 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.0.8-1]
- added rest pl translations in subpackages,
- added static subpackage.

* Fri Jul 17 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [4.0.7-2]
- added some pl translatiin.

* Sun Jun 14 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.0.7-1]
- added Khimenko Victor <khim@sch57.msk.ru> style modyfication for making
  separated subpackage perl stuff and all my old modyfication witch was
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
