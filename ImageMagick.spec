%include	/usr/lib/rpm/macros.perl
Summary:	Image display, conversion, and manipulation under X
Summary(de):	Darstellen, Konvertieren und Bearbeiten von Grafiken unter X
Summary(fr):	Visualisation, conversion, et manipulation d'images sous X.
Summary(pl):	Narz�dzie do wy�wietlania, konwersji i manipulacji grafikami
Summary(tr):	X alt�nda resim g�sterme, �evirme ve de�i�iklik yapma
Name:		ImageMagick
Version:	5.2.4
Release: 	1
Copyright:	freeware
Serial:		1
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://ftp.wizards.dupont.com/pub/ImageMagick/%{name}-%{version}.tar.gz
Patch0:		ImageMagick-libpath.patch
Patch1:		ImageMagick-perlpaths.patch
URL:		http://www.wizards.dupont.com/cristy/ImageMagick.html
BuildRequires:	perl => 5.005_03-14
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel >= 1.0.1
BuildRequires:	freetype-devel
Requires:	%{name}-libs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man
%define		_includedir	%{_prefix}/include/X11
%define		_perlmandir	/usr/share/man

%description
ImageMagick is an image display, conversion, and manipulation tool. It
runs under X windows. It is very powerful in terms of it's ability to
allow the user to edit images. It can handle many different formats as
well.

%description -l de
ImageMagick ist ein Tool zur Bildanzeige, -konvertierung und
manipulation,
- -das unter X-Windows l�uft. Es ist enorm leitungsf�hig in Bezug auf
  die Grafikmanipulationsfunktionen, die es dem Anwender bietet, und auf
  die Vielfalt der unterst�tzten Formate.

%description -l fr
ImageMagick est un outil d'affichage, de conversion et de manipulation
d'images. Il tourne sous X Window et est tr�s puissant en termes de
capacit� d'�dition des images. Il peut aussi g�rer de nombreux formats
diff�rents.

%description -l pl
ImageMagic jest narz�dziem do manipulacji, konwersji i wy�wietlania. W
sk�ad pakietu wchodz� zar�wno narz�dzia X Window jak i do u�ywania z
linii polece� umo�liwiaj�ce edycj� plik�w graficznych. Narz�dzia z
pakietu ImageMagic potrafi� obs�u�y� wiele r�ncyh format�w
graficznych.

%description -l tr
ImageMagick bir resim g�sterme, �evirme ve de�i�iklik yapma
program�d�r. X Window pencereleme sistemi alt�nda �al���r. Kullan�c�ya
resimler �zerinde de�i�iklik yapma a��s�ndan pek �ok olanak sunar. Bir
�ok resim bi�imini rahatl�kla kullanabilir.

%package devel
Summary:	Libraries and header files for ImageMagick development
Summary(pl):	Biblioteki i pliki nag��wkowe dla ImageMagick'a
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This is the ImageMagick development package. It includes the static
libraries and header files for use in developing your own applications
that make use of the ImageMagick code and/or APIs.

%description -l de devel
Dies ist das ImageMagick-Entwicklerpaket. Es enth�lt die statischen
Libraries und Header-Dateien zum Entwickeln von Anwendungen, die
ImageMagick-Code und/oder -APIs nutzen.

%description -l fr devel
Paquetage de d�veloppement ImageMagick. Contient les biblioth�ques
statiques et les en-t�tes utilis�s pour cr�er vos propres applications
utilisant le code d'ImageMagick et/ou ses APIs.

%description -l pl devel
Pakiet ten zawieraja pliki potrzebne przy kompilowaniu program�w
wykorzystuj�cych blibliotek� ImageMagick takie jak pliki nag��wkowe,
biblioteki statyczne i dokumentacj� niezb�dn� przy pisaniu w�asnych
program�w z wykorzystaniem API jakie udost�pnia ImageMagick.

%description -l tr devel
Bu paket, ImageMagick uygulama aray�z�n� kullanan programlar
geli�tirmek i�in gereken ba�l�k dosyalar�n� ve kitapl�klar� i�erir.

%package static
Summary:	ImageMagick static libraries
Summary(pl):	Biblioteki statyczne ImageMagick
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
ImageMagick static libraries.

%description -l pl devel
Biblioteki statyczne ImageMagick.

%package perl
Summary:	libraries and modules for access to ImageMagick from perl
Summary(pl):	Biblioteki i modu�y perl dla ImageMagick'a
Group:		Development/Languages/Perl  
Group(pl):	Programowanie/J�zyki/Perl
Requires:	%{name} = %{version}
Requires:	%{perl_sitearch}
%requires_eq	perl

%description perl
This is the ImageMagick perl support package. It perl modules and
support files for access to ImageMagick library from perl without
unuseful forking or such.

%description -l pl perl
Biblioteki i modu�y umo�liwiaj�ce korzystanie z ImageMagick'a z
poziomu perla.

%package libs
Summary:	ImageMagick libraries
Summary(pl):	Biblioteki ImageMagick
Group:		X11/Libraries
Group(pl):	X11/Biblioteki

%description libs
ImageMagick libraries.

%description -l pl libs
Biblioteki ImageMagick.

%prep
%setup  -q
%patch0 -p0
%patch1 -p0

%build
aclocal
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-shared \
	--enable-lzw \
	--enable-16bit-pixel \
	--with-perl \
	--with-ttf \
	--with-x

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-perl

%{__make} install DESTDIR=$RPM_BUILD_ROOT 
install PerlMagick/demo/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-perl

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* \
	$RPM_BUILD_ROOT/%{perl_sitearch}/auto/Image/Magick/Magick.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Image/Magick
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT{%{_mandir}/man*/*,%{_perlmandir}/man3/*} \
	README.txt

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files
%defattr(644,root,root,755)
%{_datadir}/ImageMagick

%attr(755,root,root) %{_bindir}/animate
%attr(755,root,root) %{_bindir}/combine
%attr(755,root,root) %{_bindir}/convert
%attr(755,root,root) %{_bindir}/display
%attr(755,root,root) %{_bindir}/identify
%attr(755,root,root) %{_bindir}/import
%attr(755,root,root) %{_bindir}/mogrify
%attr(755,root,root) %{_bindir}/montage

%{_mandir}/man[145]/*

%files devel
%defattr(644,root,root,755)
%doc www ImageMagick.html README.txt.gz

%attr(755,root,root) %{_bindir}/Magick-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%{_includedir}/magick

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files perl
%defattr(644,root,root,755)
%{perl_sitearch}/Image
%dir %{perl_sitearch}/auto/Image
%dir %{perl_sitearch}/auto/Image/Magick
%{perl_sitearch}/auto/Image/Magick/.packlist
%{perl_sitearch}/auto/Image/Magick/autosplit.ix
%{perl_sitearch}/auto/Image/Magick/Magick.bs
%attr(755,root,root) %{perl_sitearch}/auto/Image/Magick/Magick.so
%{_perlmandir}/man3/Image::Magick.*
/usr/src/examples/%{name}-perl
