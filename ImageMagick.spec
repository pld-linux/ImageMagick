%include	/usr/lib/rpm/macros.perl
Summary:	Image display, conversion, and manipulation under X
Summary(de):	Darstellen, Konvertieren und Bearbeiten von Grafiken unter X
Summary(fr):	Visualisation, conversion, et manipulation d'images sous X
Summary(pl):	Narzêdzie do wy¶wietlania, konwersji i manipulacji grafikami
Summary(tr):	X altında resim gösterme, çevirme ve değişiklik yapma
Name:		ImageMagick
Version:	5.3.9
Release:	1
Epoch:		1
License:	Freeware
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Group(pt):	X11/Aplicações/Gráficos
Source0:	ftp://ftp.simplesystems.org/pub/ImageMagick/%{name}-%{version}.tar.gz
Patch0:		%{name}-libpath.patch
Patch1:		%{name}-perlpaths.patch
Patch2:		%{name}-libwmf.patch
Patch3:		%{name}-DESTDIR.patch
Patch4:		%{name}-amfix.patch
URL:		http://www.imagemagick.org/
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	XFree86-devel
BuildRequires:	XFree86-DPS-devel
BuildRequires:	bzip2-devel >= 1.0.1
BuildRequires:	freetype-devel >= 2.0.2-2
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libwmf-devel
BuildRequires:	libtool
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	libxml2-devel >= 2.0
#BuildRequires:	lcms-devel
#BuildRequires:	fpx-devel
#BuildRequires:	hdf-devel
#BuildRequires:	jbigkit-devel
#BuildRequires:	jasper-devel
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
manipulation, -das unter X-Windows läuft. Es ist enorm leitungsfähig
in Bezug auf die Grafikmanipulationsfunktionen, die es dem Anwender
bietet, und auf die Vielfalt der unterstützten Formate.

%description -l fr
ImageMagick est un outil d'affichage, de conversion et de manipulation
d'images. Il tourne sous X Window et est très puissant en termes de
capacité d'édition des images. Il peut aussi gérer de nombreux formats
différents.

%description -l pl
ImageMagick jest narzêdziem do manipulacji, konwersji i wy¶wietlania.
W sk³ad pakietu wchodz± zarówno narzêdzia X Window jak i do u¿ywania z
linii poleceñ umo¿liwiaj±ce edycjê plików graficznych. Narzêdzia z
pakietu ImageMagick potrafi± obs³u¿yæ wiele ró¿nych formatów
graficznych.

%description -l tr
ImageMagick bir resim gösterme, çevirme ve değişiklik yapma
programıdır. X Window pencereleme sistemi altında çalışır. Kullanıcıya
resimler üzerinde değişiklik yapma açısından pek çok olanak sunar. Bir
çok resim biçimini rahatlıkla kullanabilir.

%package devel
Summary:	Libraries and header files for ImageMagick development
Summary(pl):	Biblioteki i pliki nag³ówkowe dla ImageMagick
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description devel
This is the ImageMagick development package. It includes header files
for use in developing your own applications that make use of the
ImageMagick code and/or APIs.

%description -l de devel
Dies ist das ImageMagick-Entwicklerpaket. Es enthält Header-Dateien
zum Entwickeln von Anwendungen, die ImageMagick-Code und/oder -APIs
nutzen.

%description -l fr devel
Paquetage de développement ImageMagick. Contient les bibliothèques
statiques et les en-têtes utilisés pour créer vos propres applications
utilisant le code d'ImageMagick et/ou ses APIs.

%description -l pl devel
Pakiet ten zawieraja pliki potrzebne przy kompilowaniu programów
wykorzystuj±cych blibliotekê ImageMagick takie jak pliki nag³ówkowe i
dokumentacjê niezbêdn± przy pisaniu w³asnych programów z
wykorzystaniem API jakie udostêpnia ImageMagick.

%description -l tr devel
Bu paket, ImageMagick uygulama arayüzünü kullanan programlar
geliştirmek için gereken başlık dosyalarını ve kitaplıkları içerir.

%package static
Summary:	ImageMagick static libraries
Summary(pl):	Biblioteki statyczne ImageMagick
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
ImageMagick static libraries.

%description -l pl static
Biblioteki statyczne ImageMagick.

%package perl
Summary:	Libraries and modules for access to ImageMagick from perl
Summary(pl):	Biblioteki i modu³y perla dla ImageMagick
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Requires:	%{name}-libs = %{version}

%description perl
This is the ImageMagick perl support package. It perl modules and
support files for access to ImageMagick library from perl without
unuseful forking or such.

%description -l pl perl
Biblioteki i modu³y umo¿liwiaj±ce korzystanie z ImageMagick z poziomu
perla.

%package libs
Summary:	ImageMagick libraries
Summary(pl):	Biblioteki ImageMagick
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ

%description libs
ImageMagick libraries.

%description -l pl libs
Biblioteki ImageMagick.

%package c++
Summary:	ImageMagick Magick++ library
Summary(pl):	Biblioteka Magick++
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-libs = %{version}

%description c++
This package contains the Magick++ library, a C++ binding to the
ImageMagick graphics manipulation library.

Install ImageMagick-c++ if you want to use any applications that use
Magick++.

%description -l pl c++
Pakiet zawiera bibliotekê Magick++ - interfejs w C++ do biblioteki
ImageMagick. Jest potrzebny do uruchamiania programów korzystaj±cych z
Magick++.

%package c++-devel
Summary:	C++ bindings for the ImageMagick library
Summary(pl):	Pliki nag³ówkowe z interfejsem C++ do ImageMagick
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
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
Pakiet zawiera pliki nag³ówkowe potrzebne do kompilowania programów
korzystaj±cych z Magick++.

%package c++-static
Summary:	C++ bindings for the ImageMagick - static library
Summary(pl):	Interfejs C++ do ImageMagick - biblioteka statyczna
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
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
%patch4 -p1

# fix lcms.h include path
perl -pi -e 's@lcms/lcms\.h@lcms.h@' magick/transform.c

%build
libtoolize --copy --force
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
