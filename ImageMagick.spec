%include	/usr/lib/rpm/macros.perl
Summary:	Image display, conversion, and manipulation under X
Summary(de):	Darstellen, Konvertieren und Bearbeiten von Grafiken unter X
Summary(fr):	Visualisation, conversion, et manipulation d'images sous X
Summary(pl):	Narz�dzie do wy�wietlania, konwersji i manipulacji grafikami
Summary(tr):	X alt�nda resim g�sterme, �evirme ve de�i�iklik yapma
Name:		ImageMagick
Version:	5.3.1
Release:	2
Epoch:		1
License:	Freeware
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://ftp.simplesystems.org/pub/ImageMagick/%{name}-%{version}.tar.gz
Patch0:		%{name}-libpath.patch
Patch1:		%{name}-perlpaths.patch
Patch2:		%{name}-delegates-destdir.patch
Patch3:		%{name}-libwmf.patch
URL:		http://www.imagemagick.org/
BuildRequires:	perl => 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	XFree86-devel
BuildRequires:	XFree86-DPS-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel >= 1.0.1
BuildRequires:	freetype-devel >= 2.0.2-2
BuildRequires:	libwmf-devel
#BuildRequires:	libxml2-devel >= 2.0
#BuildRequires:	lcms-devel
#BuildRequires:	fpx-devel
#BuildRequires:	hdf-devel
#BuildRequires:	jbigkit-devel
BuildRequires:	autoconf
BuildRequires:	automake >= 1.4d
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

%description -l fr
ImageMagick est un outil d'affichage, de conversion et de manipulation
d'images. Il tourne sous X Window et est tr�s puissant en termes de
capacit� d'�dition des images. Il peut aussi g�rer de nombreux formats
diff�rents.

%description -l pl
ImageMagick jest narz�dziem do manipulacji, konwersji i wy�wietlania. W
sk�ad pakietu wchodz� zar�wno narz�dzia X Window jak i do u�ywania z
linii polece� umo�liwiaj�ce edycj� plik�w graficznych. Narz�dzia z
pakietu ImageMagick potrafi� obs�u�y� wiele r�nych format�w
graficznych.

%description -l tr
ImageMagick bir resim g�sterme, �evirme ve de�i�iklik yapma
program�d�r. X Window pencereleme sistemi alt�nda �al���r. Kullan�c�ya
resimler �zerinde de�i�iklik yapma a��s�ndan pek �ok olanak sunar. Bir
�ok resim bi�imini rahatl�kla kullanabilir.

%package devel
Summary:	Libraries and header files for ImageMagick development
Summary(pl):	Biblioteki i pliki nag��wkowe dla ImageMagick
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This is the ImageMagick development package. It includes header files
for use in developing your own applications that make use of the
ImageMagick code and/or APIs.

%description -l de devel
Dies ist das ImageMagick-Entwicklerpaket. Es enth�lt Header-Dateien zum
Entwickeln von Anwendungen, die ImageMagick-Code und/oder -APIs nutzen.

%description -l fr devel
Paquetage de d�veloppement ImageMagick. Contient les biblioth�ques
statiques et les en-t�tes utilis�s pour cr�er vos propres applications
utilisant le code d'ImageMagick et/ou ses APIs.

%description -l pl devel
Pakiet ten zawieraja pliki potrzebne przy kompilowaniu program�w
wykorzystuj�cych blibliotek� ImageMagick takie jak pliki nag��wkowe
i dokumentacj� niezb�dn� przy pisaniu w�asnych program�w
z wykorzystaniem API jakie udost�pnia ImageMagick.

%description -l tr devel
Bu paket, ImageMagick uygulama aray�z�n� kullanan programlar
geli�tirmek i�in gereken ba�l�k dosyalar�n� ve kitapl�klar� i�erir.

%package static
Summary:	ImageMagick static libraries
Summary(pl):	Biblioteki statyczne ImageMagick
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
ImageMagick static libraries.

%description -l pl devel
Biblioteki statyczne ImageMagick.

%package perl
Summary:	libraries and modules for access to ImageMagick from perl
Summary(pl):	Biblioteki i modu�y perl dla ImageMagick
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Requires:	%{name}-libs = %{version}

%description perl
This is the ImageMagick perl support package. It perl modules and
support files for access to ImageMagick library from perl without
unuseful forking or such.

%description -l pl perl
Biblioteki i modu�y umo�liwiaj�ce korzystanie z ImageMagick z
poziomu perla.

%package libs
Summary:	ImageMagick libraries
Summary(pl):	Biblioteki ImageMagick
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki

%description libs
ImageMagick libraries.

%description -l pl libs
Biblioteki ImageMagick.

%package c++
Summary:	ImageMagick Magick++ library
Summary(pl):	Biblioteka Magick++
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-libs = %{version}

%description c++
This package contains the Magick++ library, a C++ binding to the
ImageMagick graphics manipulation library.

Install ImageMagick-c++ if you want to use any applications that use
Magick++.

%description -l pl c++
Pakiet zawiera bibliotek� Magick++ - interfejs w C++ do biblioteki
ImageMagick. Jest potrzebny do uruchamiania program�w korzystaj�cych
z Magick++.

%package c++-devel
Summary:	C++ bindings for the ImageMagick library
Summary(pl):	Pliki nag��wkowe z interfejsem C++ do ImageMagick
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
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

%description -l pl c++-devel
Pakiet zawiera pliki nag��wkowe potrzebne do kompilowania program�w
korzystaj�cych z Magick++.

%package c++-static
Summary:	C++ bindings for the ImageMagick - static library
Summary(pl):	Interfejs C++ do ImageMagick - biblioteka statyczna
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-c++-devel = %{version}
Requires:	%{name}-devel = %{version}

%description c++-static
C++ bindings for the ImageMagick - static library.

%description -l pl c++-static
Biblioteka Magick++ w wersji statycznej.

%prep
%setup  -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1

# fix typo
perl -pi -e 's@htmlc\.@html.c@' coders/Makefile.am
# fix lcms.h include path
perl -pi -e 's@lcms/lcms\.h@lcms.h@' magick/transform.c

%build
aclocal
autoconf
automake -a -c
%configure \
	--enable-shared \
	--enable-lzw \
	--enable-16bit-pixel \
	--with-perl \
	--with-ttf \
	--with-x \
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

gzip -9nf README.txt

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post   c++ -p /sbin/ldconfig
%postun c++ -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

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
%attr(755,root,root) %{_bindir}/combine
%attr(755,root,root) %{_bindir}/convert
%attr(755,root,root) %{_bindir}/display
%attr(755,root,root) %{_bindir}/identify
%attr(755,root,root) %{_bindir}/import
%attr(755,root,root) %{_bindir}/mogrify
%attr(755,root,root) %{_bindir}/montage

%{_mandir}/man1/[Iacdim]*

%files devel
%defattr(644,root,root,755)
%doc images www ImageMagick.html README.txt.gz

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
